import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix, 
    precision_score, recall_score, f1_score
)
import matplotlib.pyplot as plt
import seaborn as sns

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
    classifier = st.selectbox("Select classifier", [
        "Logistic Regression", 
        "Support Vector Machine (SVM)",
        "K-Nearest Neighbours (KNN)",
        "Kernel SVM",
        "Naïve Bayes",
        "Decision Tree",
        "Random Forest"
    ])

    # Specify classifier parameters
    if classifier == "Logistic Regression":
        from sklearn.linear_model import LogisticRegression
        C = st.number_input("C (Inverse of regularization strength)", value=1.0, min_value=0.01, step=0.01, key='logreg_C')
        max_iter = st.number_input("Maximum number of iterations", value=100, min_value=10, step=10, key='logreg_max_iter')
        model = LogisticRegression(C=C if C else 1.0, max_iter=max_iter if max_iter else 100)
    elif classifier == "Support Vector Machine (SVM)":
        from sklearn.svm import SVC
        C = st.number_input("C (Regularization parameter)", value=1.0, min_value=0.01, step=0.01, key='svm_C')
        kernel = st.selectbox("Kernel type", ["linear", "poly", "rbf", "sigmoid"], index=2, key='svm_kernel')
        gamma = st.selectbox("Kernel coefficient (gamma)", ["scale", "auto"], key='svm_gamma')
        model = SVC(C=C if C else 1.0, kernel=kernel if kernel else 'rbf', gamma=gamma if gamma else 'scale', probability=True)
    elif classifier == "K-Nearest Neighbours (KNN)":
        from sklearn.neighbors import KNeighborsClassifier
        n_neighbors = st.number_input("Number of neighbors (k)", value=5, min_value=1, step=1, key='knn_n_neighbors')
        model = KNeighborsClassifier(n_neighbors=n_neighbors if n_neighbors else 5)
    elif classifier == "Kernel SVM":
        from sklearn.svm import SVC
        C = st.number_input("C (Regularization parameter)", value=1.0, min_value=0.01, step=0.01, key='ksvm_C')
        gamma = st.selectbox("Kernel coefficient (gamma)", ["scale", "auto"], key='ksvm_gamma')
        model = SVC(kernel='rbf', C=C if C else 1.0, gamma=gamma if gamma else 'scale', probability=True)
    elif classifier == "Naïve Bayes":
        from sklearn.naive_bayes import GaussianNB
        model = GaussianNB()
    elif classifier == "Decision Tree":
        from sklearn.tree import DecisionTreeClassifier
        max_depth = st.number_input("Maximum depth of the tree", value=None, min_value=1, step=1, key='dt_max_depth')
        criterion = st.selectbox("Function to measure the quality of a split", ["gini", "entropy"], index=0, key='dt_criterion')
        model = DecisionTreeClassifier(max_depth=max_depth if max_depth else None, criterion=criterion if criterion else 'gini')
    elif classifier == "Random Forest":
        from sklearn.ensemble import RandomForestClassifier
        n_estimators = st.number_input("Number of trees in the forest", value=100, min_value=10, step=10, key='rf_n_estimators')
        max_depth = st.number_input("Maximum depth of the tree", value=None, min_value=1, step=1, key='rf_max_depth')
        model = RandomForestClassifier(n_estimators=n_estimators if n_estimators else 100, max_depth=max_depth if max_depth else None)

    if st.button("Train and Evaluate"):
        # Train the model
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
        report = classification_report(y_test, y_pred, zero_division=0)

        st.write("### Results")
        st.write(f"Accuracy: {accuracy}")
        st.write(f"Precision: {precision}")
        st.write(f"Recall: {recall}")
        st.write(f"F1 Score: {f1}")
        st.write("Classification Report:")
        st.text(report)

        # Confusion Matrix
        st.write("### Confusion Matrix")
        conf_matrix = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots()
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', ax=ax)
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        st.pyplot(fig)
