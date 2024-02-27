import requests
import cv2
import numpy as np
from functools import lru_cache
from s3_client import s3_client
from generate_presigned_urls import create_presigned_url
from db import connection, cursor


@lru_cache(maxsize=128)
def main(url):
    """
    Takes a presigned s3 url and returns a grayscale image while storing the images height, weight in the database

    :param url: str

    :return: np.ndarray
    """
    response = requests.get(url)
    nparr = np.frombuffer(
        response.content, np.uint8
    )  # convert raw bytes to numpy array
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # decode numpy array to image

    height, width, _ = img.shape

    # Check to see if the image is already in the database
    cursor.execute(
        """
        SELECT EXISTS (SELECT 1 FROM images WHERE url = ?)
        """,
        (url,),
    )

    # If the image is not in the database, add it
    if not cursor.fetchone()[0]:
        cursor.execute(
            "INSERT INTO images (url, height, width) VALUES (?, ?, ?)",
            (url, height, width),
        )

        connection.commit()

    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


if __name__ == "__main__":
    presigned_image_url = create_presigned_url(
        "aicadium-demo", "images/Turtle Photo by Richard Segal.jpg"
    )
    main(presigned_image_url)
    s3_client.close()
    connection.close()
