import pandas as pd
from sklearn.decomposition import PCA
import json
import matplotlib.pyplot as plt

def json_to_DF(fname, FILTER_OUT = []):
    '''
    Takes NBA json file and returns dataframes of it for better computation
    NOTE: need to include .json extension in the string; opens from current directory
    NOTE:   FILTER_OUT expects a list of strings that filters out column data by specified header
            Header names to use can be found via: some_json_dict['resultSets'][0]['headers']
            headers = ['SEASON_ID', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID',
            'TEAM_ABBREVIATION', 'TEAM_NAME', 'PLAY_TYPE', 'TYPE_GROUPING',
            'PERCENTILE', 'GP', 'POSS_PCT', 'PPP', 'FG_PCT', 'FT_POSS_PCT',
            'TOV_POSS_PCT', 'SF_POSS_PCT', 'PLUSONE_POSS_PCT', 'SCORE_POSS_PCT',
            'EFG_PCT', 'POSS', 'PTS', 'FGM', 'FGA', 'FGMX']
    :param: fname, str
    :param: FILTER_OUT, list
    :return: DataFrame
    '''

    with open(fname) as f:
        playt_json = json.load(f)

        '''
        Code to take nba json to dataframes is from below:
        https://towardsdatascience.com/using-python-pandas-and-plotly-to-generate-nba-shot-charts-e28f873a99cb
        '''

        data = playt_json['resultSets'][0]['rowSet']
        headers = playt_json['resultSets'][0]['headers']
        df = pd.DataFrame.from_records(data, columns=headers)
        df = df.drop(columns=FILTER_OUT)
        return df

#need modification on how to use the data
df_player = json_to_DF('leaguedash_iso_2019_P.json', FILTER_OUT = ['SEASON_ID','TEAM_ID', 'PLAYER_ID', 'TEAM_ABBREVIATION', 'PLAY_TYPE', 'TEAM_NAME', 'TYPE_GROUPING'])
player_name = df_player.iloc[:, 0]
data_Mat = df_player.iloc[:, 2:]
pca = PCA(n_components=2)
pca.fit(data_Mat)
data_pca = pca.fit_transform(data_Mat)
print(data_pca)

fig, ax = plt.subplots()
for i in range(int(data_pca.size/2)):
    player = data_pca[i]
    ax.scatter(player[0], player[1])
    ax.annotate(player_name[i], (player[0], player[1]))
plt.show()
