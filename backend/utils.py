import os
import boto3


def get_aws_credentials():
    """
    This function reads a secure parameter from AWS' SSM service.
    The request must be passed a valid parameter name, as well as
    temporary credentials which can be used to access the parameter.
    The parameter's value is returned.
    """
    try:
        # Extract credentials from AWS SSM (for cloud deployment)
        ssm = boto3.client("ssm", region_name="us-east-1")

        AWS_REGION = ssm.get_parameter(Name="DEFAULT_REGION", WithDecryption=True)["Parameter"]["Value"]
        AWS_ACCESS_KEY = ssm.get_parameter(Name="ACCESS_KEY_ID", WithDecryption=True)["Parameter"]["Value"]
        AWS_SECRET_ACCESS_KEY = ssm.get_parameter(Name="SECRET_ACCESS_KEY", WithDecryption=True)["Parameter"]["Value"]

    except:
        # Extract credentials from environment variables (for local deployment)
        AWS_REGION = os.environ["AWS_DEFAULT_REGION"]
        AWS_ACCESS_KEY = os.environ["AWS_ACCESS_KEY_ID"]
        AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]

    return AWS_REGION, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY
