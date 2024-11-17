#!/bin/bash
cd ./mlflow/
mlflow server --backend-store-uri sqlite:///mlruns.db