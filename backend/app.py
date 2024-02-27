import os
import dotenv
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

dotenv.load_dotenv()


def chatbot():
    """
    Function for Bedrock foundation model
    """
    llm = Bedrock(
        credentials_profile_name="default",
        model_id="meta.llama2-70b-chat-v1",
        model_kwargs={"temperature": 0.5, "top_p": 0.9, "max_gen_len": 512},
    )

    return llm


def memory():
    """
    Function for ConversationBufferMemory (llm and max token limits)
    """
    llm_data = chatbot()
    memory = ConversationBufferMemory(
        llm=llm_data,
        max_token_limit=512,
    )

    return memory


def remove_self_conversation(response):
    index = response.find("\nHuman:")
    if index != -1:
        return response[:index]
    return response


def format_input_text(input_text):

    return f"{input_text}\nDo not include any self reflection or conversations that was not provided."


def conversation(input_text, memory):
    """
    Function for Conversation Chain - input prompt + memory
    """
    llm_data = chatbot()
    llm_conversation = ConversationChain(llm=llm_data, memory=memory, verbose=False)

    input_text = format_input_text(input_text)
    response = llm_conversation.invoke(input=input_text)
    chat_reply = remove_self_conversation(response["response"])

    return chat_reply
