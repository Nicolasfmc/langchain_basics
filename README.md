# LangChain Basics

A collection of simple, practical examples demonstrating basic LangChain methods, functions, and concepts. This repository serves as a learning resource for developers getting started with LangChain.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setting Up Your Environment

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/langchain_basics.git
   cd langchain_basics
   ```

2. **Create a virtual environment:**

   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and add your API keys:

   ```txt
   OPENAI_API_KEY=your_openai_api_key_here
   # Add other API keys as needed
   ```

## 📚 Examples (Ordered by Complexity)

### Beginner Level

1. **[Basic](./basic.py)** - Introduction to basics
2. **[Simple Sequential Chain](./simple_sequential_chain.py)** - Basic sequential chain implementation

### Intermediate Level

3. **[Conversation Buffer Memory](./conversation_buffer_memory.py)** - Basic memory management for conversations
4. **[Conversation Buffer Window Memory](./conversation_buffer_window_memory.py)** - Windowed memory for chat history
5. **[Conversation Summary Memory](./conversation_summary_memory.py)** - Summarized conversation memory
6. **[LCEL Basic](./lcel_basic.py)** - The basic of LangChain Expression Language (LCEL)
7. **[LCEL Join Chains](./lcel_join_chains.py)** - LangChain Expression Language (LCEL) + Join chains
8. **[Conversation Buffer Custom Chain](./conversation_buffer_custom_chain.py)** - Custom chain with buffer memory
9. **[JSON Output Parser](./json_output_parser.py)** - Parsing structured JSON outputs
10. **[Retrieval QA Tasks](./retrieval_qa_tasks.pdf.py)** - Document retrieval and Q&A
11. **[Retrieval QA](./retrieval_qa.py)** - Intermediate retrieval-based question answering

## 🛠️ What You'll Learn

- **Basic LangChain Setup**: Environment configuration and basic usage
- **Memory Management**: Different types of conversation memory (buffer, window, summary)
- **Chain Operations**: Sequential chains and custom chain implementations
- **Output Parsing**: Structured data extraction and JSON parsing
- **Retrieval Systems**: Document-based question answering and retrieval-augmented generation (RAG)
- **Advanced Patterns**: Custom chains and complex workflow implementations

## 📖 Usage

Each Python file in this repository is a standalone example. To run any example:

```bash
python filename.py
```

For example:

```bash
python simple_sequential_chain.py
```

## 🔧 Virtual Environment Management

### Why Use Virtual Environments?

Virtual environments help you:

- Keep project dependencies isolated
- Avoid conflicts between different projects
- Maintain consistent development environments
- Easy dependency management

### Managing Your Virtual Environment

**Activate the environment** (do this every time you work on the project):

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

**Deactivate when done:**

```bash
deactivate
```

**Update requirements.txt** when you add new packages:

```bash
pip freeze > requirements.txt
```

## 📦 Dependencies

The `requirements.txt` file contains all necessary dependencies. Key packages include:

- `langchain` - Core LangChain library
- `openai` - OpenAI API integration
- `python-dotenv` - Environment variable management
- Additional utilities for specific examples

## 🤝 Contributing

Feel free to contribute by:

1. Adding new examples
2. Improving existing code
3. Adding documentation
4. Reporting issues

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Troubleshooting

**Common Issues:**

1. **Import errors**: Make sure your virtual environment is activated and dependencies are installed
2. **API key errors**: Verify your `.env` file is properly configured
3. **Module not found**: Check that you're running commands from the project root directory

**Getting Help:**

- Check the official [LangChain documentation](https://docs.langchain.com/)
- Review individual file comments for specific usage instructions
- Open an issue in this repository for bug reports or questions

---

Happy coding! 🚀
