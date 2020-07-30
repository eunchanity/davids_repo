import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)


def crossval_logit_weight_scores(X_trainval, y_trainval):
    """
    input: X_trainval (dataframe) of features after trainval/test split, y_trainval (series) of target after trainval/test split
    output: accuracy, precision, recall, f1, roc/auc scores for logistic regression model (after cross validation and adjusting class weights)
    """
    # splitting into train and val sets
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=71)
    (
        cv_logitw_accuracy,
        cv_logitw_precision,
        cv_logitw_recall,
        cv_logitw_f1,
        cv_logitw_rocauc,
        cv_logitw_scores,
    ) = (
        [],
        [],
        [],
        [],
        [],
        [],
    )
    X_trainval, y_trainval = np.array(X_trainval), np.array(y_trainval)
    for train_ind, val_ind in skf.split(X_trainval, y_trainval):
        X_train, y_train = X_trainval[train_ind], y_trainval[train_ind]
        X_val, y_val = X_trainval[val_ind], y_trainval[val_ind]

        # logistic regression
        logitw = LogisticRegression(solver="liblinear", class_weight={1: 2, 0: 1})

        # feature scaling
        scaler = StandardScaler()
        X_trainscaled = scaler.fit_transform(X_train)
        X_valscaled = scaler.transform(X_val)

        logitw.fit(X_trainscaled, y_train)
        y_predict = logitw.predict(X_valscaled)

        # accuracy, precision, recall, f1 scores
        cv_logitw_accuracy.append(accuracy_score(y_val, y_predict))
        cv_logitw_precision.append(
            precision_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_logitw_recall.append(
            recall_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_logitw_f1.append(f1_score(y_val, y_predict, average="binary", pos_label=1))
        cv_logitw_rocauc.append(
            roc_auc_score(y_val, logitw.predict_proba(X_valscaled)[:, 1])
        )

    # create mean for cv scores
    accuracy_mean = {}
    accuracy_mean["accuracy"] = np.mean(cv_logitw_accuracy)

    precision_mean = {}
    precision_mean["precision"] = np.mean(cv_logitw_precision)

    recall_mean = {}
    recall_mean["recall"] = np.mean(cv_logitw_recall)

    f1_mean = {}
    f1_mean["f1"] = np.mean(cv_logitw_f1)

    rocauc_mean = {}
    rocauc_mean["ROC/AUC"] = np.mean(cv_logitw_rocauc)

    # all scores in one list
    cv_logitw_scores.append(accuracy_mean)
    cv_logitw_scores.append(precision_mean)
    cv_logitw_scores.append(recall_mean)
    cv_logitw_scores.append(f1_mean)
    cv_logitw_scores.append(rocauc_mean)

    return cv_logitw_scores


def crossval_rfc_weight_scores(X_trainval, y_trainval):
    """
    input: X_trainval (dataframe) of features after trainval/test split, y_trainval (series) of target after trainval/test split
    output: accuracy, precision, recall, f1, roc/auc scores for random forest model (after cross validation and adjusting class weights)
    """
    # splitting into train and val sets
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=71)
    (
        cv_rfcw_accuracy,
        cv_rfcw_precision,
        cv_rfcw_recall,
        cv_rfcw_f1,
        cv_rfcw_rocauc,
        cv_rfcw_scores,
    ) = (
        [],
        [],
        [],
        [],
        [],
        [],
    )
    X_trainval, y_trainval = np.array(X_trainval), np.array(y_trainval)
    for train_ind, val_ind in skf.split(X_trainval, y_trainval):
        X_train, y_train = X_trainval[train_ind], y_trainval[train_ind]
        X_val, y_val = X_trainval[val_ind], y_trainval[val_ind]

        # random forest
        rfcw = RandomForestClassifier(class_weight={1: 2, 0: 1})
        rfcw.fit(X_train, y_train)
        y_predict = rfcw.predict(X_val)

        # accuracy, precision, recall, f1 scores
        cv_rfcw_accuracy.append(accuracy_score(y_val, y_predict))
        cv_rfcw_precision.append(
            precision_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_rfcw_recall.append(
            recall_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_rfcw_f1.append(f1_score(y_val, y_predict, average="binary", pos_label=1))
        cv_rfcw_rocauc.append(roc_auc_score(y_val, rfcw.predict_proba(X_val)[:, 1]))

    # create mean for cv scores
    accuracy_mean = {}
    accuracy_mean["accuracy"] = np.mean(cv_rfcw_accuracy)

    precision_mean = {}
    precision_mean["precision"] = np.mean(cv_rfcw_precision)

    recall_mean = {}
    recall_mean["recall"] = np.mean(cv_rfcw_recall)

    f1_mean = {}
    f1_mean["f1"] = np.mean(cv_rfcw_f1)

    rocauc_mean = {}
    rocauc_mean["ROC/AUC"] = np.mean(cv_rfcw_rocauc)

    # all scores in one list
    cv_rfcw_scores.append(accuracy_mean)
    cv_rfcw_scores.append(precision_mean)
    cv_rfcw_scores.append(recall_mean)
    cv_rfcw_scores.append(f1_mean)
    cv_rfcw_scores.append(rocauc_mean)

    return cv_rfcw_scores
