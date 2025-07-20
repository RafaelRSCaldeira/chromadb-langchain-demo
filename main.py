from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import chromadb

load_dotenv()


# ingest pdf document
loader = PyPDFLoader("./assets/document.pdf")

# splits document in chunks
docs = loader.load_and_split()

# initialize llm model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# initialize embedding model
embeddings = OpenAIEmbeddings()

# initialize chroma client
chroma_client = chromadb.Client()

# create collection
collection = chroma_client.create_collection(name="demo_collection")

# add document in collection
collection.add(
    ids=["id1"],
    documents=[
        docs
    ]
)

# querying document
results = collection.query(
    query_texts=["What is Lorem Ipsum about?"], # Chroma will embed this for you
    n_results=1 # how many results to return
)

print(results)