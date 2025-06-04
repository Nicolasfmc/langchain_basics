# -------------------------------
# | conversation_summary_memory |
# -------------------------------

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory

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
  "Any eco-friendly accommodation suggestions there?",
  "List 20 other cities with similar characteristics to what we've discussed. Rank them by how interesting they are, and include the one you already suggested.",
  "For the first city you mentioned earlier, give me 5 restaurants to visit. Respond with only the name of the city and the restaurant names."
]

memory = ConversationSummaryMemory(llm=llm)

conversation = ConversationChain(
  llm=llm, 
  verbose=True,
  memory=memory
)

for message in messages:
  response = conversation.predict(input=message)
  print(response)
