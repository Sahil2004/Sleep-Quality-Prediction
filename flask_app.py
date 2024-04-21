from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os
import pickle

app = Flask(__name__)

# Load the pre-trained Decision Tree model
model_path = os.path.join(os.path.dirname(__file__), 'decision_tree_model.pkl')
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs
        gender = request.form['gender']
        age = int(request.form['age'])
        sleep_duration = float(request.form['sleep_duration'])
        physical_activity = float(request.form['physical_activity'])
        stress_level = int(request.form['stress_level'])
        bmi_category = request.form['bmi_category']
        systolic_bp = float(request.form['systolic_bp'])
        diastolic_bp = float(request.form['diastolic_bp'])
        heart_rate = int(request.form['heart_rate'])
        daily_steps = int(request.form['daily_steps'])
        sleep_disorder = request.form['sleep_disorder']

        # Preprocess user inputs
        user_input = pd.DataFrame({
            'Gender': [gender],
            'Age': [age],
            'Sleep Duration (hours)': [sleep_duration],
            'Physical Activity Level (minutes/day)': [physical_activity],
            'Stress Level': [stress_level],
            'BMI Category': [bmi_category],
            'Systolic Blood Pressure': [systolic_bp],
            'Diastolic Blood Pressure': [diastolic_bp],
            'Heart Rate (bpm)': [heart_rate],
            'Daily Steps': [daily_steps],
            'Sleep Disorder': [sleep_disorder]
        })

        # Label encode categorical features
        label_encoder = LabelEncoder()
        for column in ['Gender', 'BMI Category', 'Sleep Disorder']:
            user_input[column] = label_encoder.fit_transform(user_input[column])

        # Predict sleep quality
        sleep_quality = model.predict(user_input)

        return render_template('index.html', sleep_quality=sleep_quality[0])
    return render_template('index.html', sleep_quality=None)

if __name__ == '__main__':
    app.run(debug=True)