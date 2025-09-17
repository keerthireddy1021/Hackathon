from flask import Flask, request, jsonify
from rag_engine import get_answer   # M3 function
from translator import detect_language, translate   # M4 functions
import json
import os
from datetime import datetime

app = Flask(__name__)

# File for logs
LOG_FILE = "chat_logs.jsonl"

def log_interaction(session_id, query, answer, lang, sources):
    """Save each chat interaction in JSON Lines format."""
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": session_id,
        "query": query,
        "answer": answer,
        "language": lang,
        "sources": sources
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Parse JSON safely
        data = request.get_json(force=True, silent=True)
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400

        query = data.get("query")
        session_id = data.get("session_id", "default")

        # Validate input
        if not query or not isinstance(query, str):
            return jsonify({"error": "Missing or invalid 'query'"}), 400

        # Step 1: Detect language
        lang = detect_language(query)

        # Step 2: Translate query → English (if needed)
        query_en = translate(query, "en") if lang != "en" else query

        # Step 3: Get answer from RAG engine
        answer_en, sources = get_answer(query_en, session_id)

        # Step 4: Translate answer back to user’s language
        answer = translate(answer_en, lang) if lang != "en" else answer_en

        # Step 5: Log the interaction
        log_interaction(session_id, query, answer, lang, sources)

        # Step 6: Return response
        return jsonify({
            "answer": answer,
            "sources": sources,
            "language": lang
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Ensure log file exists
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w", encoding="utf-8").close()

    app.run(host="0.0.0.0", port=5000, debug=True)
