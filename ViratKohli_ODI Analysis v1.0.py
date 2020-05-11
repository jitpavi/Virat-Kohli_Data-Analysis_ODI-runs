"""
Code Name: Data Analysis of Virat Kohli's ODI batting career
Code Author: Jitin Pavithran
Code Version: v1.0
Code Description: The purpose of the code is to perform an in-depth analysis of Virat Kohli's ODI career statistics and understand what all factors are crucial which influences stellar performance when it comes to batting
"""

# Import all the important libraries required for this code

from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Perform webscraping using BeautifulSoup method and download the data for ODI statistics for each Calendar year

espncricinfo_url = "https://stats.espncricinfo.com/ci/engine/player/253802.html?class=2;template=results;type=batting;view=innings"

response_vkohli = requests.request("GET",url=espncricinfo_url)

soup_vkohli = BeautifulSoup(response_vkohli.content,'html.parser')

soup_body = soup_vkohli.findAll('tr',class_='data1')

final_list=[]
for body in soup_body[1:]:
    data = body.findAll('td')
    summary_list = [data[len].text.strip() for len in range(len(data))]
    final_list.append(tuple(summary_list))

head_list=[]
soup_heading = soup_vkohli.findAll('tr',class_='headlinks')

col_head = soup_heading[0].findAll('th')
head_list = [col.text.strip() for col in col_head]

# Create a Raw Data Dataframe

kohli_dict= pd.DataFrame(final_list,columns=head_list,index=pd.Series(np.arange(1,249)))

# This data required massive amount of Data Wrangling hence we proceed first with the the removal of unwanted columns

kohli_dict.drop(columns=[""],axis=1,inplace=True)

kohli_dict['ODI Match No.'] = kohli_dict.index.values
kohli_dict.set_index('ODI Match No.',drop=True,inplace=True)
kohli_dict.reset_index(inplace=True)
kohli_dict.rename(columns={'Runs':'Innings Runs Scored','Mins':'Innings Minutes Batted','BF':'Count of Balls Faced','4s':'Count of 4s',
                           '6s':'Count of 6s','SR':'Strike Rate','Pos':'Batting Position','Inns':'Innings','Opposition':'Opposition Team','Ground':'Venue','Start Date':'Match Date'
                           },inplace=True)

kohli_dict['Innings Runs Scored'] = kohli_dict['Innings Runs Scored'].str.replace('*','')
kohli_dict['Opposition Team'] = kohli_dict['Opposition Team'].str.replace('v ','')
kohli_dict.replace('TDNB',0,inplace=True)
kohli_dict.replace('DNB',0,inplace=True)
kohli_dict.replace('-',0,inplace=True)
kohli_dict[['Innings Runs Scored','Innings Minutes Batted','Count of Balls Faced','Count of 4s','Count of 6s','Batting Position','Innings']] = kohli_dict[['Innings Runs Scored','Innings Minutes Batted',
                                                                                                                                                 'Count of Balls Faced','Count of 4s','Count of 6s',
                                                                                                                                                 'Batting Position','Innings']].astype('int')

kohli_dict['Dismissal'] = kohli_dict['Dismissal'].str.replace('0','')
kohli_dict['Dismissal'].fillna('Not Played',inplace=True)
kohli_dict[['Strike Rate']] = kohli_dict[['Strike Rate']].astype(float)
kohli_dict['Match Date'] = pd.to_datetime(kohli_dict['Match Date'])
kohli_dict['Year Played'] = kohli_dict['Match Date'].dt.year


kohli_dict.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Virat_kohli_statistics\Virat_kohli_statistics_filterdata.csv")

# Perform webscraping using BeautifulSoup method and download the data for ODI statistics for each Venue basis

espncricinfo_url_ground = "https://stats.espncricinfo.com/ci/engine/player/253802.html?class=2;orderby=runs;template=results;type=batting;view=ground"

response_vkohli_ground = requests.request("GET",url=espncricinfo_url_ground)

soup_vkohli_ground = BeautifulSoup(response_vkohli_ground.content,'html.parser')

soup_body_ground = soup_vkohli_ground.findAll('tr',class_='title')

final_list_ground=[]
for body in soup_body_ground:
    data = body.findAll('td')
    summary_list = [data[len].text.strip() for len in range(len(data))]
    final_list_ground.extend((summary_list))

