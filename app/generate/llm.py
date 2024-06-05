from langchain_community.llms import Ollama
from erniebot_agent.extensions.langchain.llms import ErnieBot


def LlmModel(model:str="ernie-speed"):
    if model == "qwen:7b":
        return Ollama(
            model=model,
        )
    elif model == "ernie-speed":
        return ErnieBot(model=model)
    else:
        raise ValueError("Model not found")
