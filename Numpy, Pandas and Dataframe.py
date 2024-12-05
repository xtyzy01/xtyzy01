#!/usr/bin/env python
# coding: utf-8

# **One-dimentional numpy**

# In[2]:


import numpy as np


# In[8]:


patient_ages=np.array([25, 30, 40, 22, 35, 50, 29, 60, 41, 28])


# In[9]:


# Calculate the average age of the patients
average_age = np.mean(patient_ages)
print("The average age of the patients is:", average_age)


# In[13]:


# Create a Numpy array with cholesterol levels of 8 patients
cholesterol_levels = np.array([210, 180, 230, 250, 300, 220, 200, 190])

# Identify the highest cholesterol level
highest_cholesterol = np.max(cholesterol_levels)
print("The highest cholesterol level is:", highest_cholesterol)


# In[2]:


#Create a Numpy array of 12 blood pressure readings:
bp_readings= np.array([120, 130, 140, 135, 125, 110, 145, 120, 130, 140, 150, 135])

#Find the standard deviation of blood pressure readings
std_bpreadings= np.std(bp_readings)
print("The standard deviation is:",std_bpreadings)


# In[3]:


# Create a numpy array of body temperatures
temperatures = np.array([37.1, 36.5, 37.3, 36.8, 37.0, 38.0, 36.7, 37.2, 36.9, 37.5])

# Calculate the mean temperature
mean_temperature = np.mean(temperatures)

print("Mean Body Temperature:", mean_temperature)


# In[4]:


# Create a numpy array of patient weight measurements
weights = np.array([60, 72, 65, 58, 82, 75, 70, 68, 66, 80])

# Reverse the order of weights
reversed_weights = weights[::-1]

print("Reversed Weights:", reversed_weights)


# **Two dimensional Numpy**

# In[5]:


import numpy as np

# Create the array
patient_data = np.array([
    [25, 70, 120],
    [30, 80, 130],
    [40, 85, 140]
])

# Access the blood pressure of the second patient
blood_pressure_second_patient = patient_data[1, 2]  # Second patient is at index 1, blood pressure is at index 2
print("Blood pressure of the second patient:", blood_pressure_second_patient)


# In[6]:


# Create the 4x4 array
blood_tests = np.array([
    [5.6, 7.1, 6.2, 5.8],
    [5.3, 6.9, 7.0, 6.5],
    [5.7, 6.5, 6.8, 6.0],
    [5.4, 7.0, 6.5, 5.9]
])

# Calculate the sum of values across each row
row_sums = blood_tests.sum(axis=1)

print("Sum of values across each row (total test results for each patient):", row_sums)


# In[7]:


# Create the 2D array
blood_sugar_levels = np.array([
    [80, 85, 90],
    [95, 92, 88],
    [85, 83, 82],
    [100, 105, 110],
    [75, 78, 80]
])

# Calculate the average blood sugar level for the 3rd patient
average_blood_sugar_third_patient = blood_sugar_levels[2].mean()  # Third patient is at index 2
print("Average blood sugar level for the 3rd patient:", average_blood_sugar_third_patient)


# In[8]:


# Create the BMI matrix
bmi_values = np.array([
    [22.1, 23.5],
    [27.8, 28.0],
    [21.2, 20.9]
])

# Create the weight array
weights = np.array([60, 70, 80])

# Reshape the weight array to align with the BMI matrix for broadcasting
weights = weights.reshape(-1, 1)  # Reshape to a column vector

# Perform element-wise multiplication
bmi_weight_product = bmi_values * weights

print("Element-wise multiplication of BMI and weight:")
print(bmi_weight_product)


# In[3]:


# Define the temperature data for two patients over five days
temperatures = np.array([
    [37.0, 36.5, 37.1, 36.9, 37.0],  # Patient 1
    [36.8, 37.3, 37.0, 36.7, 37.2]   # Patient 2
])

# Find the maximum temperature for each patient (along each row)
max_temperatures = np.max(temperatures, axis=1)

print(max_temperatures)


# **Pandas in healthcare**

# In[4]:


import pandas as pd