soup_body_ground_data = soup_vkohli_ground.findAll('tr',class_='data1')

final_list_ground_data=[]
for body in soup_body_ground_data[1:]:
    data = body.findAll('td')
    summary_list = [data[len].text.strip() for len in range(len(data))]
    final_list_ground_data.append(tuple(summary_list))

head_list=[]
soup_heading_ground_head = soup_vkohli_ground.findAll('tr',class_='headlinks')

col_head = soup_heading_ground_head[0].findAll('th')
head_list = [col.text.strip() for col in col_head]

# Create RAW Data Dataframe holding information on Venue basis
kohli_dict_ground= pd.DataFrame(final_list_ground_data,columns=head_list)


# This data required massive amount of Data Wrangling hence we proceed first with the the removal of unwanted columns

kohli_dict_ground.drop(columns=[""],axis=1,inplace=True)
kohli_dict_ground['Ground'] = final_list_ground

kohli_dict_ground['Venue_location'] = kohli_dict_ground['Ground'].apply(lambda val: ('Home' if re.search('.*India$',val) else 'Away'))

kohli_dict_ground.replace('-',0,inplace=True)

kohli_dict_ground[['Mat','Inns','NO','Runs','BF','100','50','0','4s','6s']] = kohli_dict_ground[['Mat','Inns','NO','Runs','BF','100','50','0','4s','6s']].astype('int')

kohli_dict_ground[['Ave','SR']] = kohli_dict_ground[['Ave','SR']].astype(float)

kohli_dict_ground.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Virat_kohli_statistics\Virat_kohli_grounddata.csv",index=False)


# Explorative Data Analysis of data on the basis matches played at each Venue

Venuewise_Record = kohli_dict_ground.groupby('Venue_location',as_index=False).agg({'Mat':'sum','Inns':'sum','Runs':'sum','SR':'mean',
                                                                                   'Ave':'mean','4s':'sum','6s':'sum','100':'sum','50':'sum'
                                                                                   })


Venuewise_Record.rename(columns={'Runs':'Venuewise_Runs','SR':'Venuewise_SR','Mat':'Venuewise_Matchcount',
                                '4s':'Venuewise_4s','6s':'Venuewise_6s','Ave':'Venuewise_Avg','100':'Venuewise_Centuries'},inplace=True)

Venuewise_Record.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Virat_kohli_statistics\Virat_kohli_statistics_venuewisedata.csv",index=False)

# Explorative Data Analysis based on the Runs scored in ODI  for each calender year

# Data Analysis of Runs scored against each variable
Venue_runs = kohli_dict.groupby('Venue').agg({'Innings Runs Scored':'sum'}).sort_values('Innings Runs Scored',ascending=False)
OppTeam_runs = kohli_dict.groupby('Opposition Team').agg({'Innings Runs Scored':'sum'}).sort_values('Innings Runs Scored',ascending=False)
Batpos_runs = kohli_dict.groupby('Batting Position').agg({'Innings Runs Scored':'sum'}).sort_values('Innings Runs Scored',ascending=False)
Innings_runs= kohli_dict.groupby('Innings').agg({'Innings Runs Scored':'sum'}).sort_values('Innings Runs Scored',ascending=False)
Year_Runs = kohli_dict.groupby('Year Played').agg({'Innings Runs Scored':'sum'}).sort_values('Innings Runs Scored',ascending=False)


# Data Analysis of Centuries against each variable
OppTeam_cent = kohli_dict[kohli_dict['Innings Runs Scored']>=100].groupby('Opposition Team').agg({'Innings Runs Scored':'count'}).sort_values('Innings Runs Scored',ascending=False)
Year_cent = kohli_dict[kohli_dict['Innings Runs Scored']>=100].groupby('Year Played').agg({'Innings Runs Scored':'count'}).sort_values('Innings Runs Scored',ascending=False)
Innings_cent = kohli_dict[kohli_dict['Innings Runs Scored']>=100].groupby('Innings').agg({'Innings Runs Scored':'count'}).sort_values('Innings Runs Scored',ascending=False)
Venue_cent = kohli_dict[kohli_dict['Innings Runs Scored']>=100].groupby('Venue').agg({'Innings Runs Scored':'count'}).sort_values('Innings Runs Scored',ascending=False)

