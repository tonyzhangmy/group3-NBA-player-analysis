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
  
## How to run the code:


### Some figures are in the format of .html which can't be showed inline on Jupyternotebook. So we attach the link here.

[3D PCA categorizing Slider](https://plot.ly/~swishan/16)
<br>
<br>
[2D Scatter Plot Slider](https://plot.ly/~swishan/18)
<br>
<br>
[11 playtypes ](https://plot.ly/~swishan/20)
<br>
<br>
