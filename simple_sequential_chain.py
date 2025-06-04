# ------------------------------
# | simple_sequential_chain    |
# ------------------------------

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
  model="gpt-3.5-turbo",
  api_key=os.getenv("OPENAI_API_KEY"),
  temperature=0.7
)

prompt_city = ChatPromptTemplate.from_template(
  "Suggest a city based on my interest in {interest}"
)

prompt_restaurants = ChatPromptTemplate.from_template(
  "Suggest restaurants popular among locals in {city}"
)

prompt_cultural = ChatPromptTemplate.from_template(
  "Suggest cultural activities and places in {city}"
)

chain_city = LLMChain(prompt=prompt_city, llm=llm)
chain_restaurants = LLMChain(prompt=prompt_restaurants, llm=llm)
chain_cultural = LLMChain(prompt=prompt_cultural, llm=llm)

chain = SimpleSequentialChain(
  chains=[chain_city, chain_restaurants, chain_cultural],
  verbose=True
)

result = chain.invoke("Oscar Niemeyer Museum")
print(result)
