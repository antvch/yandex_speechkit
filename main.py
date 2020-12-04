import argparse
import os
from dotenv import load_dotenv
import httpx
from iamtoken import iamtoken
from speech_generator import synthesize


load_dotenv()
folder_id = os.getenv('FOLDER_ID')
# folder_id = "b1gacesci6esb91psrc7"
# iam_token = "t1.9euelZqKjc6UmJ7KxouKz86KzIyRlu3rnpWalYqbjJyWx5OPkpCdyM2PiZXl9Pc3dl0B-u9nWhOr3fT3dyRbAfrvZ1oTqw.6ish-6v1lX3LUx9oktJgNJvn-vAM-oVXj2UZ6jlZGFnw0sKF_WeKAdEiaitf24kgZHl0--RAACuBPM_bRVaWBw"
text = input('Введите текст: ')


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--token", required=True, help="IAM token")
    # parser.add_argument("--folder_id", required=True, help="Folder id")
    # parser.add_argument("--text", required=True, help="Text for synthesize")
    # parser.add_argument("--output", required=True, help="Output file name")
    # args = parser.parse_args()

    # with open(args.output, "wb") as f:
    #     for audio_content in synthesize(args.folder_id, args.token, args.text):
    #         f.write(audio_content)
    iam_token = iamtoken()

    with open('audio/speech.wav', "wb") as f:
        for audio_content in synthesize(folder_id, iam_token, text):
            f.write(audio_content)
