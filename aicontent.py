import openai
import config
import os
from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper,ServiceContext
from langchain import OpenAI
os.environ['OPENAI_API_KEY'] = "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"
index=GPTSimpleVectorIndex.load_from_disk("./model/index.json")
def ask(question):
    reponse=index.query(question)
    return reponse.response