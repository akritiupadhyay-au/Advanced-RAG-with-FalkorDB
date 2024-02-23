# Advanced RAG with FalkorDB
Knowledge Graphs has changed the way RAG applications are getting built. Since RAG mitigates knowledge limitations like hallucinations and knowledge cut-offs, we use RAG to build QA chatbots. Knowledge Graphs store and query the original data and capture different entities and relations embedded in one’s data.

**FalkorDB** is a high-performance Graph Database designed for applications prioritizing fast response times and refusing to compromise on data modeling. It succeeds RedisGraph and is recognized for its exceptionally low latency. Users trust FalkorDB for its uncompromising performance. It can be easily run using Docker.

Use this command to install Falkor DB using docker: `docker run -p 6379:6379 -p 7687:7687 falkordb/falkordb`

With the help of a Falkor DB Knowledge Graph, I have built an advanced RAG application using the Diffbot API and the OpenAI base model.

## Steps to Follow:
1. Clone this [repository](https://github.com/akritiupadhyay-au/Advanced-RAG-with-FalkorDB) using this command: `git clone https://github.com/akritiupadhyay-au/Advanced-RAG-with-FalkorDB.git`
2. Change the directory: `cd Advanced-RAG-with-FalkorDB`
3. Install the [requirements](requirements.txt): `pip install -r requirements.txt`
4. Edit the [environment file](.env) with your API keys.
5. Run the [app.py](app.py) in your terminal: `python app.py run`

You'll see the results. You can change the Wikipedia Query while loading using LangChain framework. Also, you can try different queries related to the loaded Wikipedia Query in the Chain.

To know more in details, visit my medium [article](https://medium.com/@akriti.upadhyay/building-advanced-rag-applications-using-falkordb-langchain-diffbot-api-and-openai-083fa1b6a96c)
