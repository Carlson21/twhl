import requests
import os
import sys
import urllib.request


from bot import *

GAMES = ["IRL",
            "Counter-Strike: Global Offensive",
            "Among Us",
            "Dota 2",
            "Fortnite",
            "Fall Guys: Ultimate Knockout",
            "Call Of Duty: Modern Warfare",
            "VALORANT",
            "Phasmophobia",
            "Minecraft",
            "Grand Theft Auto V",
            "Genshin Impact",
            "Hearthstone",
            "League of Legends",
            "Call of Duty: Black Ops Cold War",
            "World of Warcraft",
            "PLAYERUNKNOWN'S BATTLEGROUNDS",
            "Last Day on Earth: Survival",
            "Poker",
            "Path of Exile",
            "Overwatch",
            "FIFA 21",
            "World of Warships",
            "Sign of Silence",
            "Lineage 2",
            "Virtual Casino",
            "World of Tanks",
            "Escape From Tarkov",
            "Baldur's Gate 3",
            "Mafia: Definitive Edition",
            "Rocket League",
            "Raft"]

def parse_clip(game):

    url = "https://gql.twitch.tv/gql"
    json_req = """[{"query":"query ClipsCards__Game($gameName: String!, $limit: Int, $cursor: Cursor, $criteria: GameClipsInput) { game(name: $gameName) { id clips(first: $limit, after: $cursor, criteria: $criteria) { pageInfo { hasNextPage __typename } edges { cursor node { id slug url embedURL title viewCount language curator { id login displayName __typename } game { id name boxArtURL(width: 52, height: 72) __typename } broadcaster { id login displayName __typename } thumbnailURL createdAt durationSeconds __typename } __typename } __typename } __typename } } ","variables":{"gameName":~,"limit":100,"criteria":{"languages":[],"filter":"LAST_DAY"},"cursor":"MjA="},"operationName":"ClipsCards__Game"}]"""
    json_req = json_req.replace("~", '"' + game + '"')
    r = requests.post(url, data=json_req, headers={"client-id":"kimne78kx3ncx6brgo4mv6wki5h1ko"})
    r_json = r.json()
    try:
        edges = r_json[0]['data']['game']['clips']['edges']
        urls = [edge['node']['url'] for edge in edges]
        nick_names = [edge['node']['curator']['login'] for edge in edges]
        for number, url in enumerate(urls):
            print(url, number)
            download(url, nick_names[number])
    except:
        print(sys.exc_info())



def download(url, nick):
    try:
            dcn = open('Downloaded_clips_names.txt', 'r')
    except:
            print('111111111111111111')
    client_id = '8cj0jqucouj6uv8h5aa46g4n8hmfvt'
    access_token = 'ixuz1qlsuybgc7k46yni9sq2uxg4is'
    basepath = 'clips/'
    slug = url.replace('https://clips.twitch.tv/', '')
    clip_info = requests.get("https://api.twitch.tv/helix/clips?id=" + slug,
                             headers={"Client-ID": client_id, "Authorization": "Bearer " + access_token}).json()
    thumb_url = clip_info['data'][0]['thumbnail_url']
    mp4_url = thumb_url.split("-preview", 1)[0] + ".mp4"
    out_file = basepath + slug + ".mp4"       
    print('OKOKOKOKOKOKOKOK')


    def dl_progress(count, block_size, total_size):
        if total_size / 1024**2 <= 10:
            percent = int(count * block_size * 100 / total_size)
            sys.stdout.write("\r...%d%%" % percent)
            sys.stdout.flush()
        else:
            raise IOError("Too heavy")

    try:
        check = slug in dcn.read()
        if check is True:
            raise IOError("Already added")
        try:
            urllib.request.urlretrieve(mp4_url, out_file, reporthook=dl_progress)
        except:
            print(sys.exc_info(), '333333333')
        dcn_write = open('Downloaded_Clips_Names.txt', 'a')
        dcn_write.write(slug + '\n')
        dcn_write.close()
        send_clip(out_file, nick)


    except:
        print(sys.exc_info(),'2222222222222222222')


while True:
    for game in GAMES:
        parse_clip(game)
