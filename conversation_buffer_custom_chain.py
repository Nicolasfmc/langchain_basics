# ------------------------------------
# | conversation_buffer_custom_chain |
# ------------------------------------

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import ConversationChain
from langchain_core.memory import ConversationBufferMemory

load_dotenv()

llm = ChatOpenAI(
  model="gpt-3.5-turbo",
  api_key=os.getenv("OPENAI_API_KEY"),
  temperature=0.7
)

messages = [
    "I want to visit a place in Brazil known for its beaches and culture. Can you recommend one?",
    "What is the best time of year to visit in terms of weather?",
    "What kinds of outdoor activities are available?",
    "Any eco-friendly accommodation suggestions there?",
    "List 20 other cities with similar characteristics to what we've discussed. Rank them by how interesting they are, and include the one you already suggested.",
    "For the first city you mentioned earlier, give me 5 restaurants to visit. Respond with only the name of the city and the restaurant names.",
]

memory = ConversationBufferMemory()

conversation = ConversationChain(
  llm=llm,
  verbose=True,
  memory=memory
)

long_conversation = ""

for message in messages:
  long_conversation += f"User: {message}\n"
  long_conversation += "AI: "

  prompt = PromptTemplate(template=long_conversation, input_variables=[""])
  chain = prompt | llm | StrOutputParser()
  response = chain.invoke(input={})

  long_conversation += f"{response}\n"

  print(long_conversation)
