import requests
import time
from requests_toolbelt import MultipartEncoder, StreamingIterator
import argparse
import os

# p神的脚本 https://gist.github.com/phith0n/7719ad04f07d6d1cd076a95ba6ce15b9
# python upload.py --url http ://127.0.0.1:8080/upload -c 20 -s 2 -f 1.xml
# 20次假文件，每次2秒，真文件为1.xml
class CustomIter(object):
    def __init__(self, size: int, sleep: int):
        self.len = size
        self.sleep = sleep

    def read(self, chunk_size):
        if self.len > 0:
            time.sleep(self.sleep)
            read_len = min(chunk_size, self.len)
            print("write a chunk, chunk_size: ", chunk_size, "read_len: ", read_len)
            self.len -= read_len
            return b'a' * read_len
        else:
            return b''


def main():
    parser = argparse.ArgumentParser(description='Upload a file with custom chunk size and url.')
    parser.add_argument('-u', '--url', type=str, help='Upload URL')
    parser.add_argument('-c', '--chunk-times', type=int, default=20, help='Chunk times')
    parser.add_argument('-s', '--sleep', type=int, default=1, help='Sleep time in seconds')
    parser.add_argument('-f', '--filename', type=str, help='The real file you want to upload', required=True)
    args = parser.parse_args()

    m = MultipartEncoder(
        fields=(
            ('real', (os.path.basename(args.filename), open(args.filename, 'rb'), 'application/octet-stream')),
            ('fake', ('fake.txt', CustomIter(args.chunk_times*16*1024, args.sleep), 'text/plain')),
        )
    )

    response = requests.post(args.url, data=m, headers={'Content-Type': m.content_type},stream=True)
    print(response.text)


if __name__ == '__main__':
    main()