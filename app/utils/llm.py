from erniebot_agent.extensions.langchain.chat_models import ErnieBotChat
from erniebot_agent.extensions.langchain.llms import ErnieBot
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate


def LlmModel(model: str = "ernie-speed"):
    return ErnieBot(model=model)


def ChatModel(model: str = "ernie-speed"):
    return ErnieBotChat(model=model)


completion_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个专业的文本续写模型，你的任务是续写下面的文本并在中填入。你必须提取出所有的要点并尽可能地按照原文的风格续写。",
        ),
        ("user", "{human_input}"),
    ]
)

abstract_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个专业的文本摘要模型，你的任务是提取出所有的要点来摘要下面的文本。字数尽可能地限制为{word_count}字",
        ),
        ("user", "{human_input}"),
    ]
)

translate_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个专业的文本翻译模型，你的任务是将下面的文本翻译成{lang}。",
        ),
        ("user", "{human_input}"),
    ]
)

polish_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个专业的文本润色模型，你的任务是按照{style}风格修改文本。只需要输出修改后的文本。",
        ),
        ("user", "{human_input}"),
    ]
)

fix_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个专业的病句改写模型，你的任务是检查文本中的语病并修改，但尽量不要改变原有的意思。只需要输出修改后的文本。",
        ),
        ("user", "{human_input}"),
    ]
)

refine_template = (
    "你的工作是编写最终摘要\n"
    "我们已经提供了一定程度的现有摘要：{existing_answer}\n"
    "我们有机会完善现有的总结"
    "（仅在需要时）下面有更多上下文。\n\n"
    "------------\n"
    "{text}\n"
    "------------\n"
    "鉴于新的背景，完善原始摘要"
    "如果上下文没有用，请返回原始摘要。"
)
refine_prompt = PromptTemplate.from_template(refine_template)

summary_template = """写出以下内容的简洁摘要：
{text}
简要总结"""
summary_prompt = PromptTemplate.from_template(summary_template)
