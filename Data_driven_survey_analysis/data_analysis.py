import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from mpl_toolkits.mplot3d import Axes3D



# 1.PLOTTING PEOPLE RESPONSES WITH THIER RESPECTIVE NATIVES

da1=pd.read_csv('Data_driven_survey_analysis/final_cleaned_survey.csv')

state_counts = da1['Native'].value_counts()

States=list(state_counts.index)

counts=state_counts.values

plt.figure(figsize=(8,8))

colors = sn.color_palette("hsv", len(counts)) 

bars=plt.barh(States, counts, color=colors)

for bar, count, color in zip(bars, counts, colors):

    plt.text(count + 0.5, bar.get_y() + bar.get_height()/2,  
             str(count), 
             va='center', 
             color=color,   
             fontsize=10, 
             fontweight='bold')

plt.ylabel('States in TamilNadu')

plt.xlabel('Number of People')

plt.title('People Responses in each states',fontsize=18,fontweight='bold')

plt.tight_layout()

plt.xticks(rotation=0)

plt.savefig('Data_driven_survey_analysis/media_plots/people-native.png')

plt.show()



# 2.PEOPLE WITH JOB STATUS
 
da2=da1.copy()


# Plotting histogram for each employment status

job_status = da2['employement_status'].unique()

plt.figure(figsize=(10,7))

c=0

for i, status in enumerate(job_status, 1):

    plt.subplot(len(job_status), 1, i)

    ages = da2[da2['employement_status'] == status]['age']

    colors = ['red', 'skyblue', 'green', 'yellow']

    counts, bins, patches = plt.hist(
        ages,
        bins=range(18, 50, 2),
        color=colors[c],
        edgecolor='black'
    )

    for count, patch in zip(counts, patches):

        if count > 0:

            plt.text(
                patch.get_x() + patch.get_width() / 2,   # center of bar
                count / 2,                                # middle height
                int(count),
                ha='center',
                va='center',
                color='k',
                fontsize=7,
                fontweight='bold'
            )
    c+=1

    plt.title(status, fontsize=16, fontweight='bold')

    plt.xlabel('Age')

    plt.ylabel('People')

plt.tight_layout()

plt.savefig('Data_driven_survey_analysis/media_plots/people-job_status')

plt.show()


# 3.PLOTTING UNEMPLOYEMENT STATUS ONLY IN CHENNAI 


da3=da1.copy()

chennai_data = da3[da3['Native'].str.lower() == 'chennai']

counts = chennai_data['employement_status'].value_counts()

plt.figure(figsize=(7,7))

plt.pie(counts, labels=counts.index, autopct='%1.1f%%', colors = ["#DC2828", "#982074","#0EE932FF","#5191C6"])

plt.title('Employment Status Distribution in Chennai',fontsize=20,fontweight='bold')

plt.savefig('Data_driven_survey_analysis/media_plots/people-employement_status-chennai')

plt.show()



# 4.PLOTTING PEOPLES WITH THEIR SOCIAL MEDIA PLATFORMS


da4=da1.copy()

social_counts=da4['social_media'].value_counts()

plt.figure(figsize=(8,5))

plt.stem(social_counts.index, social_counts.values)

plt.xticks(rotation=45)

plt.title('Social Media Usage (Lollipop Chart)')

plt.xlabel('Platform')

plt.ylabel('Number of People')

plt.savefig('Data_driven_survey_analysis/media_plots/people-social_media.png')

plt.show()



# 5.PLOTTING PEOPLES USING SOCIAL MEDIA HOURS AND PRODUCTIVITY

da5 = da1.copy()

# Ordering my data here

hours_order = ['<2', '2', '4', '>4']

productivity_order = [
    'Not productive',
    'Slightly productive',
    'Modertely productive',
    'Highly productive'
]

platforms = da5['social_media'].unique()

for platform in platforms:

    subset = da5[da5['social_media'] == platform]

    pivot = pd.crosstab(
        subset['social_media_hours'],
        subset['how_productive']
    )

    # Enforcing order without dropping data

    pivot = pivot.reindex(hours_order)

    pivot = pivot.reindex(columns=productivity_order) 

    pivot.plot(
        kind='bar',
        stacked=True,
        figsize=(7,5),
        colormap='Paired'
    )

    plt.title(f'Productivity vs Social Media Hours – {platform}',fontsize='16',fontweight='bold')

    plt.xlabel('Social Media Usage Time (Hours)')

    plt.ylabel('Number of People')

    plt.xticks(rotation=0)

    plt.legend(title='Productivity Level')

    plt.tight_layout()

    plt.savefig(f'Data_driven_survey_analysis/media_plots/social_media_hours_vs_productivity-{platform}.png')

    plt.show()



# 6.UMEMPLOYED STATUS WITH DEGREE


da5=da1.copy()

unemployed_df = da5[da5['employement_status'] == 'Unemployed']

degree_counts = unemployed_df['degree'].value_counts()

plt.figure(figsize=(10,6))

colors = sn.color_palette("husl", len(degree_counts)) 

bars = plt.bar(degree_counts.index, degree_counts.values, color=colors, edgecolor='black')

