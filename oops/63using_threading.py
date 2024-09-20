import requests
from datetime import datetime
import threading

image_data = [
              "https://cnex.com.np/images/Pioneering-Female-Img7.png",
              "https://cnex.com.np/images/Our-Story.png",
              "https://cnex.com.np/images/Our-Story.png",
              "https://cnex.com.np/images/Pioneering-Female-Img7.png",
              "https://cnex.com.np/images/disk-image-rotate.png",
            ]

i = 0
for image_url in image_data:
    print("downloading ",image_url)
    # i = i+1
    data  = requests.get(image_url)
    # #save this image
    with open(f"{i}.png", "wb") as f:
        f.write(data.content)

    image_threading_ = threading.Thread(image_url)
    image_threading_.start()
    image_threading_.join()

