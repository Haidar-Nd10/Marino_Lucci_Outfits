# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:48:42 2023

@author: Haidar
"""

import streamlit as st
import pandas as pd
import base64

# Load your inventory dataset
inventory = pd.read_csv(r'C:\Users\Haidar\Desktop\Marino Lucci\inventory for photography.csv', encoding='ISO-8859-1')

# Initialize an empty list to store outfit data in session state
if 'outfits_data' not in st.session_state:
    st.session_state.outfits_data = []

# Streamlit App
st.title("Outfit Creator")

# Create a dictionary to store selected values
selected_values = {
    'Top Code': None,
    'Top Color': None,
    'Jacket Code': None,
    'Jacket Color': None,
    'Pants Code': None,
    'Pants Color': None,
}

# Use st.sidebar to place input boxes and buttons in the sidebar menu
with st.sidebar:
    # Streamlit App
    st.title("Select Outfit")
    # Top
    st.subheader('Top')
    unique_top_codes = inventory['Product_Code'].unique()
    top_code = st.selectbox('Top Code', unique_top_codes, key='top_code')
    top_colors = inventory[inventory['Product_Code'] == top_code]['Color'].unique()
    top_color = st.selectbox('Top Color', top_colors, key='top_color')
    selected_values['Top Code'] = top_code
    selected_values['Top Color'] = top_color

    # Jacket
    st.subheader('Jacket')
    unique_jacket_codes = inventory['Product_Code'].unique()
    jacket_code = st.selectbox('Jacket Code', unique_jacket_codes, key='jacket_code')
    jacket_colors = inventory[inventory['Product_Code'] == jacket_code]['Color'].unique()
    jacket_color = st.selectbox('Jacket Color', jacket_colors, key='jacket_color')
    selected_values['Jacket Code'] = jacket_code
    selected_values['Jacket Color'] = jacket_color

    # Pants
    st.subheader('Pants')
    unique_pants_codes = inventory['Product_Code'].unique()
    pants_code = st.selectbox('Pants Code', unique_pants_codes, key='pants_code')
    pants_colors = inventory[inventory['Product_Code'] == pants_code]['Color'].unique()
    pants_color = st.selectbox('Pants Color', pants_colors, key='pants_color')
    selected_values['Pants Code'] = pants_code
    selected_values['Pants Color'] = pants_color

    # Add a button to add the outfit to the DataFrame
    if st.button("Add New Outfit"):
        # Append the selected values to the list in session state
        st.session_state.outfits_data.append(selected_values)

    # Remove Row
    st.subheader('Remove Row')
    if len(st.session_state.outfits_data) > 0:
        row_to_remove = st.selectbox('Select Row to Remove', list(range(len(st.session_state.outfits_data))))
        if st.button("Remove Selected Row"):
            # Remove the selected row from the list in session state
            st.session_state.outfits_data.pop(row_to_remove)

# Display the updated Outfit DataFrame
st.write("Outfit DataFrame:")
if len(st.session_state.outfits_data) > 0:
    df = pd.DataFrame(st.session_state.outfits_data)
    st.write(df)

# Add a button to download the DataFrame as a CSV file
if len(st.session_state.outfits_data) > 0:
    csv_data = df.to_csv(index=False, encoding='utf-8-sig')
    b64 = base64.b64encode(csv_data.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="outfits.csv">Download CSV</a>'
    st.markdown(href, unsafe_allow_html=True)
