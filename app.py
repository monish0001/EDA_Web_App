# import streamlit as st
# from modules.data_loader import load_data
# from modules.eda import show_eda
# from modules.preprocessing import show_preprocessing
# import warnings
# warnings.filterwarnings('ignore')  # Ignore all warnings

# # Add custom CSS to hide the menu and deploy button
# # hide_streamlit_style = """
# #             <style>
# #             #MainMenu {visibility: hidden;}
# #             footer {visibility: hidden;}
# #             header {visibility: hidden;}
# #             .viewerBadge_link__1S137 {display: none;}
# #             </style>
# #             """
# # st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# def main():
#     st.title('Exploratory Data Analysis (EDA) and Preprocessing WebApp')

#     # Sidebar to upload CSV file
#     st.sidebar.title('Upload CSV File')
#     uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])

#     if uploaded_file is not None:
#         # Load data if not already loaded
#         if 'df' not in st.session_state:
#             try:
#                 st.session_state.df = load_data(uploaded_file)
#                 st.sidebar.success('File successfully uploaded and loaded!')
#             except Exception as e:
#                 st.sidebar.error(f'Error loading file: {str(e)}')
#                 st.stop()  # Stop execution if file loading fails
        
#         # Sidebar menu for EDA and Preprocessing options
#         st.sidebar.title('Menu')
#         option = st.sidebar.radio('Select an option:', ['EDA', 'Preprocessing'])

#         # Based on selected option, display EDA or Preprocessing
#         if option == 'EDA':
#             show_eda(st.session_state.df)
#         elif option == 'Preprocessing':
#             show_preprocessing()
#     else:
#         st.sidebar.info('Awaiting file upload.')

# if __name__ == "__main__":
#     main()
import streamlit as st
from modules.data_loader import load_data
from modules.eda import show_eda
from modules.preprocessing import show_preprocessing
import warnings

warnings.filterwarnings('ignore')  # Ignore all warnings

# Add custom CSS to hide the menu and deploy button
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .viewerBadge_link__1S137 {display: none;}
            .css-1aumxhk, .css-qrbaxs {
                font-size: 24px;  /* Adjust the font size as needed */
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def show_classification():
    st.write("### Classification")
    st.write("Coming soon...")

def show_regression():
    st.write("### Regression")
    st.write("Coming soon...")

def main():
    st.title('EDA & Preprocessing WebApp')

    # Main page for file upload
    st.header('Upload CSV File')
    uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'], help='Limit 200MB per file • CSV only')

    if uploaded_file is not None:
        # Load data if not already loaded
        if 'df' not in st.session_state:
            try:
                st.session_state.df = load_data(uploaded_file)
                st.success('File successfully uploaded and loaded!')
            except Exception as e:
                st.error(f'Error loading file: {str(e)}')
                st.stop()  # Stop execution if file loading fails
        
        # Sidebar menu for EDA and Preprocessing options
        st.sidebar.title('Menu')
        main_option = st.sidebar.radio('Select an option:', ['EDA', 'Preprocessing', 'ML Algorithms'])

        if main_option == 'EDA':
            show_eda(st.session_state.df)
        elif main_option == 'Preprocessing':
            show_preprocessing()
        elif main_option == 'ML Algorithms':
            ml_option = st.sidebar.radio('Select an ML Algorithm type:', ['Classification', 'Regression'])
            if ml_option == 'Classification':
                show_classification()
            elif ml_option == 'Regression':
                show_regression()
    else:
        st.info('Awaiting file upload.')

if __name__ == "__main__":
    main()
