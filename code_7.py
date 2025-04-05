import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
#If any of this libraries is missing from your computer. Please install them using pip.

filename = 'Flight_Delays_2018.csv'
df = pd.read_csv(filename)

#ARR_DELAY is the column name that should be used as dependent variable (Y).


#####   Section 1: Heatmap 

corr_matrix = df.corr(numeric_only = True).round(2)

sns.heatmap(corr_matrix, annot = True)

plt.show()
input()

#####   Section 2: Regression




