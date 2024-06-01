"""
Suggested Answers Study Case 3
@author: fawdy
"""


#========================Study Case 3 Number 1================================#

import pandas as pd
import warnings
warnings.simplefilter("ignore")
import numpy as np

currns = pd.read_excel('study_case_3.xlsx', sheet_name='CURRNS')
tcdns = pd.read_excel('study_case_3.xlsx', sheet_name='TCDNS')
resbalnsw = pd.read_excel('study_case_3.xlsx', sheet_name='RESBALNSW')
resbalreq = pd.read_excel('study_case_3.xlsx', sheet_name='RESBALREQ')


def convert_date(df_input=None):
    
    df_output = df_input.copy()
    df_output['observation_date'] = pd.to_datetime(df_output['observation_date'])   
    df_output.set_index('observation_date', inplace=True)
    
    # Convert unit of account
    ua = df_output['unit_account'][0]
    
    if ua=='millions usd':
        df_output['value'] = df_output['value'] / 1000000
    
    df_output = df_output[['value']]
    
    return df_output

# Resample the data to monthly frequency and sum the values
resbalnsw_monthly = convert_date(resbalnsw).resample('MS').sum()

currns_conv = convert_date(currns)
tcdns_conv = convert_date(tcdns)
resbalreq_conv = convert_date(resbalreq)

# Most current data
df_merge = currns_conv.merge(tcdns_conv, left_index=True, right_index=True).merge(resbalreq_conv, left_index=True, right_index=True).merge(resbalnsw_monthly, left_index=True, right_index=True)

df_merge.columns = ['currns', 'tcdns', 'resbalreq', 'resbalnsw']

df_merge['currency_deposit_ratio'] = df_merge['currns'] / df_merge['tcdns']
df_merge['excess_reserve_ratio'] = (df_merge['resbalnsw'] - df_merge['resbalreq']) / df_merge['tcdns']

# Assuming rr=11%, calculate the money multiplier (M1)
rr = 0.11
cdr = df_merge['currency_deposit_ratio'][-1]
err = df_merge['excess_reserve_ratio'][-1]
m1_mm = (1+cdr)/(rr+cdr+err)


print(f'Answer Number 1 poin a: {np.round(cdr, 3)}')
print(f'Answer Number 1 poin b: {np.round(err, 3)}')
print(f'Answer Number 1 poin c: {np.round(m1_mm, 3)}')


#========================Study Case 3 Number 2================================#


dff = pd.read_excel('study_case_3.xlsx', sheet_name='DFF')
dfedtar = pd.read_excel('study_case_3.xlsx', sheet_name='DFEDTAR')
dfedtaru = pd.read_excel('study_case_3.xlsx', sheet_name='DFEDTARU')
dfedtarl = pd.read_excel('study_case_3.xlsx', sheet_name='DFEDTARL')

dff_conv = convert_date(dff)
dfedtar_conv = convert_date(dfedtar)
dfedtaru_conv = convert_date(dfedtaru)
dfedtarl_conv = convert_date(dfedtarl)

old_target = dff_conv.merge(dfedtar_conv, how='inner', left_index=True, right_index=True)
old_target.columns = ['eff', 'target']
new_target = dff_conv.merge(dfedtaru_conv, how='inner', left_index=True, right_index=True).merge(dfedtarl_conv, how='inner', left_index=True, right_index=True)
new_target.columns = ['eff', 'upper', 'lower']



new_target['status'] = np.where((new_target['eff']<=new_target['upper']) & (new_target['eff']>=new_target['lower']),
                                'inside target', 'outside target')

new_target['status_detail'] = np.where((new_target['eff']>new_target['upper']) & (new_target['status']=='outside target'),
                                       'over the target', 'below the target')

current_ul = new_target['upper'][-1]
current_ll = new_target['lower'][-1]
current_eff = new_target['eff'][-1]
current_status = new_target['status'][-1]

print(f'Answer Number 2 poin a :current upper limit = {current_ul}; current lower limit = {current_ll}; and funds_rate = {current_eff}; the eff is {current_status}')

new_target_outside = new_target[new_target['status']=='outside target']
date_miss = new_target_outside.index[-1]
status_detail = new_target_outside['status_detail'][-1]

if status_detail=='over the target':
    miss_value = new_target_outside['eff'][-1] - new_target_outside['upper'][-1]
else:
    miss_value = new_target_outside['lower'][-1] - new_target_outside['eff'][-1]
    
print(f'Answer Number 2 poin b: The last time Fed miss the target ({status_detail}) = {date_miss}; The Fed miss by {np.round(miss_value, 3)} %')

old_target['miss'] = np.abs(old_target['eff'] - old_target['target'])
avg_miss_a = old_target.loc['2006-01-01':'2007-12-31']['miss'].mean()
avg_miss_b = old_target.loc['2008-01-01':'2008-12-15']['miss'].mean()

new_target_outside['miss'] = np.where(new_target_outside['status_detail']=='over the target',
                                      new_target_outside['eff'] - new_target_outside['upper'],
                                      new_target_outside['lower'] - new_target_outside['eff'])
avg_miss_c = new_target_outside['miss'].mean()

max_miss_a = old_target.loc['2006-01-01':'2008-12-15']['miss'].max()
max_miss_c = new_target_outside['miss'].max()

max_miss = max_miss_c
if max_miss_a>max_miss_c:
    max_miss = max_miss_a

print(f'What was the average daily miss between the beginning of 2006 and the end of 2007? = {np.round(avg_miss_a, 3)} %')
print(f'What was the average daily miss between the beginning of 2008 and December 15, 2008? = {np.round(avg_miss_b, 3)} %')
print(f'What was the average daily miss for the period from December 16, 2008, to the most current date available? = {np.round(avg_miss_c, 3)} %')
print(f'Since 2006, what was the largest single daily miss? = {np.round(max_miss, 3)} %')
