# Sleep-Quality-Prediction

This is a sleep quality prediction Machine Learning Project. In this project, we predict the Sleep Quality of the person rated from 0 - 10. Two types of ML models are being used: Linear Discriminent Analysis and Decision Trees.

# Dataset

The dataset being used is sourced from kaggle. The dataset can be found at: https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset. The various attributes of the dataset are as follows:

1. Person ID: An identifier for each individual.
2. Gender: The gender of the person (Male/Female).
3. Age: The age of the person in years.
4. Occupation: The occupation or profession of the person.
5. Sleep Duration (hours): The number of hours the person sleeps per day.
6. Quality of Sleep (scale: 1-10): A subjective rating of the quality of sleep, ranging from 1 to 10.
7. Physical Activity Level (minutes/day): The number of minutes the person engages in physical activity daily.
8. Stress Level (scale: 1-10): A subjective rating of the stress level experienced by the person, ranging from 1 to 10.
9. BMI Category: The BMI category of the person (e.g., Underweight, Normal, Overweight).
10. Blood Pressure (systolic/diastolic): The blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure.
11. Heart Rate (bpm): The resting heart rate of the person in beats per minute.
12. Daily Steps: The number of steps the person takes per day.
13. Sleep Disorder: The presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea).

# Results

LDA gives a maximum of 98.67% accuracy and Decision Trees gives a maximum of 100% accuracy for the current dataset.

The effect of each attribute on the result of the model in each case is shown in the graphs.

# Architecture

This project is made using flask for the web app. The model is exported and added to the flask. The code for the flask app is in the `src/` directory. The flask app exports an API endpoint at the `/` (root).

It listens to the `GET` and `POST` requests at the `\` and serves the HTML template at the root on the `GET` request and calculates and serves the result of the prediction at the `POST` request. The format of data acceptance in the `POST` request is `application/x-www-form-urlencoded`.

# Hosting

The current version of the App can be found at: https://sahilgarg.pythonanywhere.com/. If you find any bug or any issue, please make an issue on github or send a message at: me.sahil.gg@gmail.com. Thanks!

# Contribution

This project is licensed under the MIT license and is open to any code contributions. Just make a PR :)
