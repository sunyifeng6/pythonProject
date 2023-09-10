import openai
from langchain.prompts import PromptTemplate
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import os
os.environ["OPENAI_API_KEY"] = "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"

#os.environ["OPENAI_API_KEY"] = "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"
#openai.api_key = "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"
model_engine = "gpt-3.5-turbo-16k-0613"

chat = ChatOpenAI(temperature=0)

sys_prompt = PromptTemplate(
    input_variables=["entity","text"],
    template="请你根据{entity}这几个对象进行拆分成多个对应的文档，不能生成文档里没有的内容，并且要保障文档内容的完整性:{text}")

sys_prompt.format_prompt(entity="123",text="123")
chain = LLMChain(llm=chat,prompt=sys_prompt)
print(chain.run(entity="123",text="123"))