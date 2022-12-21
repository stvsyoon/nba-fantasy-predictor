'''
scrapes NBA box scores for the month of December 2020 and outputs into a CSV
'''

import pandas as pd
from datetime import datetime
import time

dates = []

# table of all december NBA games
# we only use this url for the game date and city code (e.g. LAL for LA Lakers game)
try:
    df = pd.read_html(f'https://www.basketball-reference.com/leagues/NBA_2021_games-december.html')
    df1 = df[0][['Date', 'Home/Neutral']]

    date_string = df1['Date'].to_string(index=False)
    location_string = df1['Home/Neutral'].to_string(index=False)

    new_date = date_string.split('\n')
    new_location = location_string.split('\n')

    for i in range(len(new_location)):
        new_location[i] = new_location[i].strip()

    for i in range(len(new_date)):
        mydatetime = datetime.strptime(new_date[i], '%a, %b %d, %Y')
        newdatetime = mydatetime.strftime('%Y%m%d')
        newdict = {'date': newdatetime, 'team': new_location[i]}
        dates.append(newdict) # example newdict value -> {'date:' 20201222, 'team': Brooklyn Nets}
    print(dates)

except:
    print('u suck')

# ignore this cancer
def add_url(dict):
    if dict['team'] == 'Atlanta Hawks':
        city = 'ATL'
    elif dict['team'] == 'Brooklyn Nets':
        city = 'BRK'
    elif dict['team'] == 'Boston Celtics':
        city = 'BOS'
    elif dict['team'] == 'Charlotte Hornets':
        city = 'CHO'
    elif dict['team'] == 'Chicago Bulls':
        city = 'CHI'
    elif dict['team'] == 'Cleveland Cavaliers':
        city = 'CLE'
    elif dict['team'] == 'Dallas Mavericks':
        city = 'DAL'
    elif dict['team'] == 'Denver Nuggets':
        city = 'DEN'
    elif dict['team'] == 'Detroit Pistons':
        city = 'DET'
    elif dict['team'] == 'Golden State Warriors':
        city = 'GSW'
    elif dict['team'] == 'Houston Rockets':
        city = 'HOU'
    elif dict['team'] == 'Indiana Pacers':
        city = 'IND'
    elif dict['team'] == 'Los Angeles Clippers':
        city = 'LAC'
    elif dict['team'] == 'Los Angeles Lakers':
        city = 'LAL'
    elif dict['team'] == 'Memphis Grizzlies':
        city = 'MEM'
    elif dict['team'] == 'Miami Heat':
        city = 'MIA'
    elif dict['team'] == 'Milwaukee Bucks':
        city = 'MIL'
    elif dict['team'] == 'Minnesota Timberwolves':
        city = 'MIN'
    elif dict['team'] == 'New Orleans Pelicans':
        city = 'NOP'
    elif dict['team'] == 'New York Knicks':
        city = 'NYK'
    elif dict['team'] == 'Oklahoma City Thunder':
        city = 'OKC'
    elif dict['team'] == 'Orlando Magic':
        city = 'ORL'
    elif dict['team'] == 'Philadelphia 76ers':
        city = 'PHI'
    elif dict['team'] == 'Phoenix Suns':
        city = 'PHO'
    elif dict['team'] == 'Portland Trail Blazers':
        city = 'POR'
    elif dict['team'] == 'Sacramento Kings':
        city = 'SAC'
    elif dict['team'] == 'San Antonio Spurs':
        city = 'SAS'
    elif dict['team'] == 'Toronto Raptors':
        city = 'TOR'
    elif dict['team'] == 'Utah Jazz':
        city = 'UTA'
    elif dict['team'] == 'Washington Wizards':
        city = 'WAS'

    dict['city'] = city
    dict['url'] = dict['date'] + '0' + dict['city']

for date in dates:
    add_url(date)

for date in dates:
    url = date['url']
    time.sleep(0.5)
    try:
        df = pd.read_html(f'https://www.basketball-reference.com/boxscores/{url}.html')
        df1 = df[0][:-1]
        df2 = df[8][:-1]

        df1.drop([5], inplace=True)
        df2.drop([5], inplace=True)

        df1.to_csv('Z:\\Simon2\\Projects\\nba\\nba.csv', mode='a', header=False)
        df2.to_csv('Z:\\Simon2\\Projects\\nba\\nba.csv', mode='a', header=False)
    except:
        print('u suck')
