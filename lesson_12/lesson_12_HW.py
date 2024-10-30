import time
import requests
import os
from pathlib import Path
import threading
from multiprocessing import Process


src_root = Path(__file__).parent.parent
txt_path = Path("rockyou.txt")
image_path = "image.jpg"
download_url = "https://picsum.photos/1000/1000"


# DONE Filenames are passed as plain strings, but they must be a Path objects in the concrete function
# that opens the file itself.

# 2. DONE This code works pretty slowly. Change it using multithreading and multiprocessing as we did in the lesson
# 3. DONE Add time counters and uncomment the print command in the try/except block. P.S. Use time.perf_counter.
# 4. The encryption could simulate the heavy task. No need to achieve the actual encryption
# 5. DONE The image downloader MUST download the image for real.


# CPU-bound task (heavy computation)
def encrypt_file(path: Path):
    print(f"Processing file from {path} in process {os.getpid()}")

    # Just simulate a heavy computation
    _ = [i for i in range(100_000_000)]

# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(f"Downloading image from {image_url} in thread {threading.current_thread().name}")
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    print(f"image downloaded as {image_path}")

def as_threads():
    try:
        cpu_task = threading.Thread(target=encrypt_file, args=(txt_path,))
        io_task = threading.Thread(target=download_image, args= (download_url,))

        start = time.perf_counter()

        cpu_task.start()
        io_task.start()

        io_task.join()
        download_counter = time.perf_counter() - start

        cpu_task.join()
        encryption_counter = time.perf_counter() - start

        total_counter = time.perf_counter() - start

        print(
            f"Time taken for encryption task: {encryption_counter}, "
            f"I/O-bound task: {download_counter}, "
            f"Total: {total_counter} seconds"
        )
    except Exception as e:
        print(f"Error occurred: {e}")

def as_thread_and_process():
    try:
        cpu_task = Process(target=encrypt_file, args=(txt_path,))
        io_task = threading.Thread(target=download_image, args=(download_url,))

        start = time.perf_counter()

        cpu_task.start()
        io_task.start()

        io_task.join()
        download_counter = time.perf_counter() - start

        cpu_task.join()
        encryption_counter = time.perf_counter() - start

        total_counter = time.perf_counter() - start

        print(
            f"Time taken for encryption task: {encryption_counter}, "
            f"I/O-bound task: {download_counter}, "
            f"Total: {total_counter} seconds"
        )
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
        # encrypt_file(txt_path)
        # download_image("https://picsum.photos/1000/1000")
        as_threads()
        as_thread_and_process()