for bar, count in zip(bars, degree_counts.values):

    plt.text(bar.get_x() + bar.get_width()/2, count + 0.1, str(count),
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.xticks(rotation=45, ha='right')

plt.xlabel('Degree',fontweight='bold')

plt.ylabel('Number of Unemployed People',fontweight='bold')

plt.title('Degrees of Unemployed People', fontsize=14, fontweight='bold')

plt.tight_layout()

plt.savefig('Data_driven_survey_analysis/media_plots/degree-unemployement.png')

plt.show()




# 7.PLOTTING SLEEP HOURS VS SOCIAL_MEDIA_HOURS VS NO_OF_PEOPLE

da6=da1.copy()

pivot = da6.pivot_table(
    index='sleep_hours',            # pivot X-axis
    columns='social_media_hours',   # pivot Y-axis
    values='how_productive',        # pivot Z-axis : counts
    aggfunc='count',
    fill_value=0
)

x_labels = pivot.index.tolist()

y_labels = pivot.columns.tolist()

x_pos = np.arange(len(x_labels))

y_pos = np.arange(len(y_labels))

xpos, ypos = np.meshgrid(x_pos, y_pos, indexing="ij")

xpos = xpos.flatten()

ypos = ypos.flatten()

zpos = np.zeros_like(xpos)


dz = []

for x in x_labels:

    for y in y_labels:
        dz.append(pivot.loc[x, y])

dz = np.array(dz)

fig = plt.figure(figsize=(10,7))

ax = fig.add_subplot(111, projection='3d')

colors = plt.cm.viridis(dz / dz.max())  

ax.bar3d(xpos, ypos, zpos, 0.5, 0.5, dz, color=colors, edgecolor='black')


ax.set_xticks(x_pos)

ax.set_xticklabels(x_labels, rotation=45, ha='right')

ax.set_yticks(y_pos)

ax.set_yticklabels(y_labels)

ax.set_zlabel('Number of People')

ax.set_xlabel('Sleep Hours')

ax.set_ylabel('Social Media Hours')

ax.set_title('Sleep Hours vs Social Media Hours vs No of People', fontsize=14, fontweight='bold')

plt.tight_layout()

plt.savefig('Data_driven_survey_analysis/media_plots/sleep-social_media-people')

plt.show()





# 8. PLOTTING FINANCIAL STABILITY VS MONEY MANAGEMENT


da7=da1.copy()

financial_table = pd.crosstab(da7['money_management'], da7['financial_stability'])

# Plotting  heatmap here

plt.figure(figsize=(8,6))

sn.heatmap(financial_table, annot=True, fmt='d', cmap='plasma', cbar=True)

plt.title('Money Management vs Financial Stability', fontsize=14, fontweight='bold')

plt.xlabel('Financial Stability',fontweight='bold')

plt.ylabel('Money Management',fontweight='bold')

plt.tight_layout()

plt.savefig('Data_driven_survey_analysis/media_plots/financial_stability_vs_manage_money')

plt.show()





# 9.PLOTTING AGE VS CAREER_PRESSURE

da8=da1.copy()

career_map = {
    "I don't feel any pressure about my career": 1,
    "I feel career pressure occasionally.": 2,
    "I feel overwhelming pressure every day about my future career": 3,
    "I feel pressure most of the time due to expectations or uncertainty.": 4
}


da8['career_num'] = da8['career_pressure'].map(career_map)


# Scatter plots

plt.figure(figsize=(10,6))

scatter = plt.scatter(
    da8['age'],
    da8['career_num'],
    s=100,
    cmap='viridis',
    alpha=0.8,
    edgecolors='black'
)

plt.xlabel('Age')

plt.ylabel('Career Pressure Level')

plt.title('Age vs Career Pressure', fontsize=14, fontweight='bold')

plt.yticks([1,2,3,4], [
    "No pressure",
    "Occasional",
    "Daily high",
    "Most of the time"
])

cbar = plt.colorbar(scatter)

cbar.set_label('Age vs Career Pressure', rotation=270, labelpad=15)

plt.tight_layout()

plt.savefig('Data_driven_survey_analysis/media_plots/Age_vs_Career_pressure')

plt.show()





# 10.PLOTTING LERAN_NEW VS PRODUCTIVITY (DUE TO SLEEP HOURS)


da9=da1.copy()


learn_map = {
    "I don't update my knowledge.": 1,
    "Once in a few months": 2,
    "Once or twice a month": 3,
    "Daily": 4
}

prod_map = {
    "Not productive": 1,
    "Slightly productive": 2,
    "Modertely productive": 3,
    "Highly productive": 4
}

sleep_map = {'<4':1, '4-6':2, '6-8':3, '>8':4}

da9['learn_num'] = da9['learn_new'].map(learn_map)

da9['prod_num'] = da9['how_productive'].map(prod_map)

da9['sleep_num'] = da9['sleep_hours'].map(sleep_map)

# Scatter plot

plt.figure(figsize=(10,6))

scatter = plt.scatter(
    da9['learn_num'],
    da9['prod_num'],
    c=da9['sleep_num'],       
    s=120,
    cmap='plasma',
    alpha=0.8,
    edgecolors='black'
)

plt.xlabel('Learning Frequency')

plt.ylabel('Productivity Level')

plt.title('Learning New Skills vs Productivity (Color: Sleep Hours)', fontsize=14, fontweight='bold')

plt.xticks([1,2,3,4], ['No learning', 'Few months', 'Monthly', 'Daily'])

plt.yticks([1,2,3,4], ['Not productive', 'Slightly', 'Moderate', 'Highly'])

cbar = plt.colorbar(scatter)

cbar.set_label('Sleep Hours', rotation=270, labelpad=15)

plt.tight_layout()

plt.savefig('Data_driven_survey_analysis/media_plots/skill_development_vs_productivity_vs_sleep')

plt.show()
