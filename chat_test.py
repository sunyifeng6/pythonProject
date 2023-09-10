import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import docx
def getText(fileName):
    doc = docx.Document(fileName)
    TextList = []
    for paragraph in doc.paragraphs:
        TextList.append(paragraph.text)
    return '\n'.join(TextList)
os.environ["OPENAI_API_KEY"] = "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"
chat = ChatOpenAI(temperature=0,model="gpt-3.5-turbo")
template = "请你从以下文本中利用{input_project}，每个文档格式必须要与原文档格式保持一致，每个文档的标题数需与原文本保持一致，每个文档都不能遗漏原文的信息:"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
# text = "六、扶持措施\n（一）创新创业团队以及创新创业人才以现场考察、组织专家评审、择优遴选方式产生，在年度资助项目数内对入选创新创业团队给予200万元资助，入选创新人才、创业人才给予80万元一次性生活补贴。\n（二）项目实施期限为3年。\n（三）项目资金按市方案确定的分担形式安排，即由市级财政与申请资助企业注册地所在县（市、区）财政按比例分担，其中：市本级财政与云城区分担比例为7:3，与云安区、罗定市、新兴县、郁南县、云浮新区、佛山（云浮）产业转移工业园区分担比例为3:7。市财政分担部分，由市科技局按规定程序向市政府申请专项资金。县（市、区）财政分担部分，由各县（市、区）项目审核职能部门按规定向县（市、区）政府申请资金。")
text = getText("零散-25350/二、专题类别.docx")
# get a chat completion from the formatted messages
ans = chat(chat_prompt.format_prompt(input_project="创新创业团队、创新人才、创业人才三个项目对应生成三个文档",
                               text=text).to_messages()).content
# ans = chat(chat_prompt.format_prompt(input_project="创新创业团队、创新人才、创业人才三个项目对应生成三个文档",
#                                  text="七、监督管理\n（一）项目承担单位需在每年12月底向属地科技主管部门提交项目当年的工作总结报告，由各地县级科技部门汇总当地总结报告报市科技局，市科技局将采取查核书面材料与实地考察等方式进行年度考核。考核不及格的需整改落实。\n（二）各县（市、区）科技部门须加强监督管理，市科技局将对创新创业团队以及创新创业人才工作情况、资金使用情况进行不定期监督检查，并接受社会监督。\n（三）云浮市创新创业团队以及创新创业人才资助资金必须按规定用途使用，严禁虚报、冒领、贪污、截留、挤占、挪用、套取财政资金等行为。对弄虚作假、骗取财政资金的单位和个人，将不予发放或追回已发放的财政资金，通报有关部门，并将其列入严重失信记录名单实施联合惩戒，5年内不再受理其申请相关财政补贴，情节严重的，依法追究其法律责任。").to_messages()).content
print(ans)
# -> AIMessage(content="J'aime programmer.", additional_kwargs={})