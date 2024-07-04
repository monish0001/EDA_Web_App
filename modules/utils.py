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
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap')  # Set the title on the axes (not plt)
    return fig

# Use session state to manage data persistence
def update_session_state(df):
    if 'df' not in session_state:
        session_state.df = df
    else:
        session_state.df = df

def plot_box_and_kde(df, column):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Box plot
    sns.boxplot(x=df[column], ax=ax1)
    ax1.set_title(f'Box Plot of {column}')

    # KDE plot
    sns.kdeplot(df[column], shade=True, ax=ax2)
    ax2.set_title(f'KDE Plot of {column}')

    # Display plot in Streamlit
    st.pyplot(fig)


def plot_count(df, column):
    plt.figure(figsize=(10, 6))

    # Count plot
    sns.countplot(x=column, data=df)
    plt.title(f'Count Plot of {column}')
    plt.xticks(rotation=90)

    # Display plot in Streamlit
    st.pyplot()
def check_columns_distribution(df,selected_col):
    st.subheader(f'Column: {selected_col}')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    sns.boxplot(x=df[selected_col], ax=ax1)
    ax1.set_title('Box Plot')

    sns.kdeplot(df[selected_col], shade=True, ax=ax2)
    ax2.set_title('KDE Plot')

    st.pyplot(fig)

def categorical_column_analysis(df,selected_cat_col):
        st.subheader(f'Column: {selected_cat_col}')

        fig=plt.figure(figsize=(10, 6))
        sns.countplot(x=selected_cat_col, data=df)
        plt.title(f'Count Plot of {selected_cat_col}')
        plt.tight_layout()
        plt.xticks(rotation=90,fontsize='small')
        st.pyplot(fig)

        st.write('**Frequency Analysis:**')
        freq_table = df[selected_cat_col].value_counts().reset_index()
        freq_table.columns = [selected_cat_col, 'Frequency']
        st.write(freq_table)
        
def correlation_analysis(df,col1,col2):
    st.subheader(f'Correlation between {col1} and {col2}')
    correlation = df[col1].corr(df[col2])
    st.write(f'Correlation coefficient: {correlation}')

    fig=plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[col1], y=df[col2])
    plt.title(f'Scatter Plot of {col1} vs {col2}')
    st.pyplot(fig)
    