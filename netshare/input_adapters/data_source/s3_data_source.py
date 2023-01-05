import os
import tempfile

from netshare.configs import get_config
from netshare.input_adapters.data_source import DataSource


class S3DataSource(DataSource):
    """
    This plugin gets an S3 bucket, and recursively find and downloads all the files in it.
    Subdirectories are being flattened, and the filenames are change to be unique.

    The config should contain the following:
    * bucket_name: The name of the bucket to download from.
    """

    def fetch_data(self) -> str:
        # We import boto3 here, because it is a requirement only if you use s3 as a data source.
        import boto3

        target_dir = tempfile.mkdtemp()

        s3_bucket = boto3.resource("s3").Bucket(get_config("bucket_name"))
        for s3_object in s3_bucket.objects.all():
            path, filename = os.path.split(s3_object.key)
            unique_filename = os.path.join(path, filename).replace("/", "_")
            s3_bucket.download_file(
                s3_object.key, os.path.join(target_dir, unique_filename)
            )
        return target_dir
