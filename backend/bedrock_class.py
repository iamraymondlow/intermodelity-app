import os
import boto3
import dotenv

dotenv.load_dotenv()


def getParameter():
    """
    This function reads a secure parameter from AWS' SSM service.
    The request must be passed a valid parameter name, as well as
    temporary credentials which can be used to access the parameter.
    The parameter's value is returned.
    """
    # Create the SSM Client
    ssm = boto3.client("ssm", os.environ["AWS_DEFAULT_REGION"])

    # Get the requested parameter
    AWS_REGION = ssm.get_parameter(Name="DEFAULT_REGION", WithDecryption=True)["Parameter"]["Value"]
    AWS_ACCESS_KEY = ssm.get_parameter(Name="ACCESS_KEY_ID", WithDecryption=True)["Parameter"]["Value"]
    AWS_SECRET_ACCESS_KEY = ssm.get_parameter(Name="SECRET_ACCESS_KEY", WithDecryption=True)["Parameter"]["Value"]

    return AWS_REGION, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY


try:
    AWS_REGION, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY = getParameter()
except:
    AWS_REGION = os.environ["AWS_DEFAULT_REGION"]
    AWS_ACCESS_KEY = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]


class BedrockClass:

    @staticmethod
    def get_bedrock_client():
        """
        This function will return the bedrock client.
        """
        bedrock_client = boto3.client(
            "bedrock",
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

        return bedrock_client

    @staticmethod
    def get_bedrock_runtime_client():
        """
        This function will return the bedrock runtime client.
        """
        bedrock_runtime_client = boto3.client(
            "bedrock-runtime",
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

        return bedrock_runtime_client
