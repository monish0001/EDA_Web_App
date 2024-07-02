import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit import session_state

def plot_box_and_kde(df, column):
    st.subheader(f'Column: {column}')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    sns.boxplot(x=df[column], ax=ax1)
    ax1.set_title('Box Plot')

    sns.kdeplot(df[column], shade=True, ax=ax2)
    ax2.set_title('KDE Plot')

    st.pyplot(fig)

def plot_count(df, column):
    st.subheader(f'Column: {column}')
    plt.figure(figsize=(10, 6))
    sns.countplot(x=column, data=df)
    plt.title(f'Count Plot of {column}')
    plt.xticks(rotation=90)
    st.pyplot()

    st.write('**Frequency Analysis:**')
    freq_table = df[column].value_counts().reset_index()
    freq_table.columns = [column, 'Frequency']
    st.write(freq_table)

def plot_correlation_heatmap(df, numeric_cols):
    corr_matrix = df[numeric_cols].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    st.pyplot()

# Use session state to manage data persistence
def update_session_state(df):
    if 'df' not in session_state:
        session_state.df = df
    else:
        session_state.df = df
