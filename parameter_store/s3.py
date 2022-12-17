from .iparameter_store import IParameterStore

import boto3
from botocore.exceptions import ClientError


class S3(IParameterStore):
    def __init__(self, bucket: str):
        self.store = boto3.client("s3")
        self.bucket = bucket

    def put(
        self, path: str, value: str, field_type: str = "String", overwrite: bool = True
    ) -> dict:
        try:
            return self.store.put_object(
                Body=value.encode("ascii"), Bucket=self.bucket, Key=path
            )

        except ClientError as e:
            raise

    def get(self, path: str, with_decryption: bool = True) -> dict:
        try:
            data = self.store.get_object(Bucket=self.bucket, Key=path)
            contents = data["Body"].read()
            return contents.decode("utf-8")

            # return self.store.download_file
        except ClientError as e:
            if e.response["Error"]["Code"] == "ParameterNotFound":
                return "[]"
            raise
