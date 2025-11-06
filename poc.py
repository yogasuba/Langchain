# poc.py - Run with OpenAI


from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

import os

def load_documents(path):
    """Load a PDF or text file."""
    if path.lower().endswith(".pdf"):
        loader = PyPDFLoader(path)
        docs = loader.load()
    else:
        loader = TextLoader(path, encoding="utf-8")
        docs = loader.load()
    return docs

def build_index(docs):
    """Split documents, create embeddings, and store them in Chroma."""
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")
    return db

def run_qa(db):
    """Run a simple Q&A loop using modern RAG pattern."""
    
    # Define the prompt template
    template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Answer:"""
    
    prompt = ChatPromptTemplate.from_template(template)
    
    # Set up the LLM
    llm = ChatOpenAI(temperature=0)
    
    # Create the RAG chain
    retriever = db.as_retriever()
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    print("\n*** Ready. Ask questions about the document (type 'exit' to quit). ***\n")
    while True:
        query = input("Question: ").strip()
        if query.lower() in ("exit", "quit"):
            break
        try:
            answer = rag_chain.invoke(query)
            print("\nAnswer:\n", answer)
        except Exception as e:
            print(f"\nError: {e}")
        print("\n" + "-"*60 + "\n")

def main():
    path = input("Enter document path (sample.pdf or sample.txt): ").strip()
    if not os.path.exists(path):
        print("File not found:", path)
        return

    print("Loading document...")
    docs = load_documents(path)

    print("Building index (this may take a moment)...")
    db = build_index(docs)

    run_qa(db)

if __name__ == "__main__":
    main()

