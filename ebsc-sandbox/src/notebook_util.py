import boto3
from dotenv import load_dotenv
import os

load_dotenv()

def setup_epa_s3_session():
    """Function that streamlines using assume role to return an s3_client
    for interacting with a shared bucket with the EPA

    Returns:
        boto3.session: s3 boto session for reading objects from EPA bucket
    """

    client = boto3.client("sts")
    assume_role_response = client.assume_role(
        RoleArn=os.environ["role_arn"],
        RoleSessionName="read-access-to-bucket",
    )
    sts_credentials = assume_role_response["Credentials"]

    boto3_session = boto3.Session(
        aws_access_key_id=sts_credentials["AccessKeyId"],
        aws_secret_access_key=sts_credentials["SecretAccessKey"],
        aws_session_token=sts_credentials["SessionToken"],
        region_name="us-east-1",
    )

    return boto3_session