# Create a Pandas Series
blood_pressure = pd.Series([120, 130, 140, 135, 125])

# Find the maximum and minimum blood pressure values
max_bp = blood_pressure.max()
min_bp = blood_pressure.min()

print(f"Maximum Blood Pressure: {max_bp}")
print(f"Minimum Blood Pressure: {min_bp}")


# In[5]:


# Create a Pandas Series
cholesterol_levels = pd.Series([210, 180, 220, 250, 280, 230])

# Filter patients with cholesterol levels above 240
high_cholesterol = cholesterol_levels[cholesterol_levels > 240]

print("Patients with cholesterol levels above 240:")
print(high_cholesterol)


# In[6]:


# Create a Pandas Series
ages = pd.Series([35, 40, 25, 30, 45, 50, 55, 60, 65, 70])

# Calculate the median age
median_age = ages.median()

print(f"The median age of the patients is: {median_age}")


# In[7]:


# Create a Pandas Series
weights = pd.Series([70, 80, 75, 65, 85])

# Add 5 kg to each patient's weight
updated_weights = weights + 5

print("Updated weights (in kg):")
print(updated_weights)


# In[8]:


# Create a Pandas Series
temperatures = pd.Series([37.2, 36.8, 37.5, 38.0, 36.6, 37.1, 36.9, 37.3, 37.4, 37.0])

# Calculate the average temperature
average_temperature = temperatures.mean()

print(f"The average temperature of the patients is: {average_temperature:.2f}°C")


# **Dataframe**

# In[1]:


import pandas as pd

# Create the DataFrame with patient data
data = {
    'Name': ['John', 'Jane', 'Tom', 'Alice'],
    'Age': [28, 34, 45, 52],
    'Blood Pressure': [120, 130, 140, 150],
    'Cholesterol': [200, 220, 240, 260]
}
df = pd.DataFrame(data)

# Select patients with cholesterol greater than 220
patients_high_cholesterol = df[df['Cholesterol'] > 220]
print(patients_high_cholesterol)


# In[2]:


# Create a DataFrame with patient information
patient_data = {
    'Name': ['John', 'Jane', 'Tom', 'Alice'],
    'Age': [28, 34, 45, 52],
    'Height': [1.75, 1.68, 1.82, 1.60],  # height in meters
    'Weight': [72, 65, 85, 70],  # weight in kilograms
    'Blood Pressure': [120, 130, 140, 150]
}
patient_df = pd.DataFrame(patient_data)

# Calculate BMI and add it as a new column
patient_df['BMI'] = patient_df['Weight'] / (patient_df['Height'] ** 2)

# Print the DataFrame
print(patient_df)


# In[3]:


# Create a DataFrame with patient blood test results
test_data = {
    'Test ID': [1, 2, 3, 4],
    'Patient Name': ['John', 'Jane', 'Tom', 'Alice'],
    'Result': [5.6, 6.1, 5.8, 6.3]
}
test_df = pd.DataFrame(test_data)

# Filter patients with a test result greater than 6.0
high_result_patients = test_df[test_df['Result'] > 6.0]

# Print the filtered DataFrame
print(high_result_patients)


# In[4]:


# Create a DataFrame with patient age, weight, and height
patient_data_summary = {
    'Age': [28, 34, 45, 52],
    'Weight': [72, 65, 85, 70],  # weight in kilograms
    'Height': [1.75, 1.68, 1.82, 1.60]  # height in meters
}
summary_df = pd.DataFrame(patient_data_summary)

# Calculate the mean of each column
mean_values = summary_df.mean()

# Print the mean values
print(mean_values)


# In[5]:


# Create the DataFrame
data = {
    'Patient Name': ['John', 'Jane', 'Tom', 'Alice'],
    'Treatment Type': ['Surgery', 'Consultation', 'Surgery', 'Consultation'],
    'Treatment Date': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01']
}

df = pd.DataFrame(data)

# Filter records where the treatment type is "Surgery"
surgery_records = df[df['Treatment Type'] == 'Surgery']
print(surgery_records)


# In[ ]:




