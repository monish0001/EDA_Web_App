import streamlit as st
from modules.data_loader import load_data
from modules.eda import show_eda
from modules.preprocessing import show_preprocessing
import warnings
warnings.filterwarnings('ignore')  # Ignore all warnings

def main():
    st.title('Exploratory Data Analysis (EDA) and Preprocessing WebApp')

    # Sidebar to upload CSV file
    st.sidebar.title('Upload CSV File')
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])

    if uploaded_file is not None:
        # Load data if not already loaded
        if 'df' not in st.session_state:
            try:
                st.session_state.df = load_data(uploaded_file)
                st.sidebar.success('File successfully uploaded and loaded!')
            except Exception as e:
                st.sidebar.error(f'Error loading file: {str(e)}')
                st.stop()  # Stop execution if file loading fails
        
        # Sidebar menu for EDA and Preprocessing options
        st.sidebar.title('Menu')
        option = st.sidebar.radio('Select an option:', ['EDA', 'Preprocessing'])

        # Based on selected option, display EDA or Preprocessing
        if option == 'EDA':
            show_eda(st.session_state.df)
        elif option == 'Preprocessing':
            show_preprocessing()
    else:
        st.sidebar.info('Awaiting file upload.')

if __name__ == "__main__":
    main()
