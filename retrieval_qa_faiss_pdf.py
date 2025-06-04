# ----------------------------
# | retrieval_qa_faiss_pdf  |
# ----------------------------

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA

load_dotenv()

llm = ChatOpenAI(
  model="gpt-3.5-turbo",
  api_key=os.getenv("OPENAI_API_KEY"),
  temperature=0.7
)

pdf_path = input("Enter the path to the PDF file: ")
loader = PyPDFLoader(pdf_path)
documents = loader.load()

splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = splitter.split_documents(documents)
print(texts)

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embeddings)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
)

question = "What does the accounts receivable department do?"
result = qa_chain.invoke({"query": question})

print(result)
