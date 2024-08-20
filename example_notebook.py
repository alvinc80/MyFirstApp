import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title('Iris Dataset Analysis')

# Load the dataset
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
    df = pd.read_csv(url)
    return df

df = load_data()

# Display the first few rows of the dataframe
st.subheader('Data Overview')
st.write(df.head())

# Histogram of 'sepal_length'
st.subheader('Histogram of Sepal Length')
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.histplot(df['sepal_length'], kde=True, ax=ax1)
ax1.set_title('Histogram of Sepal Length')
ax1.set_xlabel('Sepal Length')
ax1.set_ylabel('Frequency')
st.pyplot(fig1)

# Scatter plot of 'sepal_length' vs 'sepal_width'
st.subheader('Sepal Length vs Sepal Width')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', data=df, hue='species', ax=ax2)
ax2.set_title('Sepal Length vs Sepal Width')
ax2.set_xlabel('Sepal Length')
ax2.set_ylabel('Sepal Width')
ax2.legend(title='Species')
st.pyplot(fig2)



