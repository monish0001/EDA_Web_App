import streamlit as st
import matplotlib.pyplot as plt
from .utils import plot_box_and_kde, plot_count, plot_correlation_heatmap

def show_eda(df):
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write('**Data Preview:**')
    # Adjust sampling size based on the DataFrame's size
    st.write(st.session_state.df)
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write('**Data Shape:**')
    st.write(df.shape)
    st.markdown('<hr>', unsafe_allow_html=True)
    numeric_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    st.write(f'**Number of Numeric Columns:** {len(numeric_cols)}')
    st.write(f'**Numeric Columns:** {", ".join(numeric_cols)}')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write(f'**Number of Categorical Columns:** {len(categorical_cols)}')
    st.write(f'**Categorical Columns:** {", ".join(categorical_cols)}')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write('**Descriptive Statistics:**')
    st.write(df.describe())
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write('**Missing Values:**')
    st.write(df.isnull().sum())
    st.write(f'Total Missing Values : {df.isnull().sum().sum()}')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write('**Correlation Heatmap:**')
    if st.button('Show Heatmap'):
        fig = plot_correlation_heatmap(df, numeric_cols)
        st.pyplot(fig)
    st.markdown('<hr>', unsafe_allow_html=True)
