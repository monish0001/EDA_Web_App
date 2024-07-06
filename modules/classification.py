# modules/classification.py

import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def show_classification(df):
    st.write("### Classification")

    # Select target column
    target_col = st.selectbox("Select target column", df.columns)
    
    # Select feature columns
    feature_cols = st.multiselect("Select feature columns", df.columns.difference([target_col]))
    
    if not feature_cols:
        st.warning("Please select feature columns.")
        return
    
    X = df[feature_cols]
    y = df[target_col]

    # Split the data
    test_size = st.slider("Test size", min_value=0.1, max_value=0.5, step=0.1, value=0.3)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Select classifier
    classifier = st.selectbox("Select classifier", ["Logistic Regression", "Random Forest", "SVM"])

    if st.button("Train and Evaluate"):
        if classifier == "Logistic Regression":
            from sklearn.linear_model import LogisticRegression
            model = LogisticRegression()
        elif classifier == "Random Forest":
            from sklearn.ensemble import RandomForestClassifier
            model = RandomForestClassifier()
        elif classifier == "SVM":
            from sklearn.svm import SVC
            model = SVC()

        # Train the model
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        st.write("### Results")
        st.write(f"Accuracy: {accuracy}")
        st.write("Classification Report:")
        st.text(report)
