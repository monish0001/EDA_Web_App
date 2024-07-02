import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit import session_state
from .utils import plot_box_and_kde, plot_count, plot_correlation_heatmap

def show_eda(df):
    
    st.write('**Data Preview:**')
    # Adjust sampling size based on the DataFrame's size
    sample_size = min(10, len(df))
    st.write(df.sample(sample_size))

    st.write('**Data Shape:**')
    st.write(df.shape)

    numeric_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    st.write(f'**Number of Numeric Columns:** {len(numeric_cols)}')
    st.write(f'**Numeric Columns:** {", ".join(numeric_cols)}')

    st.write(f'**Number of Categorical Columns:** {len(categorical_cols)}')
    st.write(f'**Categorical Columns:** {", ".join(categorical_cols)}')

    st.write('**Descriptive Statistics:**')
    st.write(df.describe())

    st.write('**Missing Values:**')
    st.write(df.isnull().sum())

    st.write('**Check Columns Distribution:**')
    selected_col = st.selectbox('Select a column for detailed analysis:', numeric_cols)

    if selected_col:
        plot_box_and_kde(df, selected_col)

    st.write('**Categorical Column Analysis:**')
    selected_cat_col = st.selectbox('Select a categorical column for analysis:', categorical_cols)

    if selected_cat_col:
        plot_count(df, selected_cat_col)

    st.write('**Correlation Heatmap:**')
    if st.button('Show Heatmap'):
        plot_correlation_heatmap(df, numeric_cols)
