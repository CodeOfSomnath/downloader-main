import requests
import random


def download(url_path):
    res = requests.get(url_path, stream=True)
    size = 2 * 1024
    for data in res.iter_content(chunk_size=size):
        # print(data)
        pass
    res.close()
    if res.status_code != 200:
        print("Download Error.. ")


if __name__ == "__main__":
    urls = ["https://releases.ubuntu.com/22.04.3/ubuntu-22.04.3-desktop-amd64.iso",
            "https://cdimage.kali.org/kali-2023.4/kali-linux-2023.4-installer-amd64.iso"
            ]
    i = 0
    while True:
        print(f"Downloading {i} no. file ")

        try:
             download(random.choice(urls))
        except Exception as e:
            print("Downloading error occured...")
            print(e)

        i = i +1
    # download(url)
