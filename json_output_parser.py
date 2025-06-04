# ----------------------
# | json_output_parser |
# ----------------------

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

class Destination(BaseModel):
  city = Field("city to visit")
  reason = Field("reason why it is interesting to visit the city")

llm = ChatOpenAI(
  model="gpt-3.5-turbo",
  api_key=os.getenv("OPENAI_API_KEY"),
  temperature=0.7
)

parser = JsonOutputParser(pydantic_object=Destination)

prompt_city = PromptTemplate(
  template="""Suggest a city based on my interest in {interest}
  {output_format}
  """,
  input_variables=["interest"],
  partial_variables={"output_format": parser.get_format_instructions()},
)

prompt_restaurants = PromptTemplate.from_template(
  "Suggest restaurants popular among locals in {city}"
)

prompt_cultural = PromptTemplate.from_template(
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
