from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI, Request
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
from erniebot_agent.extensions.langchain.llms import ErnieBot
from pydantic import BaseModel
from app.generate.prompts import (
    abstract_prompt,
    completion_prompt,
    fix_prompt,
    polish_prompt,
    translate_prompt,
)

router = APIRouter(
    prefix="/api/langserve",
    tags=["langserve"],
    responses={404: {"description": "Not found"}},
)


from langserve import APIHandler
completion_chain = completion_prompt | ErnieBot(model="ernie-speed")


add_routes(
    app=router,
    runnable=completion_chain,
    path="/completion",
    enabled_endpoints=["invoke", "stream"],
)

abstract_chain = abstract_prompt | ErnieBot(model="ernie-speed")

add_routes(
    app=router,
    runnable=abstract_chain,
    path="/abstract",
    enabled_endpoints=["invoke", "stream"],
)


fix_chain = fix_prompt | ErnieBot(model="ernie-speed")

add_routes(
    app=router,
    runnable=fix_chain,
    path="/fix",
    enabled_endpoints=["invoke", "stream"],
)

polish_prompt = polish_prompt | ErnieBot(model="ernie-speed")

add_routes(
    app=router,
    runnable=polish_prompt,
    path="/polish",
    enabled_endpoints=["invoke", "stream"],
)

translate_chain = translate_prompt | ErnieBot(model="ernie-speed")

add_routes(
    app=router,
    runnable=translate_chain,
    path="/translate",
    enabled_endpoints=["invoke", "stream"],
)
