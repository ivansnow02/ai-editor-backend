from erniebot_agent.extensions.langchain.llms import ErnieBot
import re
from typing import Any, Callable, Dict

from fastapi import HTTPException, Request
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import ConfigurableFieldSpec
from langchain_core.runnables.history import RunnableWithMessageHistory
from typing_extensions import TypedDict
from fastapi import APIRouter



from langserve import add_routes

from ..generate.llm import ChatModel


def _is_valid_identifier(value: str) -> bool:
    """
    判断给定的字符串是否是一个有效的标识符。

    Args:
        value (str): 要检查的字符串。

    Returns:
        bool: 如果字符串是有效的标识符，则返回True；否则返回False。
    """
    valid_characters = re.compile(r"^[a-zA-Z0-9-_]+$")
    return bool(valid_characters.match(value))


def create_session_factory() -> Callable[[str, str], BaseChatMessageHistory]:
    """
    创建一个会话工厂，返回一个用于获取聊天历史记录的函数。

    Returns:
        一个可调用对象，接受两个参数（user_id 和 conversation_id），并返回聊天历史记录。
    """
    def get_chat_history(user_id: str, conversation_id: str) -> RedisChatMessageHistory:
        if not _is_valid_identifier(user_id):
            raise ValueError(
                f"用户ID {user_id} 不符合有效格式。"
            )
        if not _is_valid_identifier(conversation_id):
            raise ValueError(
                f"对话ID {conversation_id} 不符合有效格式。"
            )

        history = RedisChatMessageHistory(session_id=f"{conversation_id}")
        return history

    return get_chat_history


router = APIRouter(
    prefix="/api/langserve",
    tags=["dev"],
    responses={404: {"description": "Not found"}},
)


def _per_request_config_modifier(
    config: Dict[str, Any], request: Request
) -> Dict[str, Any]:
    """
    修改每个请求的配置。

    Args:
        config (Dict[str, Any]): 原始配置字典。
        request (Request): 请求对象。

    Returns:
        Dict[str, Any]: 修改后的配置字典。
    """
    config = config.copy()
    configurable = config.get("configurable", {})
    user_id: str | None = request.cookies.get("user_id", None)

    if user_id is None:
        raise HTTPException(
            status_code=400,
            detail="请设置cookie：'user_id'.",
        )
    configurable["user_id"] = user_id
    config["configurable"] = configurable
    return config


prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages(
    messages=[
        ("system", "你是一个专业的文本编辑器助手，你的任务是帮助用户编辑文本。"),
        MessagesPlaceholder(variable_name="history"),
        ("user", "{human_input}"),
    ]
)

chain = prompt | ChatModel()


class InputChat(TypedDict):
    human_input: str


chain_with_history = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=create_session_factory(),
    input_messages_key="human_input",
    history_messages_key="history",
    history_factory_config=[
        ConfigurableFieldSpec(
            id="user_id",
            annotation=str,
            name="User ID",
            description="用户的身份ID",
            default="",
            is_shared=True,
        ),
        ConfigurableFieldSpec(
            id="conversation_id",
            annotation=str,
            name="Conversation ID",
            description="对话的ID",
            default="",
            is_shared=True,
        ),
    ],
).with_types(input_type=InputChat)


add_routes(
    router,
    chain_with_history,
    path="/chat_with_history",
    per_req_config_modifier=_per_request_config_modifier,
    enabled_endpoints=["invoke", "stream", "stream_log"],
)
