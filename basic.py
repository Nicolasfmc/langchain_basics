# -----------------
# | Basic Example |
# -----------------

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

number_of_days = 7
number_of_children = 2
activity = "beach"

template = PromptTemplate.from_template(
  "Create a {number_of_days}-day travel itinerary for a family with {number_of_children} children who enjoy {activity}."
)

prompt = template.format(
  number_of_days=number_of_days,
  number_of_children=number_of_children,
  activity=activity
)

llm = ChatOpenAI(
  model="gpt-3.5-turbo",
  api_key=os.getenv("OPENAI_API_KEY"),
  temperature=0.7
)

response = llm.invoke(prompt)

print(response.content)
