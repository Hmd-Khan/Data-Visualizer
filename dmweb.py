import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Data Minning Website")

uploded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploded_file is not None:
    df = pd.read_csv(uploded_file)
    
    st.subheader("Data preview")
    st.write(df.head())
    
    st.subheader("Data summary")
    st.write(df.describe())
    
    st.subheader("Filter data")
    columns=df.columns.tolist()
    selected_columns = st.selectbox("Select columns to filter by",columns)
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox("select value", unique_values)
    
    filtered_df = df[df[selected_columns] == selected_value]
    st.write(filtered_df)
    
    st.subheader("Plot data")
    
    x_column = st.selectbox("Select x column", columns)
    y_column = st.selectbox("Select y column", columns)

    if st.button("Plot data"):
        fig, ax = plt.subplots()
        ax.scatter(filtered_df[x_column], filtered_df[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)
