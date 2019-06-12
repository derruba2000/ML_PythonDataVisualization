import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




def RunExercise():
    # Scatter Plots

    # Reading the data
    # Path of the file to read
    insurance_filepath = "../../../../Data/Kaggle/DataSets/insurance.csv"

    # Read the file into a variable insurance_data
    insurance_data = pd.read_csv(insurance_filepath)
    insurance_data.head()
    
    # PLOT 1
    print("Exercise 4 - plot 1")
    plt.figure(figsize=(10,6))
    sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])
    sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])
    plt.show()


    # PLOT 2
    print("Exercise 4 - plot 2 Color-coded scatter plots and  linear regression")
    plt.figure(figsize=(10,6))
    sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
    sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)
    plt.show()


    # PLOT 3
    print("Exercise 4 - plot 3 swarm plot")
    plt.figure(figsize=(10,6))
    sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])
    plt.show()