from typing import List
from fastapi import APIRouter
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import re
import json
from langchain_core.messages import AIMessage
from ..generate.llm import ChatModel


schema = """
{
    "正文字体": "''''''",
    "正文字体大小": "''''''",
    "标题1": {
        "字体": "''''''",
        "字体大小": "''''''",
    },
    "标题2": {
        "字体": "''''''",
        "字体大小": "''''''",
    },
    "标题3": {
        "字体": "''''''",
        "字体大小": "''''''",
    },
}"""

prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages(
    messages=[
        (
            "system",
            "回答用户查询。将您的答案输出为 JSON"
            "匹配给定的格式：\n```json\n{schema}\n```\n"
            "确保将答案包装在 ```json 和 ``` 标签中"
            "填入指定内容在''''''中，不允许出现注释，不允许出现解释性文字，若提供信息具体对应值无法准确判断，直接原样填入，不需要你来解释和更改",
        ),
        ("user", "{query}"),
    ]
).partial(schema=schema)


def extract_json(message: AIMessage) -> List[dict]:
    text = str(message.content)
    pattern = r"```json(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    try:
        return [json.loads(match.strip()) for match in matches]
    except Exception as e:
        raise ValueError(f"{e} Failed to parse: {message}")


chain = prompt | ChatModel() | extract_json


router = APIRouter(
    prefix="/api/langserve",
    tags=["langserve"],
    responses={404: {"description": "Not found"}},
)


add_routes(
    app=router,
    runnable=chain,
    path="/format",
    enabled_endpoints=["invoke", "stream", "playground", "stream_log"],
)
