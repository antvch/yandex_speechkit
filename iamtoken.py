import time
import jwt
import requests
import os
from dotenv import load_dotenv
load_dotenv()

OAuth_TOKEN = os.getenv('OAuth_TOKEN')

# service_account_id = "ajem4lm21dl6bp27tk6h"
# key_id = "ajegob1vsp8go3980nlr"  # ID ресурса Key, который принадлежит сервисному аккаунту.
#
# with open("private.pem", 'r') as private:
#     private_key = private.read()  # Чтение закрытого ключа из файла.
#
# now = int(time.time())
# payload = {
#     'aud': 'https://iam.api.cloud.yandex.net/iam/v1/tokens',
#     'iss': service_account_id,
#     'iat': now,
#     'exp': now + 360
# }
#
# # Формирование JWT.
# encoded_token = jwt.encode(
#     payload,
#     private_key,
#     algorithm='PS256',
#     headers={
#         'kid': key_id
#     })
# print(encoded_token)


def iamtoken():

    url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"

    payload = {
        "yandexPassportOauthToken": OAuth_TOKEN
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, json=payload)

    token = response.json()
    print(token)
    print(token['iamToken'])
    return token['iamToken']
