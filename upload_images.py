import os
from s3_client import s3_client as client


def upload_demo_images():
    """
    Uploads the images in the images_to_upload directory to the s3 bucket
    """

    bucket = "aicadium-demo"
    sub_dir = "./images_to_upload/"
    for file in os.listdir(sub_dir):
        file_path = f"images/{file}"
        client.upload_file(sub_dir + file, bucket, file_path)


if __name__ == "__main__":
    upload_demo_images()
