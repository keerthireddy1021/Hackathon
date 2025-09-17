# rag_engine.py
# Placeholder for Retrieval-Augmented Generation (M3)

def get_answer(query, session_id):
    """
    Dummy function for now.
    Later it will call the RAG pipeline:
    1. Search vector DB
    2. Send top chunks + query to LLM
    3. Return generated answer + sources
    """
    # Example static answer (to test API)
   # answer = f"Received query: '{query}' (Session: {session_id})"
    #sources = ["sample_doc.pdf"]
   # return answer, sources

    # return answer_text, [list_of_sources]
    return "Mock answer for testing", ["mock_doc.pdf"]

