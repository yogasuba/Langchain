# poc_local.py - Completely free local version

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
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
    """Split documents and create embeddings using local model."""
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    # Use FREE local embeddings - no API calls
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    # Create vector store
    db = Chroma.from_documents(
        chunks, 
        embeddings, 
        persist_directory="./chroma_db"
    )
    return db

def search_documents(db, query):
    """Search for relevant document sections."""
    # Find most relevant document chunks
    relevant_docs = db.similarity_search(query, k=3)
    
    results = []
    for i, doc in enumerate(relevant_docs, 1):
        results.append({
            'section': i,
            'content': doc.page_content,
            'source': doc.metadata.get('source', 'Unknown')
        })
    return results

def display_results(results, query):
    """Display the search results in a readable format."""
    print(f"\n🔍 Search results for: '{query}'")
    print("=" * 60)
    
    for result in results:
        print(f"\n📄 Section {result['section']} (Source: {result['source']})")
        print("-" * 40)
        
        # Display content (truncated if too long)
        content = result['content']
        if len(content) > 500:
            print(content[:500] + "...")
        else:
            print(content)
    
    print("\n" + "=" * 60)

def main():
    print("🤖 Local Document Search System (100% FREE - No APIs)")
    print("This system uses local AI models - no internet or billing required!\n")
    
    path = input("Enter document path (sample.pdf or sample.txt): ").strip()
    if not os.path.exists(path):
        print("❌ File not found:", path)
        return

    print("📂 Loading document...")
    docs = load_documents(path)
    print(f"✅ Loaded {len(docs)} document sections")

    print("🔄 Building search index with local embeddings...")
    print("   (This may take a minute for the first time as it downloads the model)")
    db = build_index(docs)
    print("✅ Search index ready!")

    print("\n" + "🌟" * 25)
    print("💬 Ready to search your documents!")
    print("Type your questions and I'll find the most relevant sections.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("❓ Your question: ").strip()
        if query.lower() in ("exit", "quit", "bye"):
            print("👋 Goodbye!")
            break
        
        if not query:
            continue

        print("🔎 Searching...")
        try:
            results = search_documents(db, query)
            display_results(results, query)
            
            # Simple "answer" by showing the most relevant section
            if results:
                print(f"\n💡 Based on the most relevant section, here's what I found:")
                print(f"\"{results[0]['content'][:300]}...\"")
            else:
                print("\n❌ No relevant information found in the documents.")
                
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()