import openai
import config
from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper,ServiceContext
from langchain import OpenAI
index=GPTSimpleVectorIndex.load_from_disk("./model/index.json")
def ask(question):
    reponse=index.query(question)
    print(reponse.response)