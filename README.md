
# Aicadium practical question


#### Prompt:
Given a presigned aws s3 url, get an image from an s3 bucket.
Get height and width of image and save to db.
Returns the image as grayscale (assume the image is in rgb).
Could be called multiple times, possibly with same image.

#### Steps taken:
1. Created a new s3 bucket and uploaded an image to it.
    - Created a new s3 bucket named `aicadium-demo`
    - Created IAM user with `AmazonS3FullAccess` policy and generated access key and secret key.
    - Installed `boto3` and `botocore` python packages.
    - Created a new python file `upload_images.py` and wrote a script to upload several images to the s3 bucket.

2. Wrote a script to generate a presigned url for the image.
    - Created a new python file `generate_presigned_url.py` and wrote a script to generate a presigned url for the image.

3. Wrote a script to get the image from the s3 bucket and save the height and width of the image to a database.
    - Created a new python file `main.py` and wrote a script to get the image from the s3 bucket (using requests) and save the height and width of the image to a database.

4. Added grayscale conversion to the image.
    - Using opencv, I converted the image to grayscale and returned it from the `main` function.

5. Wrote a script to test the `main` function.
    - Created a new python file `test.py` and wrote a script to test the `main` function.
    - The script generates a presigned url for each of the uploaded images and calls the `main` function with the presigned url.

7. Added caching to the `main` function.
    - Using `functools.lru_cache`, I added caching to the `main` function to avoid redundant calls to the s3 bucket.

#### Lessons learned:
- I learned how to create a new s3 bucket and upload images to it.
- Learned about IAM users and how to generate access key and secret key.
- I learned how to use boto3 to interact with s3 buckets.
- I learned how to generate a presigned url for an s3 object.
- I learned how to use opencv to convert an image to grayscale.
- I learned how to use `functools.lru_cache` to add caching to a function.



[Image Credits](./image_credits.md)