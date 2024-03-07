import sys
import os
import json
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Append the parent directory of the backend directory to sys.path
project_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ""))
sys.path.append(project_dir_path)


# Load model parameters
def load_model_parameters(file_path):
    with open(file_path, "r") as f:
        model_parameters = json.load(f)
    return model_parameters


model_parameters_path = project_dir_path + "/config/model_parameters.json"
model_parameters = load_model_parameters(model_parameters_path)


def chatbot(model):
    """
    Function for Bedrock foundation model
    """
    llm = Bedrock(
        credentials_profile_name="default",
        model_id=model_parameters[model]["id"],
        model_kwargs=model_parameters[model]["kwargs"],
    )

    return llm


def memory(model):
    """
    Function for ConversationBufferMemory (llm and max token limits)
    """
    llm_data = chatbot(model=model)
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


def conversation(input_text, memory, model):
    """
    Function for Conversation Chain - input prompt + memory
    """
    llm_data = chatbot(model=model)
    llm_conversation = ConversationChain(llm=llm_data, memory=memory, verbose=False)

    response = llm_conversation.invoke(input=input_text)
    response = remove_self_conversation(response["response"])

    return response