# Data Analysis of Strike Rate and Average runs against each variable
Year_SR_unsort = kohli_dict.groupby('Year Played').agg({'Strike Rate':'mean'})
Year_avg_unsort = kohli_dict.groupby('Year Played').agg({'Innings Runs Scored':'mean'})

# Data Analysis of Runs Scored in each Year of his ODI Career
Yearwise_Record = kohli_dict.groupby('Year Played',as_index=False).agg({'Strike Rate':'mean','ODI Match No.':'size','Count of 4s':'sum',
                                                                        'Count of 6s':'sum','Innings Runs Scored':[np.sum,lambda val: (val>=100).sum()],
                                                                        'Innings':[lambda val: (val == 1).sum(),lambda val: (val == 2).sum()]})

Yearwise_Record.rename(columns={'Innings Runs Scored':'Yearwise_Runs','Strike Rate':'Yearwise_SR','ODI Match No.':'Yearwise_Matchcount',
                                'Count of 4s':'Yearwise_4s','Count of 6s':'Yearwise_6s','<lambda_0>':'Yearwise_Centuries',},inplace=True)
Yearwise_Record.columns = Yearwise_Record.columns.droplevel(1)
Yearwise_Record.columns = ['Year Played', 'Yearwise_SR', 'Yearwise_Matchcount', 'Yearwise_4s','Yearwise_6s', 'Yearwise_Runs', 'Yearwise_Centuries','Batting 1st', 'Batting 2nd']

Yearwise_Record['Yearwise_Avg'] = Yearwise_Record['Yearwise_Runs'] / Yearwise_Record['Yearwise_Matchcount']

Yearwise_Record_corr = Yearwise_Record[['Yearwise_Runs','Yearwise_4s', 'Yearwise_Centuries', 'Batting 2nd','Yearwise_Matchcount','Batting 1st','Yearwise_6s','Yearwise_SR']].corr()

Yearwise_Record_corr.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Virat_kohli_statistics\Virat_kohli_statistics_yearwise_corr.csv")
Yearwise_Record.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Virat_kohli_statistics\Virat_kohli_statistics_yearwisedata.csv",index=False)


# Data Visualisation

# Data Visualisation Plot of Kohli's run tally against each variable

fig1,ax1 = plt.subplots(nrows = 2,ncols = 2,figsize=(18,7))
fig1.canvas.set_window_title("Plotting of Runs Scored against each variable")
fig1.tight_layout(pad = 3.0)

Innings_runs[:5].plot(kind = 'bar',ax = ax1[0,0],rot = 0,colormap = 'bwr_r',width = 0.3)
Year_Runs[:5].plot(kind = 'bar',ax = ax1[0,1],rot = 0,colormap = 'seismic',width = 0.3)
Batpos_runs[:5].plot(kind = 'bar',ax = ax1[1,0],rot = 0,colormap = 'RdBu',width = 0.2)
OppTeam_runs[:5].plot(kind = 'bar',ax = ax1[1,1],rot = 0,colormap = 'coolwarm',width = 0.2)

