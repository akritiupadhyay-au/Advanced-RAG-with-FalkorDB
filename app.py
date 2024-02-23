import os
from dotenv import load_dotenv
load_dotenv()

from langchain_experimental.graph_transformers.diffbot import DiffbotGraphTransformer
diffbot_api_key = "DIFFBOT_API_KEY"
diffbot_nlp = DiffbotGraphTransformer(diffbot_api_key=diffbot_api_key)

from langchain.document_loaders import WikipediaLoader
query = "Washington"
raw_documents = WikipediaLoader(query=query).load()
graph_documents = diffbot_nlp.convert_to_graph_documents(raw_documents)

from langchain.graphs import FalkorDBGraph
graph = FalkorDBGraph("falkordb")
graph.add_graph_documents(graph_documents)
graph.refresh_schema()

from langchain_openai import ChatOpenAI
from langchain.chains import FalkorDBQAChain
chain = FalkorDBQAChain.from_llm(ChatOpenAI(temperature=0), graph=graph, verbose=True)

chain.run("Which university is in Washington")
