from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
import json, random

load_dotenv()

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Continue the conversation based on the context provided."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

def query_llm(chat_history, question):
    return chain.invoke({ "chat_history": chat_history, "input": question })

def respond_to_prompt (id, question):
    with open('conversational_history.json', 'r') as file:
        data = json.load(file)

    try:
        newHistory = data[str(id)]   
    except KeyError:
        print("Hello Testing this error")
        newHistory = []

    AI_answer = query_llm(newHistory, question)

    newHistory.append(f'User: {question}')
    newHistory.append(f'AI: {AI_answer}')

    data[str(id)] = newHistory

    with open('conversational_history.json', 'w') as file:
        json.dump(data, file, indent=4)
    return AI_answer
# respond_to_prompt(1234123412341234,[],'I want to eat something sweet.')