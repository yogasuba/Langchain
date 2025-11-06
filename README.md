# 📘 Document Q&A System

A flexible **document question-answering system** that can run both **with OpenAI APIs** and **completely locally** without any external services.

---

## ✨ Features

- 📄 **Support for PDF and Text documents**  
- 🔍 **Semantic search** using vector embeddings  
- 💬 **Question-answering** with relevant context  
- 🌐 **Optional OpenAI integration** for advanced responses  
- 💯 **100% local mode available** (no internet required)  
- 🚀 **Fast and efficient document processing**

---

## ⚙️ Installation

### **Prerequisites**

- Python 3.8+
- `pip` package manager

### **Install Dependencies**

```bash
# Basic installation
pip install langchain langchain-community langchain-text-splitters chromadb

# For local embeddings (FREE mode)
pip install sentence-transformers torch

# For OpenAI integration (optional)
pip install langchain-openai openai

# For PDF support
pip install pypdf

🧠 Usage
Method 1: Local Mode (FREE - No API Keys Required)

Run the system completely locally without any external services:

python poc_local.py


Features:

Uses local embedding model (all-MiniLM-L6-v2)

Works fully offline after first run

No costs or API limits

Performs document search and retrieval

Method 2: OpenAI Mode (With API Key)

Run with OpenAI for enhanced question-answering:

# Set your OpenAI API key
set OPENAI_API_KEY=your_api_key_here

# Run the script
python poc.py


Features:

Advanced GPT-powered responses

Better contextual understanding

More natural language generation


📂 File Structure
document-qa-system/
│
├── poc.py                 # Main script with OpenAI integration
├── poc_local.py           # Completely local version
├── sample.txt             # Example document
├── chroma_db/             # Vector database storage
└── README.md              # This file


🔍 How It Works

Document Loading – Reads your PDF or text files

Text Splitting – Breaks documents into manageable chunks

Embedding Generation – Converts text to numerical vectors

Local: Uses HuggingFace models

OpenAI: Uses OpenAI’s embedding API

Vector Storage – Stores embeddings in ChromaDB

Similarity Search – Finds relevant sections for queries

Answer Generation – Provides answers based on retrieved context

📄 Supported Document Formats
Format	Description
PDF (.pdf)	Research papers, manuals, books
Text (.txt)	Notes, articles, documentation
💬 Example Questions to Ask
For Technical Documents:

What is the main concept discussed?

Explain [technical term] in simple terms

What are the key findings?

How does [process] work?

For Research Papers:

What is the research methodology?

What are the conclusions?

What problem does this solve?

What data was used?

For Manuals/Guides:

How do I perform [specific task]?

What are the system requirements?

Troubleshooting steps for [issue]

⚙️ Configuration
Local Mode Settings

Embedding Model: sentence-transformers/all-MiniLM-L6-v2

Chunk Size: 1000 characters

Chunk Overlap: 200 characters

Similarity Search: Top 3 results

OpenAI Mode Settings

Model: gpt-3.5-turbo or gpt-4

Temperature: 0 (deterministic responses)

Max Tokens: Based on context

🧰 Troubleshooting
Common Issues

Module Not Found Errors

pip install --upgrade langchain-community


PDF Reading Issues

pip install --upgrade pypdf


Local Model Download Problems

Check internet connection for first-time download

Ensure sufficient disk space (~400MB for embeddings model)

OpenAI API Errors

Verify API key is set correctly

Check billing and usage limits

Ensure organization settings allow API access

⚡ Performance Tips

For large documents, increase chunk size to 1500–2000 characters

Use SSD storage for faster vector database operations

Close other memory-intensive applications when processing large files

For better local performance, consider using GPU with CUDA support

🔒 Privacy & Security
Local Mode

✅ All processing happens on your machine
✅ No data sent to external services
✅ Complete privacy and control

OpenAI Mode

⚠️ Document content sent to OpenAI servers
🔒 Follows OpenAI's data usage policies
📊 Refer to OpenAI’s privacy policy
 for details

🧾 License

This project is released under the MIT License.
Feel free to modify and use it for your own projects.
