# --------------
# | lcel_basic |
# --------------

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

class Destination(BaseModel):
  city: str = Field(description="city to visit")
  reason: str = Field(description="reason why it's interesting to visit this city")

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

step1 = prompt_city | llm | parser
step2 = prompt_restaurants | llm | StrOutputParser()
step3 = prompt_cultural | llm | StrOutputParser()

chain = (step1 | {
  "restaurantes": step2,
  "locais_culturais": step3
})

result = chain.invoke({"interest": "Oscar Niemeyer Museum"})
print(result)
