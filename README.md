# Project Name - Virat-Kohli_Data-Analysis_ODI-runs

#### -- Project Status: [Active]
Need to add annotations in all the bar plot and explore more datasets to understand better which other factos can influence the batting performance of Virat Kohli

## Project Intro/Objective:
The purpose of the project is to perform an in-depth analysis of Virat Kohli's ODI career statistics and understand what all factors are crucial which influences stellar performance when it comes to batting.I have taken into account all the important data which can be helpful in deriving the critical variables.

### Methods Used:
* Web Scraping
* Data Exploration
* Data Wrangling
* Data Visualization

### Technologies Used:
* Python
* Pandas
* Pycharm
* Seaborn
* Requests
* BeautifulSoup
* Matplotlib
* Numpy

## Project Description:

### Prerequisites
  ### -> Dataset:
  * The data set was downloaded from ESPN cric info website through web scraping.              (https://www.espncricinfo.com/india/content/player/253802.html)
  
  ### -> Python Libraries:
  * Pandas
  * Seaborn
  * Requests
  * BeautifulSoup
  * Matplotlib
  * Numpy

### Workflow:
We are going to divide the workflow in 2 sections , one dealing the ODI data on calendar year basis and 2nd one based on the Venue:

## Calender Year Basis:
1. Through web scraping we access and download the required data of Kohli from the ESPN website
2. Then massive amount of Data Wrangling is performed which will be further used for analysis.
3. Create a Dataframe holding the RAW data in a groupby form based on calander year.
4. Perform an extensive Explorative Data Analysis considering variables like Runs, Centuries, Strike-Rate and AverageRuns
5. Develop a correlation table understanding the impacting of each variable on the effective variable which Total runs scored yearly.
6. Parse the Date columns into Datetime object and convert the format into "Year-Week" type.

## Expected Output:
### As you can observe here, for calendar year when Kohli scored more than 1000 runs below listed are the crucial factors which helps him achieving the same 
### No of runs for each calender year increase if below variables increases:

### 1.No of Matches played in each calendar year.

### 2.No. of 4s hit in every ODI match.

### 3.No. of Centuries hit in a calendar year.

### 4.Every time he involved in a chase his run tally increases.

### His Strike rate has the least impact on the total runs scored in an year however no of sixes or batting in first innings do leave an impact to some extent.

 ![VK_TotalRuns_Barplot](https://github.com/jitpavi/Virat-Kohli_Data-Analysis_ODI-runs/blob/master/Output%20folder/VK_TotalRuns_Barplot.jpg)


 ![VK_Centuries_barplot](https://github.com/jitpavi/Virat-Kohli_Data-Analysis_ODI-runs/blob/master/Output%20folder/VK_Centuries_barplot.jpg)
 
 
 ![K_SRvsAvg_lineplot](https://github.com/jitpavi/Virat-Kohli_Data-Analysis_ODI-runs/blob/master/Output%20folder/VK_SRvsAvg_lineplot.jpg)


 ![VK_Yearwise_RegressionPlot](https://github.com/jitpavi/Virat-Kohli_Data-Analysis_ODI-runs/blob/master/Output%20folder/VK_Yearwise_RegressionPlot.jpg)
 
 
 ![VK_Yearwise_HeatMap](https://github.com/jitpavi/Virat-Kohli_Data-Analysis_ODI-runs/blob/master/Output%20folder/VK_Yearwise_HeatMap.jpg)

## Venue Basis:
1. Through web scraping we access and download the required data of Kohli from the ESPN website.
2. Then massive amount of Data Wrangling is performed which will be further used for analysis.
3. Create a Dataframe holding the RAW data in a groupby form based on matches played (Home and Away) on each venue throughout his career.
4. Perform an extensive Explorative Data Analysis considering variables like Runs, Centuries, 4s,6s and batting 1st or 2nd.
5. Develop pie chart showing the relationship between all variables divided in 2 slices Home and Away data respectively.

## Expected Output:
### As you can observe here, for matches played in Home and Away there is massive difference between amongst few variables as listed below:
### 1.Kohli played  more No of Matches outside India.

### 2.Kohli scored  more No of Runs outside India.

### 3.Kohli has hit more No. of Centuries outside India.

### 4.Kohli has hit more No. of 4s outside India.

### This exaclty confirms with our observation found on the earlier section on pre calendar year basis although Strike rate,6s and Avg there is not much of a difference observed here

 ![VK_Venuewise_Piechartplot](https://github.com/jitpavi/Virat-Kohli_Data-Analysis_ODI-runs/blob/master/Output%20folder/VK_Venuewise_Piechartplot.jpg)

## Featured Notebooks/Analysis/Deliverables
* [ViratKohli_ODI Analysis v1.0.py](https://github.com/jitpavi/Virat-Kohli_Data-Analysis_ODI-runs/blob/master/ViratKohli_ODI%20Analysis%20v1.0.py)

## Versioning
Code version - v1.0

## Author:

* **Jitin Pavithran** - [jitpavi](https://github.com/jitpavi)

## Acknowledgments:

* https://www.espncricinfo.com/india/content/player/253802.html

## References:

* https://www.kaggle.com/vijaydwivedi052/analysis-of-virat-kohli-in-test-matches
