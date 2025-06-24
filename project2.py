import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\ANSHIKA\\Downloads\\xAPI-Edu-Data.csv")
df['AbsenceFlag'] = df['StudentAbsenceDays'].map({'Under-7': 0, 'Above-7': 1})
df['Performance'] = df['Class'].map({'L': 0, 'M': 1, 'H': 2})

st.title(" Student Performance Dashboard")

st.write("### Average Engagement by Class")
avg = df.groupby('Class')[['raisedhands', 'VisITedResources', 'AnnouncementsView', 'Discussion']].mean()
st.bar_chart(avg)

st.write("### Correlation Heatmap")
corr = df[['raisedhands', 'VisITedResources', 'AnnouncementsView', 'Discussion', 'AbsenceFlag', 'Performance']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
