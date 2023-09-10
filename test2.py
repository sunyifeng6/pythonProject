from langchain.chat_models import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"


chat = ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo-0301")

print(chat.predict("你好"))
