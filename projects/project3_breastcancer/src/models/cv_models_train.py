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


def crossval_knn_scores(X_trainval, y_trainval):
    """
    input: X_trainval (dataframe) of features after trainval/test split, y_trainval (series) of target after trainval/test split
    output: accuracy, precision, recall, f1, roc/auc scores for k nearest neighbors model (after cross validation)
    """
    # splitting into train and val sets
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=71)
    (
        cv_knn_accuracy,
        cv_knn_precision,
        cv_knn_recall,
        cv_knn_f1,
        cv_knn_rocauc,
        cv_knn_scores,
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

        # k nearest neighbors
        knn = KNeighborsClassifier()

        # feature scaling
        scaler = StandardScaler()
        X_trainscaled = scaler.fit_transform(X_train)
        X_valscaled = scaler.transform(X_val)

        knn.fit(X_trainscaled, y_train)
        y_predict = knn.predict(X_valscaled)

        # accuracy, precision, recall, f1, roc/auc scores
        cv_knn_accuracy.append(accuracy_score(y_val, y_predict))
        cv_knn_precision.append(
            precision_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_knn_recall.append(
            recall_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_knn_f1.append(f1_score(y_val, y_predict, average="binary", pos_label=1))
        cv_knn_rocauc.append(roc_auc_score(y_val, knn.predict_proba(X_valscaled)[:, 1]))

    # create mean for cv scores
    accuracy_mean = {}
    accuracy_mean["accuracy"] = np.mean(cv_knn_accuracy)

    precision_mean = {}
    precision_mean["precision"] = np.mean(cv_knn_precision)

    recall_mean = {}
    recall_mean["recall"] = np.mean(cv_knn_recall)

    f1_mean = {}
    f1_mean["f1"] = np.mean(cv_knn_f1)

    rocauc_mean = {}
    rocauc_mean["ROC/AUC"] = np.mean(cv_knn_rocauc)

    # all scores in one list
    cv_knn_scores.append(accuracy_mean)
    cv_knn_scores.append(precision_mean)
    cv_knn_scores.append(recall_mean)
    cv_knn_scores.append(f1_mean)
    cv_knn_scores.append(rocauc_mean)

    return cv_knn_scores


def crossval_logit_scores(X_trainval, y_trainval):
    """
    input: X_trainval (dataframe) of features after trainval/test split, y_trainval (series) of target after trainval/test split
    output: accuracy, precision, recall, f1, roc/auc scores for logistic regression model (after cross validation)
    """
    # splitting into train and val sets
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=71)
    (
        cv_logit_accuracy,
        cv_logit_precision,
        cv_logit_recall,
        cv_logit_f1,
        cv_logit_rocauc,
        cv_logit_scores,
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
        logit = LogisticRegression()

        # feature scaling
        scaler = StandardScaler()
        X_trainscaled = scaler.fit_transform(X_train)
        X_valscaled = scaler.transform(X_val)

        logit.fit(X_trainscaled, y_train)
        y_predict = logit.predict(X_valscaled)

        # accuracy, precision, recall, f1 scores
        cv_logit_accuracy.append(accuracy_score(y_val, y_predict))
        cv_logit_precision.append(
            precision_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_logit_recall.append(
            recall_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_logit_f1.append(f1_score(y_val, y_predict, average="binary", pos_label=1))
        cv_logit_rocauc.append(
            roc_auc_score(y_val, logit.predict_proba(X_valscaled)[:, 1])
        )

    # create mean for cv scores
    accuracy_mean = {}
    accuracy_mean["accuracy"] = np.mean(cv_logit_accuracy)

    precision_mean = {}
    precision_mean["precision"] = np.mean(cv_logit_precision)

    recall_mean = {}
    recall_mean["recall"] = np.mean(cv_logit_recall)

    f1_mean = {}
    f1_mean["f1"] = np.mean(cv_logit_f1)

    rocauc_mean = {}
    rocauc_mean["ROC/AUC"] = np.mean(cv_logit_rocauc)

    # all scores in one list
    cv_logit_scores.append(accuracy_mean)
    cv_logit_scores.append(precision_mean)
    cv_logit_scores.append(recall_mean)
    cv_logit_scores.append(f1_mean)
    cv_logit_scores.append(rocauc_mean)

    return cv_logit_scores


def crossval_dtc_scores(X_trainval, y_trainval):
    """
    input: X_trainval (dataframe) of features after trainval/test split, y_trainval (series) of target after trainval/test split
    output: accuracy, precision, recall, f1, roc/auc scores for decision tree model (after cross validation)
    """
    # splitting into train and val sets
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=71)
    (
        cv_dtc_accuracy,
        cv_dtc_precision,
        cv_dtc_recall,
        cv_dtc_f1,
        cv_dtc_rocauc,
        cv_dtc_scores,
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

        # decision tree
        dtc = DecisionTreeClassifier()
        dtc.fit(X_train, y_train)
        y_predict = dtc.predict(X_val)

        # accuracy, precision, recall, f1 scores
        cv_dtc_accuracy.append(accuracy_score(y_val, y_predict))
        cv_dtc_precision.append(
            precision_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_dtc_recall.append(
            recall_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_dtc_f1.append(f1_score(y_val, y_predict, average="binary", pos_label=1))
        cv_dtc_rocauc.append(roc_auc_score(y_val, dtc.predict_proba(X_val)[:, 1]))

    # create mean for cv scores
    accuracy_mean = {}
    accuracy_mean["accuracy"] = np.mean(cv_dtc_accuracy)

    precision_mean = {}
    precision_mean["precision"] = np.mean(cv_dtc_precision)

    recall_mean = {}
    recall_mean["recall"] = np.mean(cv_dtc_recall)

    f1_mean = {}
    f1_mean["f1"] = np.mean(cv_dtc_f1)

    rocauc_mean = {}
    rocauc_mean["ROC/AUC"] = np.mean(cv_dtc_rocauc)

    # all scores in one list
    cv_dtc_scores.append(accuracy_mean)
    cv_dtc_scores.append(precision_mean)
    cv_dtc_scores.append(recall_mean)
    cv_dtc_scores.append(f1_mean)
    cv_dtc_scores.append(rocauc_mean)

    return cv_dtc_scores


def crossval_rfc_scores(X_trainval, y_trainval):
    """
    input: X_trainval (dataframe) of features after trainval/test split, y_trainval (series) of target after trainval/test split
    output: accuracy, precision, recall, f1, roc/auc scores for random forest model (after cross validation)
    """
    # splitting into train and val sets
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=71)
    (
        cv_rfc_accuracy,
        cv_rfc_precision,
        cv_rfc_recall,
        cv_rfc_f1,
        cv_rfc_rocauc,
        cv_rfc_scores,
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
        rfc = RandomForestClassifier()
        rfc.fit(X_train, y_train)
        y_predict = rfc.predict(X_val)

        # accuracy, precision, recall, f1 scores
        cv_rfc_accuracy.append(accuracy_score(y_val, y_predict))
        cv_rfc_precision.append(
            precision_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_rfc_recall.append(
            recall_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_rfc_f1.append(f1_score(y_val, y_predict, average="binary", pos_label=1))
        cv_rfc_rocauc.append(roc_auc_score(y_val, rfc.predict_proba(X_val)[:, 1]))

    # create mean for cv scores
    accuracy_mean = {}
    accuracy_mean["accuracy"] = np.mean(cv_rfc_accuracy)

    precision_mean = {}
    precision_mean["precision"] = np.mean(cv_rfc_precision)

    recall_mean = {}
    recall_mean["recall"] = np.mean(cv_rfc_recall)

    f1_mean = {}
    f1_mean["f1"] = np.mean(cv_rfc_f1)

    rocauc_mean = {}
    rocauc_mean["ROC/AUC"] = np.mean(cv_rfc_rocauc)

    # all scores in one list
    cv_rfc_scores.append(accuracy_mean)
    cv_rfc_scores.append(precision_mean)
    cv_rfc_scores.append(recall_mean)
    cv_rfc_scores.append(f1_mean)
    cv_rfc_scores.append(rocauc_mean)

    return cv_rfc_scores


def crossval_svm_scores(X_trainval, y_trainval):
    """
    input: X_trainval (dataframe) of features after trainval/test split, y_trainval (series) of target after trainval/test split
    output: accuracy, precision, recall, f1, roc/auc scores for support vector machine model (after cross validation)
    """
    # splitting into train and val sets
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=71)
    (
        cv_svm_accuracy,
        cv_svm_precision,
        cv_svm_recall,
        cv_svm_f1,
        cv_svm_rocauc,
        cv_svm_scores,
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

        # support vector machine
        svm = SVC(probability=True)

        # feature scaling
        scaler = StandardScaler()
        X_trainscaled = scaler.fit_transform(X_train)
        X_valscaled = scaler.transform(X_val)

        svm.fit(X_trainscaled, y_train)
        y_predict = svm.predict(X_valscaled)

        # accuracy, precision, recall, f1 scores
        cv_svm_accuracy.append(accuracy_score(y_val, y_predict))
        cv_svm_precision.append(
            precision_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_svm_recall.append(
            recall_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_svm_f1.append(f1_score(y_val, y_predict, average="binary", pos_label=1))
        cv_svm_rocauc.append(roc_auc_score(y_val, svm.predict_proba(X_valscaled)[:, 1]))

    # create mean for cv scores
    accuracy_mean = {}
    accuracy_mean["accuracy"] = np.mean(cv_svm_accuracy)

    precision_mean = {}
    precision_mean["precision"] = np.mean(cv_svm_precision)

    recall_mean = {}
    recall_mean["recall"] = np.mean(cv_svm_recall)

    f1_mean = {}
    f1_mean["f1"] = np.mean(cv_svm_f1)

    rocauc_mean = {}
    rocauc_mean["ROC/AUC"] = np.mean(cv_svm_rocauc)

    # all scores in one list
    cv_svm_scores.append(accuracy_mean)
    cv_svm_scores.append(precision_mean)
    cv_svm_scores.append(recall_mean)
    cv_svm_scores.append(f1_mean)
    cv_svm_scores.append(rocauc_mean)

    return cv_svm_scores


def crossval_gnb_scores(X_trainval, y_trainval):
    """
    input: X_trainval (dataframe) of features after trainval/test split, y_trainval (series) of target after trainval/test split
    output: accuracy, precision, recall, f1, roc/auc scores for gaussian naive bayes model (after cross validation)
    """
    # splitting into train and val sets
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=71)
    (
        cv_gnb_accuracy,
        cv_gnb_precision,
        cv_gnb_recall,
        cv_gnb_f1,
        cv_gnb_rocauc,
        cv_gnb_scores,
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

        # gaussian naive bayes
        gnb = GaussianNB()
        gnb.fit(X_train, y_train)
        y_predict = gnb.predict(X_val)

        # accuracy, precision, recall, f1 scores
        cv_gnb_accuracy.append(accuracy_score(y_val, y_predict))
        cv_gnb_precision.append(
            precision_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_gnb_recall.append(
            recall_score(y_val, y_predict, average="binary", pos_label=1)
        )
        cv_gnb_f1.append(f1_score(y_val, y_predict, average="binary", pos_label=1))
        cv_gnb_rocauc.append(roc_auc_score(y_val, gnb.predict_proba(X_val)[:, 1]))

    # create mean for cv scores
    accuracy_mean = {}
    accuracy_mean["accuracy"] = np.mean(cv_gnb_accuracy)

    precision_mean = {}
    precision_mean["precision"] = np.mean(cv_gnb_precision)

    recall_mean = {}
    recall_mean["recall"] = np.mean(cv_gnb_recall)

    f1_mean = {}
    f1_mean["f1"] = np.mean(cv_gnb_f1)

    rocauc_mean = {}
    rocauc_mean["ROC/AUC"] = np.mean(cv_gnb_rocauc)

    # all scores in one list
    cv_gnb_scores.append(accuracy_mean)
    cv_gnb_scores.append(precision_mean)
    cv_gnb_scores.append(recall_mean)
    cv_gnb_scores.append(f1_mean)
    cv_gnb_scores.append(rocauc_mean)

    return cv_gnb_scores
