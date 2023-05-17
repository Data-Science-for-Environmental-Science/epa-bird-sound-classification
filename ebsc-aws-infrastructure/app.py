from aws_cdk import App
from aws_buckets.collab_s3_bucket import (
    DataSharingBucket,
    CollaborationUser,
    MtsuDsiBucket,
)



app = App()

MtsuDsiBucket(app, "mtsu-dsi-bucket-stack")

bucket_producer = DataSharingBucket(app, "mtsu-cornell-data-sharing")
CollaborationUser(app, "collab-user-stack", user_bucket=bucket_producer.my_bucket)

app.synth()
