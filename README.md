# Project Name - # Virat-Kohli_Data-Analysis_ODI-runs

#### -- Project Status: [Active]
Need to annotations in all the bar plot and explore more datasets to understand better which other factos can influence the batting performance of Virat Kohli

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
1. Using the API call create a new dataframe and filter with those cases which are being Confirmed.
2. Inorder to acheive the output we need three columns namely Date detected, State Name and Cases Confirmed.
3. Information received through API has columns State codes mentioned in the form of columns which needs to be converted into rows for each respective dates.
4. Create a new List of Tuples which out of the original Dataframe which will contains the values above 3 columns.
5. Using the Tuples we create a master Dataframe which will be used to build the output.
6. Parse the Date columns into Datetime object and convert the format into "Year-Week" type.
7. Create a groupby on the master dataframe to compute the cumulative cases reported week wise for each state/
8. Create a new  ISO Code Dataframe holding the columns of State code and State name.
9. Perform Data Wrangling on the ISO code dataframe and sorted the column name "Code"
10. Iterate through the rows of ISO Code dataframe and create a Dictionary object to hold the mappings of Code names with State Names.

12. Access the open source geocode Json object and save it in a JSON object variable.

12. Create a fig object which will have all the required data to be displayed in the output.

13. Update the geocode property of the Figure object to make the output data more presentabe.
14. Display the data and move the week slider in the bottom to observer the cases in each states.


## Expected Output:
**_As you can observe here, for every week starting from week 10 each state of India diplays the number of cases reported.
For better understanding you can hover your mouse pointer over each state and see the figures.
Due to lack of access to GEOCodes to Ladakh the data couldnt be displayed in the final output.
_**

 ![Chloropeth Map - COVID-19 Cases in India](https://github.com/jitpavi/COVID-19-Week-Wise-Cases---Indian-State--Chloropeth-Visualisation/blob/master/Chloropeth%20Map%20-%20COVID-19%20Cases%20in%20India.JPG)

## Featured Notebooks/Analysis/Deliverables
* [COVID-19-Week-Wise-Cases---Indian-State--Chloropeth-Visualisationv1.0.py](https://github.com/jitpavi/COVID-19-Week-Wise-Cases---Indian-State--Chloropeth-Visualisation/blob/master/COVID-19-Week-Wise-Cases---Indian-State--Chloropeth-Visualisation%20v1.0.py)

## Versioning
Code version - v1.0

## Author:

* **Jitin Pavithran** - [jitpavi](https://github.com/jitpavi)

## Acknowledgments:

* https://www.espncricinfo.com/india/content/player/253802.html

## References:

* https://www.kaggle.com/vijaydwivedi052/analysis-of-virat-kohli-in-test-matches
