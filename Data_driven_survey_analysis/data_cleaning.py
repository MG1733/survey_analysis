import pandas as pd
import numpy as np

# Loading the Uncleaned data file
df=pd.read_csv('Data_driven_survey_analysis/my_survey_analysis.csv')

# Data cleaning for issue happend in converting to csv file

sleep_clean = {
    '06-Aug': '6-8',        
    '04-Jun': '4-6',        
    '6-8': '6-8',
    '4-6': '4-6',
    'More than 8': '>8',
    'less than 4': '<4'
}

social_clean = {
    'less than 2 hours': '2',
    '02-Apr': '4',
    'Rarely': '<2',
    'More than 4 hours': '>4'
    
}

# Applying replacement
df['sleep_hours'] = df['sleep_hours'].replace(sleep_clean)

df['social_media_hours'] = df['social_media_hours'].replace(social_clean)

# Check unique values to confirm

# print(df['sleep_hours'].unique())
# print(df['social_media_hours'].unique())

new_df=df.copy()
# print(new_df[['sleep_hours', 'social_media_hours']].head())

num_duplicates = new_df.duplicated().sum()

print(f"Number of duplicate rows: {num_duplicates}")

duplicate_names = new_df[new_df.duplicated(subset='name', keep=False)]

# print("Duplicated names:",duplicate_names)
# print(duplicate_names['name'].unique())       # Check for Unique before cleaning




# Removing duplicates

new_df = new_df.drop_duplicates(subset='name',keep='first')

duplicate_names = new_df[new_df.duplicated(subset='name', keep=False)]


null_age=np.isnan(new_df.age)

print(null_age)

print(duplicate_names['name'].unique())

print("Any duplicate names left?", new_df['name'].duplicated().any())

new_df.to_csv('Data_driven_survey_analysis/final_cleaned_survey.csv',index=False)







