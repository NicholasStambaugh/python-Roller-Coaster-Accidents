import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
df = pd.read_csv(r"C:\Program Files\JetBrains\rc.csv")
df.head()
print(df.bus_type)

#get a list of individual years
years = [year for year,df in df.groupby('year')]

###graph 1###
plt.figure(figsize=(12,6))
sns.set_theme(style='darkgrid')
ax = sns.lineplot(data=df.groupby('year').sum(), x=years, y='num_injured', markers='o')
ax.set_xticks(ticks=years)
ax.set_xticklabels(labels=years, rotation=45)

#formatting
ax.set_title('Injuries Per Year\n', fontsize='large')
ax.set_xlabel('\nYear')
ax.set_ylabel('Injuries\n')

#injuries per park type
df.groupby('bus_type')['num_injured'].max() \
.sort_values(ascending=False) \
    .head(5) \
    .sort_values() \
    .plot(kind='barh',
        figsize=(10, 5),
        title='Top 5 Types of Parks for Injury',
        color='blue')
plt.show()

#injuries per type of injury
df.groupby('category')['num_injured'].max() \
    .sort_values(ascending=False) \
    .head(10) \
    .sort_values() \
    .plot(kind='barh',
        figsize=(10, 5),
        title='Top Ten Reasons for Injury',
        color='purple')
plt.show()

#Total Injuries a Year
###graph2###
#filter
columns = ['mechanical', 'op_error', 'employee']
years_df = df.groupby('year')[columns].sum()

#list of individual years
years = [year for year,df in years_df.groupby('year')]

#graph
plt.figure(figsize=(12,6))
plt.grid()
plt.plot(years, years_df.groupby(['year']).sum(), marker='o')
#legend
plt.legend(labels=['mechanical malfunction', 'operation error', 'employee failure'],
           title='Failure Causes',
           fontsize='large',
           title_fontsize='large')

#title and x,y labels
plt.title('Injuries Per Year\n', size=15)
plt.xlabel('\nYear')
plt.ylabel('Injuries\n')

#x-axis tick labels and rotation
plt.xticks(years, rotation=45)

###graph 3###
#filter
df = years_df.groupby(['year']).sum()

#graph
plt.figure(figsize=(12,6))
ax = sns.lineplot(data=df, marker='o', dashes=True)

#x axis tick labels
ax.set_xticks(ticks=years)
ax.set_xticklabels(labels=years, rotation=45)

#title and x,y labels
ax.set_title('Injuries Per Cause of Ride Malfunction\n', fontsize='large')
ax.set_xlabel('\nYear', fontsize='medium')
ax.set_ylabel('Injuries\n', fontsize='medium')

#barchart
df.groupby('device_category')['num_injured'].max()\
    .sort_values(ascending=False) \
    .head(10) \
    .sort_values() \
    .plot(kind='barh',
        figsize=(10, 5),
        title='Top Ten Reasons for Injury',
        color='purple')

###graph4###
#list of individual years
years = [year for year,df in df.groupby('year')]

#filter
df = pd.DataFrame(df.groupby(['device_category', 'year']).sum())
df.sort_values(by='year', ascending=False)

#graph
plt.figure(figsize=(16,8))
ax = sns.lineplot(data=df, x='year', y='num_injured', hue='device_category', marker='X')

#x-axis tick labels and rotation
ax.set_xticks(ticks=years)
ax.set_xticklabels(labels=years, rotation=45)

#title and x,y labels
ax.set_title('Injuries Per Type of Ride\n', fontsize='large')
ax.set_xlabel('\nYear', fontsize='medium')
ax.set_ylabel('Injuries\n', fontsize='medium')

# get a list of ineividual categories
categories = [category for category in df['device_category'].unique()]

# get the total number of injuries for each category
injuries = []
for cat in categories:
    # store total injuries per category in a dictionary
    injuries.append({'category': cat, 'injuries': df[df['device_category'] == cat]['num_injured'].sum()})

# convert dictionary to a dataframe for easy graphical visualization
df = pd.DataFrame(sorted(injuries, key=lambda x: x['injuries'], reverse=True))

# set up the graph
plt.figure(figsize=(16, 8))
ax = sns.lineplot(data=df, x='category', y='injuries', marker='o')

# set specific tick labels and rotation
ax.set_xticklabels(labels=categories, rotation=45)

# set title and x,y labels
ax.set_title('Injuries Per Category of Park\n', fontsize='large')
ax.set_xlabel('Category', fontsize='medium')
ax.set_ylabel('Injuries\n', fontsize='medium')