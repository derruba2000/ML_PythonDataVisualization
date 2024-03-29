import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def RunExercise():
    # Scatter Plots
    # Path of the file to read
    iris_filepath = "../../../../Data/Kaggle/DataSets/iris.csv"

    # Read the file into a variable iris_data
    iris_data = pd.read_csv(iris_filepath, index_col="Id")

    # Print the first 5 rows of the data
    print(iris_data.head())


    # Histogram 
    print("Exercise 5 - plot 1")
    plt.figure(figsize=(10,6))
    sns.distplot(a=iris_data['Petal Length (cm)'], kde=False)
    plt.show()



    # KDE plot
    print("Exercise 5 - plot 2")
    sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)
    plt.show()



    # 2D KDE plot
    print("Exercise 5 - plot 3")
    sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")
    plt.show()
    

    # Paths of the files to read
    iris_set_filepath = "../../../../Data/Kaggle/DataSets/iris_setosa.csv"
    iris_ver_filepath = "../../../../Data/Kaggle/DataSets/iris_versicolor.csv"
    iris_vir_filepath = "../../../../Data/Kaggle/DataSets/iris_virginica.csv"

    # Read the files into variables 
    iris_set_data = pd.read_csv(iris_set_filepath, index_col="Id")
    iris_ver_data = pd.read_csv(iris_ver_filepath, index_col="Id")
    iris_vir_data = pd.read_csv(iris_vir_filepath, index_col="Id")

    # Print the first 5 rows of the Iris versicolor data
    iris_ver_data.head()

    # Histograms for each species
    sns.distplot(a=iris_set_data['Petal Length (cm)'], label="Iris-setosa", kde=False)
    sns.distplot(a=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", kde=False)
    sns.distplot(a=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", kde=False)

    # Add title
    plt.title("Histogram of Petal Lengths, by Species")

    # Force legend to appear
    plt.legend()
    plt.show()


    # KDE plots for each species
    sns.kdeplot(data=iris_set_data['Petal Length (cm)'], label="Iris-setosa", shade=True)
    sns.kdeplot(data=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", shade=True)
    sns.kdeplot(data=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", shade=True)

    # Add title
    plt.title("Distribution of Petal Lengths, by Species")
    plt.show()