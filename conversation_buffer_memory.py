# ----------------------------------------
# | conversation_buffer_memory           |
# ----------------------------------------

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(
  model="gpt-3.5-turbo",
  api_key=os.getenv("OPENAI_API_KEY"),
  temperature=0.7
)

messages = [
    "I want to visit a place in Brazil known for its cold weather and botanical park. Can you recommend one?",
    "What is the best time of year to visit in terms of weather?",
    "What kinds of outdoor activities are available?",
    "Any suggestions for eco-friendly accommodations there?",
    "List 20 other cities with similar characteristics to what we've described so far. Rank them by interest, including the one you already suggested.",
    "For the first city you suggested earlier, I want to know 5 restaurants to visit. Respond only with the city name and restaurant names.",
]

memory = ConversationBufferMemory()

conversation = ConversationChain(
  llm=llm, 
  verbose=True,
  memory=memory
)

for message in messages:
  response = conversation.predict(input=message)
  print(response)
