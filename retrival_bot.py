from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langchain.agents import create_openai_functions_agent, AgentExecutor

load_dotenv()

embeddings = OpenAIEmbeddings()
search = TavilySearchResults()
prompt = hub.pull("hwchase17/openai-functions-agent")
llm = ChatOpenAI()

def start_reterival(sources, chat_history, question):

    loader = WebBaseLoader(sources)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings)
    retriever = vector.as_retriever()


    retriever_tool = create_retriever_tool(
        retriever,
        "rag_search",
        "Search for information about provided web source. For any questions about said resource, you must use this tool!",
    )
    tools = [retriever_tool, search]

    
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor.invoke({
        "chat_history": chat_history,
        "input": question
    })['output']


