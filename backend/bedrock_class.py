import sys
import os
import boto3
import dotenv

dotenv.load_dotenv()

project_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ""))
sys.path.append(project_dir_path)

from backend.utils import get_aws_credentials


class BedrockClass:

    @staticmethod
    def get_bedrock_client():
        """
        This function will return the bedrock client.
        """
        AWS_REGION, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY = get_aws_credentials()

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
        AWS_REGION, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY = get_aws_credentials()

        bedrock_runtime_client = boto3.client(
            "bedrock-runtime",
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

        return bedrock_runtime_client
