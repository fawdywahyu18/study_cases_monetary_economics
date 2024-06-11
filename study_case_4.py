"""
Suggested Answers Study Case 4
@author: fawdy
"""

import pandas as pd
import warnings
warnings.simplefilter("ignore")
import numpy as np
from sklearn.linear_model import LinearRegression

#========================Study Case 4 Number 1================================#

# Load data
pcectpi = pd.read_excel('study_case_4.xlsx', sheet_name='PCECTPI')
unrate = pd.read_excel('study_case_4.xlsx', sheet_name='UNRATE')
nrou = pd.read_excel('study_case_4.xlsx', sheet_name='NROU')

def convert_date(df_input=None):
    
    df_output = df_input.copy()
    df_output['observation_date'] = pd.to_datetime(df_output['observation_date'])   
    df_output.set_index('observation_date', inplace=True)
    df_output = df_output[['value']]
    
    return df_output

# Resample the monthly data to quarterly frequency and avregae the values
unrate_quarterly = convert_date(unrate).resample('QS').mean()
nrou_quarterly = convert_date(nrou).resample('QS').mean()
pcectpi_conv = convert_date(pcectpi)
pcectpi_conv['change_yoy'] = (pcectpi_conv['value'] - pcectpi_conv['value'].shift(4))*100 / pcectpi_conv['value'].shift(4)

# Most Current Data
df_merge = unrate_quarterly.merge(nrou_quarterly, left_index=True, right_index=True).merge(pcectpi_conv, left_index=True, right_index=True)
df_merge.columns = ['unrate', 'nrou', 'pcectpi', 'pcectpi_change_yoy']

# Unemployment Gap and Inflation Gap
# Unemployment Gap
df_merge['un_gap'] = df_merge['unrate'] - df_merge['nrou']

# Inflation Gap
df_merge['time_trend'] = np.arange(len(df_merge))
X = df_merge[['time_trend']]
y = df_merge['pcectpi_change_yoy']

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Calculate the trend line and inflation gap
df_merge['trend_inflation'] = model.predict(X)
df_merge['inflation_gap'] = df_merge['pcectpi_change_yoy'] - df_merge['trend_inflation']

# Filter more than 2000 Q1
df_merge_filter = df_merge[df_merge.index >= '2000-01-01']

# Violation requirements
def check_violations(df):
    # Check for consecutive quarters where unemployment gap > 1.0
    df['unemployment_violation'] = (df['un_gap'] > 1.0)
    df['unemployment_violation'] = df['unemployment_violation'].rolling(window=2).sum() == 2

    # Check for consecutive quarters where absolute inflation gap > 0.5
    df['inflation_violation'] = (df['inflation_gap'].abs() > 0.5)
    df['inflation_violation'] = df['inflation_violation'].rolling(window=2).sum() == 2

    # Combine both conditions to create the categorical variable
    df['violated'] = np.where(df['unemployment_violation'] | df['inflation_violation'], 'violated', 'not_violated')

    return df

# Apply the function to the DataFrame
df_violation = check_violations(df_merge_filter)


# Study Case 4 number 1 point a, b, and c.
inflation_violation = df_violation[df_violation['inflation_violation']==True].index
unemployment_violation = df_violation[df_violation['unemployment_violation']==True].index

print(f'study case 4 number 1 point a inflation violation: {inflation_violation}')
print(f'study case 4 number 1 point a unemployment violation: {unemployment_violation}')

currrent_violation = df_violation['violated'][-1]
print(f'study case 4 number 1 point b current violation: {currrent_violation}')


#========================Study Case 4 Number 2================================#

nonborres = pd.read_excel('study_case_4.xlsx', sheet_name='NONBORRES')
fedfunds = pd.read_excel('study_case_4.xlsx', sheet_name='FEDFUNDS')
nonborres_conv = convert_date(nonborres)
fedfunds_conv = convert_date(fedfunds)
df_merge2 = nonborres_conv.merge(fedfunds_conv, left_index=True, right_index=True)
df_merge2.columns = ['nonborres', 'fedfunds']

df_merge2['nonborres_mtm'] = (df_merge2['nonborres'] - df_merge2['nonborres'].shift(1))*100 / df_merge2['nonborres'].shift(1)
df_merge2['nonborres_yoy'] = (df_merge2['nonborres'] - df_merge2['nonborres'].shift(12))*100 / df_merge2['nonborres'].shift(12)

df_merge2['fedfunds_mtm'] = df_merge2['fedfunds'] - df_merge2['fedfunds'].shift(1)
df_merge2['fedfunds_yoy'] = df_merge2['fedfunds'] - df_merge2['fedfunds'].shift(12)

# Export dataset
df_merge2.to_excel("sc_42a.xlsx")

correlation_mtm = df_merge2['nonborres_mtm'].corr(df_merge2['fedfunds_mtm'])
correlation_yoy = df_merge2['nonborres_yoy'].corr(df_merge2['fedfunds_yoy'])

print(f'study case 4 number 2 point b, mtm correlation: {np.round(correlation_mtm, 3)}')
print(f'study case 4 number 2 point b, yoy correlation: {np.round(correlation_yoy, 3)}')



