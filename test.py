from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate
)


import os
os.environ["OPENAI_API_KEY"] = "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"

model_engine = "gpt-3.5-turbo-0301"
hun_template = "{text}"
sys_template = "请你根据{entity}这几个对象进行拆分成多个对应的文档，不能生成文档里没有的内容，并且要保障文档内容的完整性"

example = [
    {
        "question" : """
        二、专题类别
本批次高层次科技创新创业人才项目分为3个专题申报：创新创业团队、创新人才和创业人才。
（一）申报单位可根据自身条件、人才实际情况自行选择申报创新创业团队、创新人才和创业人
才。
（二）申报单位只能选择申报创新创业团队、创新人才、创业人才中的一项。
（三）申报单位要慎重填写申报书的内容，如获批立项，申报书中的有关内容（如人员、配套资
金、经济指标、技术指标等）不能变更，要求与项目合同书内容一致。
（四）对符合《产业人才计划实施方案（试行）》的特殊引进对象可实行“一事一议”。""",
        "answer": """
        1.创新创业团队:
        二、专题类别
本批次高层次科技创新创业人才项目分为3个专题申报：创新创业团队、创新人才和创业人才。
（一）申报单位可根据自身条件、人才实际情况自行选择申报创新创业团队、创新人才和创业人
才。
（二）申报单位只能选择申报创新创业团队、创新人才、创业人才中的一项。
（三）申报单位要慎重填写申报书的内容，如获批立项，申报书中的有关内容（如人员、配套资
金、经济指标、技术指标等）不能变更，要求与项目合同书内容一致。
（四）对符合《产业人才计划实施方案（试行）》的特殊引进对象可实行“一事一议“。
        2.创新人才：
        本批次高层次科技创新创业人才项目分为3个专题申报：创新创业团队、创新人才和创业人才。
（一）申报单位可根据自身条件、人才实际情况自行选择申报创新创业团队、创新人才和创业人
才。
（二）申报单位只能选择申报创新创业团队、创新人才、创业人才中的一项。
（三）申报单位要慎重填写申报书的内容，如获批立项，申报书中的有关内容（如人员、配套资
金、经济指标、技术指标等）不能变更，要求与项目合同书内容一致。
（四）对符合《产业人才计划实施方案（试行）》的特殊引进对象可实行“一事一议“。
        3.创业人才
        本批次高层次科技创新创业人才项目分为3个专题申报：创新创业团队、创新人才和创业人才。
（一）申报单位可根据自身条件、人才实际情况自行选择申报创新创业团队、创新人才和创业人
才。
（二）申报单位只能选择申报创新创业团队、创新人才、创业人才中的一项。
（三）申报单位要慎重填写申报书的内容，如获批立项，申报书中的有关内容（如人员、配套资
金、经济指标、技术指标等）不能变更，要求与项目合同书内容一致。
（四）对符合《产业人才计划实施方案（试行）》的特殊引进对象可实行“一事一议“。
        """
    }
]


hun_mes = HumanMessagePromptTemplate.from_template(hun_template)
sys_mes = SystemMessagePromptTemplate.from_template(sys_template)
#ai_mes = AIMessagePromptTemplate.from_template((ai_template))
#system_message_prompt = SystemMessagePromptTemplate.from_template(template)
chat_prompt = ChatPromptTemplate.from_messages([sys_mes,hun_mes])

llm = ChatOpenAI(temperature=0,model_name=model_engine)

chain = LLMChain(llm=llm,prompt=chat_prompt)


#print(llm.predict_messages(chat_prompt))
print(chain.run(entity="创新创业团队、创新人才、创业人才",text="""
二、专题类别
本批次高层次科技创新创业人才项目分为3个专题申报：创新创业团队、创新人才和创业人才。
（一）申报单位可根据自身条件、人才实际情况自行选择申报创新创业团队、创新人才和创业人
才。
（二）申报单位只能选择申报创新创业团队、创新人才、创业人才中的一项。
（三）申报单位要慎重填写申报书的内容，如获批立项，申报书中的有关内容（如人员、配套资
金、经济指标、技术指标等）不能变更，要求与项目合同书内容一致。
（四）对符合《产业人才计划实施方案（试行）》的特殊引进对象可实行“一事一议“。
"""))