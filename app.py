import streamlit as st
import pandas as pd

# Load dataset
def load_data():
    return pd.read_csv('pet_data.csv')

data = load_data()

# Check for necessary columns
required_columns = ['Species', 'Breed', 'Age', 'Symptoms', 'Medical Health', 'Treatment']
missing_columns = [col for col in required_columns if col not in data.columns]

if missing_columns:
    st.error(f"Missing columns in the dataset: {', '.join(missing_columns)}")
    st.stop()

# Streamlit app
st.title('Animal Health and Treatment Predictor')

# Dropdowns for inputs
species = st.selectbox('Species', data['Species'].unique())
breed = st.selectbox('Breed', data[data['Species'] == species]['Breed'].unique())
age = st.number_input('Age', min_value=0, value=1)
symptoms = st.selectbox('Symptoms', data['Symptoms'].unique())

# Function to find medical health and treatment
def get_health_treatment(species, breed, age, symptoms):
    result = data[
        (data['Species'] == species) &
        (data['Breed'] == breed) &
        (data['Age'] == age) &
        (data['Symptoms'] == symptoms)
    ]
    if not result.empty:
        health = result['Medical Health'].values[0]
        treatment = result['Treatment'].values[0]
        return health, treatment
    else:
        return 'No data available', 'No data available'

# Button to get results
if st.button('Get Health and Treatment'):
    health, treatment = get_health_treatment(species, breed, age, symptoms)
    st.write(f"**Medical Health:** {health}")
    st.write(f"**Treatment:** {treatment}")

# To run this Streamlit app, save this code in a file named app.py
# and use the command `streamlit run app.py` in your terminal.