plt.savefig(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Virat_kohli_statistics\VK_TotalRuns_Barplot.jpg")


# Data Visualisation Plot of Kohli's Centuries against each variable

fig3,ax3 = plt.subplots(nrows = 2,ncols = 2,figsize=(18,7))
fig3.canvas.set_window_title("Plotting of Centuries against each variable")
fig3.tight_layout(pad = 3.0)

Innings_cent[:5].plot(kind = 'bar',ax = ax3[0,0],rot = 0,colormap = 'Wistia',width = 0.3)
Year_cent[:5].plot(kind = 'bar',ax = ax3[0,1],rot = 0,colormap = 'bwr_r',width = 0.3)
Venue_cent[:5].plot(kind = 'bar',ax = ax3[1,0],rot = 0,colormap = 'copper_r',width = 0.2)
OppTeam_cent[:5].plot(kind = 'bar',ax = ax3[1,1],rot = 0,colormap = 'seismic',width = 0.2)

ax3[0,0].legend(labels = ["Count of Centuries"],loc='upper center',fontsize=12)
ax3[0,1].legend(labels = ["Count of Centuries"],loc='upper center',fontsize=12)
ax3[1,0].legend(labels = ["Count of Centuries"],loc='upper center',fontsize=12)
ax3[1,1].legend(labels = ["Count of Centuries"],loc='upper center',fontsize=12)
plt.savefig(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Virat_kohli_statistics\VK_Centuries_barplot.jpg")


# Define the input variables for Pic chart plot

X = ['Venuewise_Runs', 'Venuewise_SR', 'Venuewise_Matchcount', 'Venuewise_4s', 'Venuewise_6s', 'Venuewise_6s', 'Venuewise_Avg','Venuewise_Centuries']
Y = Venuewise_Record['Venuewise_Runs']

# Create a Figure object with dimension 2 rows and 4 columns for showing plot fo each variable

fig4,ax4 = plt.subplots(nrows=2,ncols=4,figsize=(14,7))
fig4.canvas.set_window_title("Pie Chart Plot showing relation between 8 Variables for Venue in Home and Away")
fig4.tight_layout(pad=3.0)

# Plot a Pie Chart for each of the 8 variables

def Create_pie(size,labels,i,j):
    ax = ax4[i,j]
    d = 20 *(i+j)
    explode = (0.1,0)
    total = sum(size)
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#66b3ff','#99ff99']
    ax.pie(size,explode=explode,colors=colors,autopct = lambda p: '{:.0f}'.format(p*total/100),shadow = True, startangle = d,labeldistance=1.0)
    ax.legend(labels,loc = 'lower left',bbox_to_anchor=(0.0, 0.95))

for i in range(2):
    for j in range(4):
        k= j + i*4
        Create_pie([Venuewise_Record[X[k]][0],Venuewise_Record[X[k]][1]],[f"Home - {(re.search('.*$',X[k])).group()}",f"Away - {(re.search('.*$',X[k])).group()}"],i,j)

fig4.subplots_adjust(wspace = 0.25)
plt.savefig(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Virat_kohli_statistics\VK_Venuewise_Piechartplot.jpg")


# Data Visualisation Strike Rate and Avg Run for each year of his career
fig5,ax5 = plt.subplots(figsize=(18,7))
fig5.canvas.set_window_title("Plotting of Strike Rate and Avg Run for each year of his career")
fig5.tight_layout(pad = 3.0)

Year_avg_unsort.plot(kind='line',ax=ax5,marker='o')
Year_SR_unsort.plot(kind='line',ax=ax5,marker='o')
ax5.legend(labels = ["Avg. no. of Runs","Strike Rate"],loc='upper center',fontsize=12)
plt.savefig(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Virat_kohli_statistics\VK_SRvsAvg_lineplot.jpg")


# Define the input variables for Regression plot

X = ['Yearwise_Matchcount', 'Yearwise_4s', 'Yearwise_Centuries', 'Batting 2nd', 'Batting 1st', 'Yearwise_6s', 'Yearwise_SR','Yearwise_Avg']
Y = Yearwise_Record['Yearwise_Runs']

# Create a Figure object with dimension 2 rows and 4 columns for showing plot fo each variable

fig6,ax6 = plt.subplots(nrows=2,ncols=4,figsize=(14,7))
fig6.canvas.set_window_title("Regression Plot showing Correlation between 8 Variables and the Runs Scored in each Year")
fig6.tight_layout(pad=3.0)

# Plot regression plot for each of the 8 variables

c = Yearwise_Record_corr.columns.values.tolist()
for i in range(2):
    for j in range(4):
        k= j + i*4
        sns.regplot(x=Yearwise_Record[X[k]], y=Y, data=Yearwise_Record, ax=ax6[i, j])

plt.savefig(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Virat_kohli_statistics\VK_Yearwise_RegressionPlot.jpg")

#Plot a HeatMap object displaying the correlation between variables and Happiness score

fig7,ax7 = plt.subplots(figsize=(14,7))
plt.title("Heatmap displaying the Correlation mapping between 8 variables and Total Runs Scored in each Year")
sns.heatmap(Yearwise_Record_corr,vmin=-1,vmax=1,cmap="Accent",annot=True)
ax7.figure.subplots_adjust(bottom = 0.3)
plt.savefig(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Virat_kohli_statistics\VK_Yearwise_HeatMap.jpg")


#plt.show()
plt.close()
