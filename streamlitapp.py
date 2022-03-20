# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 12:38:43 2022

@author: kalt9
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

# Loading in csvs
@st.cache
def load_hospitals():
    hospital_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return hospital_df

@st.cache
def load_inpatient():
    inpatient_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')
    return inpatient_df

@st.cache
def load_outpatient():
    outpatient_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
    return outpatient_df

# Loading bar
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
    
## Streamlit Questions
st.title('HHA 507 Final Assignment: E2E with Streamlit')
st.subheader('Kallista Tong')
st.write('Questions:')
st.write('1. How does Stony Brook Hospital''s rating compare with the rest of NY?')
st.write('2. What is the most expensive inpatient DRGs for Stony Brook University Hospital?')
st.write('3. What is the most expensive outpatient APCs for Stony Brook University Hospital?')
st.write('4. ...')
st.write('5. ...')
st.write('6. ...')    

# Loading in dataframes
hospital_df = load_hospitals()
inpatient_df = load_inpatient()
outpatient_df = load_outpatient()

# Previewing dataframes
st.header('Hospital Data Preview')
st.markdown('This dataset displays information on hospitals across the United States.')
st.dataframe(hospital_df)

st.header('Inpatient Data Preview')
st.markdown('This dataset displays information on inpatient data for Stony Brook University Hospital.')
st.dataframe(outpatient_df)

st.header('Outpatient Data Preview')
st.markdown('This dataset displays information on outpatient data for Stony Brook University Hospital.')
st.dataframe(inpatient_df)

# Creating a dataframe for New York State hospitals
ny_df = hospital_df[hospital_df['state'] == 'NY']
st.header('Hospitals in New York State')
st.markdown('This dataset displays information on hospitals in New York State.')
st.dataframe(ny_df)

# Creating a dataframe for Stony Brook University Hospital
sbu_df = hospital_df[hospital_df['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL']
st.header('Stony Brook University Hospital')
st. markdown('This dataset displays information on Stony Brook University Hospital')
st.dataframe(sbu_df)

# Question 1
rating_table = ny_df['hospital_overall_rating'].value_counts().reset_index()
st.header('1. How does Stony Brook Hospital''s overall rating compare to the rest of New York State hospitals?')
st.subheader('New York State Hospital Ratings')
st.markdown('The following table shows the distribution of hospital ratings across New York State. From the table above, we can see that Stony Brook University Hospital has an overall rating of 4, landing in the top 10-11% highest hospital ratings in New York.')
st.dataframe(rating_table)

#Question 2
inpatient_table = inpatient_df[inpatient_df['provider_id'] == 330393]
st.header('Stony Brook University Hospital inpatient data')
st.markdown('The following table shows inpatient data for Stony Brook University hospital.')
st.dataframe(inpatient_table)

st.header('2. What is the most expensive inpatient DRGs code for Stony Brook University Hospital?')
st.subheader('Stony Brook Hospital Inpatient DRGs')
inpatient_DRGs_pivot = inpatient_table.pivot_table(index=['provider_id','provider_name','drg_definition'],values=['average_total_payments'])
inpatient_DRGs_desc = inpatient_DRGs_pivot.sort_values(['average_total_payments'], ascending=False)
st.dataframe(inpatient_DRGs_desc)
st.markdown('The most expensive inpatient DRGs code for SBU Hospital is "003 - ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH % NECK W MAJ O.R." with an average total payment of $216,636.')

#Question 3
outpatient_table = outpatient_df[outpatient_df['provider_id'] == 330393]
st.header('3. What is the most expensive outpatient APCs code for Stony Brook University Hospital?')
st.subheader('Stony Brook Hospital Outpatient APCs')
outpatient_APCs_pivot = outpatient_table.pivot_table(index=['provider_id', 'provider_name', 'apc'], values=['average_total_payments'])
outpatient_APCs_desc = outpatient_APCs_pivot.sort_values(['average_total_payments'], ascending=False)
st.dataframe(outpatient_APCs_desc)
st.markdown('The most expensive outpatient APCs code for SBU Hospital is "0074 - Level IV Endoscopy Upper Airway" with an average total pyament of $2,307.')

#Question 4
bar1 = ny_df['readmission_national_comparison'].value_counts().reset_index()
st.bar_chart(data=bar1, width=0, height=0, use_container_width=True)









