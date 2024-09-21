# vcc-group1-2050-59-75

## Virtualization and Cloud Computing Project by Group 1
#### Roll Nos: G23AI2050 (Vanshika Gupta), G23AI2059 (Aneerban Choewdhury), G23AI2075 (Shikha Soni)

##### Link to Project: https://vcc-group1-2050-59-75.as.r.appspot.com

This project segments customers based on their income and expense percentage using K-Means clustering. The model is deployed via a Flask application and hosted on Google Cloud Platform (GCP) App Engine.

##### Details of Cluster and Customer Behavior:
1. High Income Low Spend - Prospective customer for buisness growth
2. High Income High Spend - No special attention required
3. Moderate Income Moderate Spend - No special attention required
4. Low Income Low Spend - Low chances of buisness
5. Low Income High Spend - Risk to buisness

##### Steps to Run
1. Open CMD and go to project path
2. Download GoogleCloudSDKInstaller
3. Initialize by entering the command on CMD : *gcloud init*
4. Select Email ID, Project Name and Area
5. Deploy the code by entering the command on CMD: *gcloud app deploy app.yaml --project projectName*
   
##### Files Description
1. app.yaml - GCP configuration file
2. main.py - Flask web app
3. model.pkl - Pre-trained K-Means model
4. requirements.txt - Required dependencies
5. Mall_Customers.csv - Input data for the model
6. notebook.ipynb - Jupyter notebook for data processing and model training
7. templates/index.html - HTML template for web interface

##### Runtime: Python 3.9

##### Libraries:
1. pandas, numpy for data manipulation
2. scikit-learn for machine learning algorithms
3. matplotlib, seaborn for data visualization
4. flask for utilizing the trined model for future prediction.
