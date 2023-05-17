from aws_cdk import Stack, aws_s3 as s3, App, aws_iam as iam

# app resources
data_sharing_bucket_name = "mtsu-cornell-data-sharing-bucket"
bird_sound_data_bucket_name = "mtsu-bird-sound-data-bucket"


class MtsuDsiBucket(Stack):
    def __init__(self, app: App, id: str) -> None:
        super().__init__(app, id)

        internal_bucket = s3.Bucket(  # noqa: F841
            self,
            bird_sound_data_bucket_name,
            bucket_name=bird_sound_data_bucket_name,
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )


class DataSharingBucket(Stack):
    def __init__(self, app: App, id: str) -> None:
        super().__init__(app, id)

        data_sharing_bucket = s3.Bucket(
            self,
            data_sharing_bucket_name,
            bucket_name=data_sharing_bucket_name,
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )

        self.my_bucket = data_sharing_bucket


class CollaborationUser(Stack):
    def __init__(self, app: App, id: str, user_bucket) -> None:
        super().__init__(app, id)

        user = iam.User(self, "collaboration-user")
        user_bucket.grant_read_write(user)
