# A/B Testing Analysis Project

This project encompasses the analysis of A/B testing data to derive insights into user behavior and the impact of new features or changes.

## Description

In this analysis, we explore the data collected from an A/B test to compare the performance of two groups: Control and Test. The data includes user interactions with a web-based application, with the goal of understanding how a new change affects metrics such as completion rate and error rate.

## Installation

To run this project, ensure you have Jupyter Notebooks installed, which can be done through [Anaconda](https://www.anaconda.com/products/individual) or by installing [Jupyter](https://jupyter.org/install) directly.

## Usage

Open the `Project56.ipynb` notebook in Jupyter to view the analysis. The notebook is divided into sections for importing data, preparing data, exploratory data analysis (EDA), and hypothesis testing.

### Importing Data

The data is loaded from various `.csv` files into Pandas DataFrames. These files contain anonymized user data, interaction logs, and control/test group assignments.

### Data

The data consists of several datasets, detailing user demographics, behaviors, and interactions with the web interface:

- Client demographics and statistics (df1)
- Experiment group classifications (df2)
- User interactions part 1 (df3)
- User interactions part 2 (df4)

These datasets are merged to facilitate comprehensive analysis.

### Installation

To run this project, you need Python and the following libraries installed:

- pandas
- numpy
- matplotlib
- seaborn
- scipy
- statsmodels

### You can install these packages using `pip`:

pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install scipy 
pip instal statsmodels

### Preparing Data

DataFrames are merged and cleaned to ensure accurate analysis. This includes concatenating, checking for duplicates, and handling missing values.

### EDA - Exploratory Data Analysis

We conduct initial exploration to understand the distributions and relationships in the data. This includes examining numerical and categorical variables, and preparing the data for further analysis.

### Hypothesis Testing - Completion Rate

We perform statistical tests to compare the completion rates between the Test and Control groups. This helps us understand if the changes implemented had a significant impact.

## Contributing

Interested in contributing? Great! Please fork the repository and open a pull request with your proposed changes.

## Credits

This analysis was conducted by [Your Name]. Special thanks to all the contributors who have invested time into improving the project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
