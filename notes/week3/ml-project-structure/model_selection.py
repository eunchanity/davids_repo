import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler


def run_crossval_lr(X, y):
    kf = KFold(n_splits=5, shuffle=True, random_state=71)
    cv_lm_r2s, cv_lm_reg_r2s, cv_lm_las_r2s = (
        [],
        [],
        [],
    )  # collect the validation results for both models
    X, y = np.array(X), np.array(y)
    for train_ind, val_ind in kf.split(X, y):

        X_train, y_train = X[train_ind], y[train_ind]
        X_val, y_val = X[val_ind], y[val_ind]

        # simple linear regression
        lm = LinearRegression()
        lm_reg = Ridge(alpha=1)
        lm_las = Lasso(alpha=1)

        lm.fit(X_train, y_train)
        cv_lm_r2s.append(lm.score(X_val, y_val))

        # ridge with feature scaling
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_val_scaled = scaler.transform(X_val)

        lm_reg.fit(X_train_scaled, y_train)
        cv_lm_reg_r2s.append(lm_reg.score(X_val_scaled, y_val))

        # lasso with feature scaling
        lm_las.fit(X_train_scaled, y_train)
        cv_lm_las_r2s.append(lm_las.score(X_val_scaled, y_val))

        return cv_lm_r2s, cv_lm_reg_r2s, cv_lm_las_r2s
