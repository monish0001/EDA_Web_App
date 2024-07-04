import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from .utils import plot_correlation_heatmap,check_columns_distribution,categorical_column_analysis,correlation_analysis

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
    st.write('**Check Columns Distribution:**')
    selected_col = st.selectbox('Select a column for detailed analysis:', numeric_cols)
    if selected_col:
        check_columns_distribution(df,selected_col)
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write('**Categorical Column Analysis:**')
    selected_cat_col = st.selectbox('Select a categorical column for analysis:', categorical_cols)
    if selected_cat_col:
        categorical_column_analysis(df,selected_cat_col)
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write('**Correlation Analysis:**')
    col1, col2 = st.selectbox('Select first column:', numeric_cols), st.selectbox('Select second column:', numeric_cols)
    if col1 and col2:
        correlation_analysis(df,col1,col2)
        
    st.markdown('<hr>', unsafe_allow_html=True)    
    st.write('**Correlation Heatmap:**')
    if st.button('Show Heatmap'):
        fig = plot_correlation_heatmap(df, numeric_cols)
        st.pyplot(fig)
    st.markdown('<hr>', unsafe_allow_html=True)
