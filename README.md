# NBA Player Data Analysis
Analyze player's performance including 11 playtypes to determine new catogories of team roles.

## File Structure
* data:
  * data_raw: Contains the csv we got from the json file for all players from 2015-2019 based on their different playtypes.
  * data_cleaned: Contains the data after cleanning, only with the columns we need for 11 playtypes for all players from 2015-2019.
    * pca_data: Contains the data for PCA.
    * poss_ppp_data: Contains the data for bar graph.
* src: Contains all the source codes for data processing and visuallization.
  * scraping: Contains the functions for scraping and storing the data from stats.nba.com/players/.
  * analysis: Process the data we got, including PCA and k-means.
  * visualization: Plot and visualize the results.
  


### Some figures are in the format of .html which can't be showed inline on Jupyternotebook. So we attached the link here.

[3D PCA categorizing Slider](https://plot.ly/~swishan/16)
![](https://github.com/tonyzhangmy/group3-NBA-player-analysis/blob/master/data/data_cleaned/plots/3D.png)
<br>
<br>
[2D Scatter plot Slider](https://plot.ly/~swishan/18)
![](https://github.com/tonyzhangmy/group3-NBA-player-analysis/blob/master/data/data_cleaned/plots/2D.png)
<br>
<br>
[Playtypes frequency](https://plot.ly/~swishan/20)
![](https://github.com/tonyzhangmy/group3-NBA-player-analysis/blob/master/data/data_cleaned/plots/Playtypes%20Frequency%20Shares.png)
<br>
<br>
