from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser


async def generate(request) -> str:

    model = Ollama(model="qwen:7b")
    p = request.json.get("prompt").strip()
    messages = [
        SystemMessage(
            content="你是一个专业的文本补全模型，你的任务是补全下面的文本。"
        ),
        HumanMessage(content=p),
    ]
    parser = StrOutputParser()
    result = await model.ainvoke(messages)
    response = await parser.ainvoke(result)
    return response