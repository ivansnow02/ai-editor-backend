import base64
from typing import List

import magic
from fastapi import APIRouter
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders.parsers.generic import MimeTypeBasedParser
from langchain_community.document_loaders.parsers.html import BS4HTMLParser
from langchain_community.document_loaders.parsers.msword import MsWordParser
from langchain_community.document_loaders.parsers.pdf import PDFMinerParser
from langchain_community.document_loaders.parsers.txt import TextParser
from langchain_core.document_loaders import Blob
from langchain_core.documents.base import Document
from langchain_core.pydantic_v1 import Field
from langchain_core.runnables.base import RunnableLambda
from langserve import CustomUserType, add_routes

from app.utils.llm import (
    ChatModel,
    LlmModel,
    abstract_prompt,
    completion_prompt,
    fix_prompt,
    polish_prompt,
    refine_prompt,
    summary_prompt,
    translate_prompt,
)

# async def _response_formatter_streaming(input_stream):
#     async for msg in input_stream:
#         c = ""
#         c += msg.content
#         content = re.sub(
#             r"```(.*?)\n(.*?)```", r"<pre><code lang=\1>\2</code></pre>", c
#         )
#         yield content


model = LlmModel()
cmodel = ChatModel()

router = APIRouter(
    prefix="/api/langserve",
    tags=["langserve"],
    responses={404: {"description": "Not found"}},
)

completion_chain = completion_prompt | cmodel

add_routes(
    app=router,
    runnable=completion_chain,
    path="/completion",
    enabled_endpoints=["invoke", "stream", "playground", "stream_log"],
)

fix_chain = fix_prompt | cmodel

add_routes(
    app=router,
    runnable=fix_chain,
    path="/fix",
    enabled_endpoints=["invoke", "stream", "playground", "stream_log"],
)

polish_prompt = polish_prompt | cmodel

add_routes(
    app=router,
    runnable=polish_prompt,
    path="/polish",
    enabled_endpoints=["invoke", "stream", "playground", "stream_log"],
)

translate_chain = translate_prompt | cmodel

add_routes(
    app=router,
    runnable=translate_chain,
    path="/translate",
    enabled_endpoints=["invoke", "stream", "playground", "stream_log"],
)

abstract_chain = abstract_prompt | cmodel

add_routes(
    app=router,
    runnable=abstract_chain,
    path="/abstract",
    enabled_endpoints=["invoke", "stream", "playground", "stream_log"],
)

# Configure the parsers that you want to use per mime-type!
HANDLERS = {
    "application/pdf": PDFMinerParser(),
    "text/plain": TextParser(),
    "text/html": BS4HTMLParser(),
    "application/msword": MsWordParser(),
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": MsWordParser(),
}

MIMETYPE_BASED_PARSER = MimeTypeBasedParser(
    handlers=HANDLERS,
    fallback_parser=None,
)

mime = magic.Magic(mime=True)

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=4000, chunk_overlap=0
)

summary_chain = load_summarize_chain(
    llm=model,
    chain_type="refine",
    question_prompt=summary_prompt,
    refine_prompt=refine_prompt,
    return_intermediate_steps=True,
    input_key="human_input",
    output_key="output_text",
)


class SummaryRequest(CustomUserType):
    """长文本、文件"""

    files: str = Field(..., extra={"widget": {"type": "base64file"}})


def _process_request(request: SummaryRequest) -> List[Document]:
    c = base64.b64decode(request.files.encode("UTF-8"))
    mime_type = mime.from_buffer(c)
    blob = Blob.from_data(data=c, mime_type=mime_type)
    parser = HANDLERS[mime_type]
    docs = list(parser.lazy_parse(blob))
    split_docs = text_splitter.split_documents(docs)
    return split_docs


summary_runnable = (
    RunnableLambda(_process_request).with_types(input_type=SummaryRequest)
    | summary_chain
)

add_routes(
    app=router,
    runnable=summary_runnable,
    config_keys=["configurable"],
    path="/file_summary",
    enabled_endpoints=["invoke", "stream", "playground", "stream_log"],
)
