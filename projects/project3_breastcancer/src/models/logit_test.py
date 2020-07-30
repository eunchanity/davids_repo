from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)


def logit_test(X_train, X_test, y_train, y_test):
    """
    input: X_train, X_test (dataframe) of features after train/test split, y_train, y_test (series) of target after train/test split
    output: accuracy, precision, recall, f1, roc/auc scores for logistic regression model (after adjusting class weights)
    """
    # fit scaled features to logistic regression
    scaler = StandardScaler()
    X_trainscaled = scaler.fit_transform(X_train)
    X_testscaled = scaler.transform(X_test)

    logit = LogisticRegression(solver="liblinear", class_weight={1: 2, 0: 1})
    logit.fit(X_trainscaled, y_train)
    y_predict = logit.predict(X_testscaled)

    # print accuracy, precision, recall, f1, rocauc scores on test set
    logit_accuracy = accuracy_score(y_test, y_predict)
    logit_precision = precision_score(y_test, y_predict, average="binary", pos_label=1)
    logit_recall = recall_score(y_test, y_predict, average="binary", pos_label=1)
    logit_f1 = f1_score(y_test, y_predict, average="binary", pos_label=1)
    logit_rocauc = roc_auc_score(y_test, logit.predict_proba(X_testscaled)[:, 1])

    return logit_accuracy, logit_precision, logit_recall, logit_f1, logit_rocauc

