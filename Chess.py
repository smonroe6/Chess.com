from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests

from requests import request

printer = pprint.PrettyPrinter()

def print_leaderboard():
    data = get_leaderboards().json
    categories = data.keys()

    for category in categories:
        print('Category: ', category)
        for idx, entry in enumerate(data[category]):
            print(f'Rank: {idx+1} | Username: {entry["username"]} | Rating: {entry["score"]}')


def get_player_rating(username):
    data = get_player_stats(username).json
    categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
    for category in categories:
        print('Category: ', category)
        print(f'Current: {data[category]["last"]["rating"]}')
        print(f'Best: {data[category]["best"]["rating"]}')
        (f'Current: {data[category]["record"]}')
    


def get_most_recent_game(username):
    data = get_player_game_archives(username).json
    url = data['archives'][-1]
    games = requests.get(url).json()
    printer.pprint(games)

get_player_rating('clashlaxboy')
get_most_recent_game('clashlaxboy')