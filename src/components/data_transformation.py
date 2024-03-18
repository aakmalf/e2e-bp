import sys
from dataclasses import dataclass
import os

import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_path: str = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationConfig()

    def data_transformation_object(self):

        """
        
        This function is used to transform the data
        
        """

        try:
            numerical_col = ['national_inv', 'lead_time', 'in_transit_qty', 'forecast_3_month',
                             'forecast_6_month', 'forecast_9_month', 'sales_1_month',
                             'sales_3_month', 'sales_6_month', 'sales_9_month', 'min_bank',
                             'pieces_past_due', 'perf_6_month_avg', 'perf_12_month_avg','local_bo_qty']
            
            categorical_col = ['potential_issue', 'deck_risk', 'oe_constraint', 'ppap_risk','stop_auto_buy']

            numerical_pipe = Pipeline([
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])

            categorical_pipe = Pipeline([
                ("imputer", SimpleImputer(strategy = "most_frequent")),
                ("one_hot_encoder", OneHotEncoder())

            ])

            logging.info(f"numerical columns: {numerical_col}")
            logging.info(f"categorical columns: {categorical_col}")

            preprocessor = ColumnTransformer([
                ("num", numerical_pipe, numerical_col),
                ("cat", categorical_pipe, categorical_col)
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)


    def initiate_data_transformation(self, train_path, test_path):

        """
        
        This function is used to initiate the data transformation
        
        """

        logging.info("Data Transformation has been started")

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("read train and test dataset")

            logging.info("get the preprocessor object")

            preprocessor = self.data_transformation_object()

            target_column = "went_on_backorder"
            drop_column = "rev_stop"

            input_feature_train_df = train_df.drop([target_column, drop_column], axis=1)
            target_train_df = train_df[target_column]

            input_feature_test_df = test_df.drop([target_column, drop_column], axis=1)
            target_test_df = test_df[target_column]

            logging.info("start fit the preprocessor")

            input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor.transform(input_feature_test_df)
            
            logging.info("preprocessor has been fitted")

            train_arr = np.c_[input_feature_train_arr, np.array(target_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_test_df)]

            logging.info("start save the preprocessor")

            save_object(self.transformation_config.preprocessor_path, preprocessor) # we need to save for the object that has been transformed

            return (
                train_arr,
                test_arr,
                self.transformation_config.preprocessor_path
            )

        except Exception as e:

            raise CustomException(e, sys)