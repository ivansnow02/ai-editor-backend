from typing import Any, List, Optional
from urllib import response
from erniebot_agent.memory.messages import AIMessage
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from pydantic import Field
from erniebot_agent.chat_models import ERNIEBot
from erniebot_agent.memory import HumanMessage, SystemMessage, Message

MODEL = "ernie-speed"

async def complete(prompt) -> str:

    model = ERNIEBot(model=MODEL)

    messages: List[Message] = [
        HumanMessage(content=prompt),
    ]
    response: AIMessage = await model.chat(
        messages=messages,
        system=SystemMessage(
            content="你是一个专业的文本续写模型，你的任务是续写下面的文本。你必须提取出所有的要点并尽可能地按照原文的风格续写。"
        ).content
    )
    return response.content


async def abstract(prompt:str, word_count:int) -> str:

    model = ERNIEBot(model=MODEL)
    messages: List[Message] = [
        HumanMessage(content=prompt),
    ]
    response: AIMessage = await model.chat(
        messages=messages,
        system=SystemMessage(
            content=f"你是一个专业的文本摘要模型，你的任务是提取出所有的要点来摘要下面的文本。字数尽可能地限制为{str(word_count)}字。"
        ).content,
    )
    return response.content


async def translate(prompt:str, lang:str) -> str:
    
    model = ERNIEBot(model=MODEL)
    messages: List[Message] = [
        HumanMessage(content=prompt),
    ]
    response: AIMessage = await model.chat(
        messages=messages,
        system=SystemMessage(
            content=f"你是一个专业的文本翻译模型，你的任务是将下面的文本翻译成{lang}。"
        ).content,
    )
    return response.content    

async def polish(prompt:str,style:str) -> str:
    model = ERNIEBot(model=MODEL)
    messages: List[Message] = [
        HumanMessage(content=prompt),
    ]
    response: AIMessage = await model.chat(
        messages=messages,
        system=SystemMessage(
            content=f"你是一个专业的文本润色模型，你的任务是按照{style}风格修改文本。只需要输出修改后的文本。"
        ).content,
    )
    return response.content

async def fix(prompt:str) -> str:
    model = ERNIEBot(model=MODEL)
    messages: List[Message] = [
        HumanMessage(content=prompt),
    ]
    response: AIMessage = await model.chat(
        messages=messages,
        system=SystemMessage(
            content=f"你是一个专业的病句改写模型，你的任务是检查文本中的语病并修改，但尽量不要改变原有的意思。只需要输出修改后的文本。"
        ).content,
    )
    return response.content

# async def complete_stream(prompt):

#     model = ERNIEBot(model=MODEL)

#     messages: List[Message] = [
#         HumanMessage(content=prompt),
#     ]
#     ai_message = await model.chat(
#         messages=messages,
#         stream=True,
#         system=SystemMessage(
#             content="你是一个专业的文本续写模型，你的任务是续写下面的文本。你必须提取出所有的要点并尽可能地按照原文的风格续写。"
#         ).content
#     )
#     response = ""
#     async for chunk in ai_message:
#         response += chunk.content
#         yield response
