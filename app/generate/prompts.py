from langchain_core.prompts import ChatPromptTemplate


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
