# --------------------
# | lcel_join_chains |
# --------------------

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from operator import itemgetter
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

prompt_cultural = ChatPromptTemplate.from_template(
  "Suggest cultural activities and places in {city}"
)

final_prompt = ChatPromptTemplate.from_messages([
  ("ai", "Travel suggestion for the city: {city}"),
  ("ai", "Restaurants you can't miss: {restaurants}"),
  ("ai", "Recommended cultural activities and places: {cultural_places}"),
  ("system", "Combine the above information into 2 coherent paragraphs")
])

step1 = prompt_city | llm | parser
step2 = prompt_restaurants | llm | StrOutputParser()
step3 = prompt_cultural | llm | StrOutputParser()
step4 = final_prompt | llm | StrOutputParser()

chain = (step1 | {
  "restaurants": step2,
  "cultural_places": step3,
  "city": itemgetter("city")
} | step4)

result = chain.invoke({"interest": "Oscar Niemeyer Museum"})
print(result)
