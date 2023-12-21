import requests
import json
import re
import threading as t

url = 'https://api.discord.gx.games/v1/direct-fulfillment'
discordurl = 'https://discord.com/billing/partner-promotions/1180231712274387115/'

headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.opera.com',
    'pragma': 'no-cache',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105","Chromium";v="119","Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
}

data = {
    'partnerUserId': '4211343c691551054c78e6815be36f4c90bfae4fe9bb08a206ff4b324558702a'
}

json_data = json.dumps(data)


def request():
    requests.options(url)
    req = requests.post(url, headers=headers, data=json_data)

    reqContent = req.text

    pattern = '{"token":"([^"]+)"}'
    match = re.search(pattern, reqContent)

    if match:
        token = match.group(1)
        discordFormat = f"{discordurl}{token}\n"

        print(discordFormat)


        with open('savedNitro.txt', 'a') as file:
            file.write(discordFormat)

    else:
        print("No match found.")

def req(num):
    threads = []
    for _ in range(num):
        thread = t.Thread(target=request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    num = int(input("How many nitro? "))
    req(num)