
# Coupuon Acceptance Analysis and Prediction with MLOps(Mlflow) for AskmeOffers

## AskmeOffers sample Project
- It's an End to End Project covering all the required steps in a Data Science Project with Web Interface.
- Coded pipelines for every required stage of the lifecycle for this particular DS Project.
- Deployable and Production Ready project.

## Business Understanding:

### Overview:
- Coupon systems have been widely used to market products, and services and engage customers to use their products and services often. Coupons create a win-win situation for both companies and customers so, by offering a correct coupon to users, which can lead users to become frequent customers and it is enhancing a brand’s impact on its customers.

- How to know which coupon to provide a customer can be a rather complex task, since each customer profile responds differently to each other, and frequently offering them bad coupons or deals might drag them away from your business. To overcome this problem, machine learning techniques can be used to build a better coupon recommendations system.

### Business Objective:
- Predicting whether the customer will accept the coupon or not is a difficult problem, and we can not just recommend it to everyone because of the costs concerned so, in this problem, we will predict whether a customer will accept or reject the offered coupon based on the customer’s profile and history.

- This prediction helps the company in offering a correct coupon so that more customers will use their services which leads to more business for the company.

### DS Objective:
- The goal of the prediction problem is to predict whether a customer will accept or reject the coupon for a specific venue based on demographic and contextual attributes.
- If the customers accept the coupon are labeled as Y=1 and if the customers reject the coupon are labeled as Y=0. This problem can be posed as a binary class classification problem.

## Data
- This is a sample dataset which is publicly available related to coupons.
- Entire dataset description and detailed information about attributes can be found from this   [![Colab Notebook](https://img.shields.io/badge/Colab-Notebook-gold)](https://github.com/Revanth-Reddy-Pingala/AskmeOffers_Project/blob/main/AskmeOffers_Coupuon_Acceptance_Analysis_and_Prediction.ipynb)


## EDA, Feature Engineering and Models 
- Detailed EDA 1 [![Colab Notebook](https://img.shields.io/badge/Colab-Notebook1-gold)](https://github.com/Revanth-Reddy-Pingala/AskmeOffers_Project/blob/main/AskmeOffers_Coupuon_Acceptance_Analysis_and_Prediction.ipynb)

- Detailed EDA 2 [![Colab Notebook](https://img.shields.io/badge/Colab-Notebook2-gold)](https://github.com/Revanth-Reddy-Pingala/AskmeOffers_Project/blob/main/AskmeOffers(2.0)_Coupuon_Acceptance_Analysis_and_Prediction.ipynb)

## Pipelines
- Data Ingestion
- Data Validation
- Data Transformation
- Model Trainer
- Model Evaluation

## Tech Stack Used
- Python, Colab, Flask, Html, CSS, JavaScript
- Dagshub, Mlflow, Conda virtual environment
- VS Code, several Machine learning modules in Pythom

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Revanth-Reddy-Pingala/AskmeOffers_Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n aenv python=3.11 -y
```

```bash
conda activate aenv
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
flask run 
or
python app.py
```

Now,
```bash
open up you local host and port
```

### Dagshub [![Dagshub](https://img.shields.io/badge/Dagshub-blue)](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Revanth-Reddy-Pingala/AskmeOffers_Project.mlflow \
MLFLOW_TRACKING_USERNAME=Revanth-Reddy-Pingala \
MLFLOW_TRACKING_PASSWORD=your_password \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Revanth-Reddy-Pingala/AskmeOffers_Project.mlflow

export MLFLOW_TRACKING_USERNAME=Revanth-Reddy-Pingala

export MLFLOW_TRACKING_PASSWORD=your_password
```


## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model

## Demo Screenshots
<img width="1463" alt="1" src="https://github.com/Revanth-Reddy-Pingala/AskmeOffers_Project/assets/125516124/6c75489b-8754-4d60-8e45-53a725abf428">
<img width="1463" alt="2" src="https://github.com/Revanth-Reddy-Pingala/AskmeOffers_Project/assets/125516124/fb814144-8736-4f8a-a182-dea30b3a6f6e">
<img width="1463" alt="3" src="https://github.com/Revanth-Reddy-Pingala/AskmeOffers_Project/assets/125516124/e4fa95e1-c2e7-4486-b0ff-0a7b6c820d8d">
<img width="1463" alt="4" src="https://github.com/Revanth-Reddy-Pingala/AskmeOffers_Project/assets/125516124/a1214d48-01f9-48c8-8b78-9367695eaaf7">


## 🔗 Connect with me
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/revanth-reddy-pingala/)
[![linkedin](https://img.shields.io/badge/Google_Scholar-4285F4?style=for-the-badge&logo=google-scholar&logoColor=white)](https://scholar.google.com/citations?user=Iy1dCXcAAAAJ&hl=en)
[![Youtube](https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@revanthreddy369?feature=shared)
[![Blogger](https://img.shields.io/badge/Blogger-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://rrdatadiaries.blogspot.com/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/revanth_reddy.1459/)
[![X](https://img.shields.io/badge/X-4285F4?style=for-the-badge&logo=x&logoColor=white)](https://twitter.com/Revanth_R79)





