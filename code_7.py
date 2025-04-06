import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as sm_api
#If any of this libraries is missing from your computer. Please install them using pip.

filename = 'Flight_Delays_2018.csv'
df = pd.read_csv(filename)

#ARR_DELAY is the column name that should be used as dependent variable (Y).


#####   Section 1

corr_matrix = df.corr(numeric_only = True).round(2)

sns.heatmap(corr_matrix, annot = True)

# plt.show()
# input()


#####   Section 2

# df.plot.scatter(x = 'DEP_DELAY', y = 'ARR_DELAY')
# df.plot.scatter(x = 'CARRIER_DELAY', y = 'ARR_DELAY')
# df.plot.scatter(x = 'WEATHER_DELAY', y = 'ARR_DELAY')
# df.plot.scatter(x = 'NAS_DELAY', y = 'ARR_DELAY')
# df.plot.scatter(x = 'LATE_AIRCRAFT_DELAY', y = 'ARR_DELAY')

# plt.show()


#####   Section 3

y = df['ARR_DELAY']
x = df['DEP_DELAY']
x1 = df['CARRIER_DELAY']
x2 = df['WEATHER_DELAY']
x3 = df['NAS_DELAY']
x4 = df['LATE_AIRCRAFT_DELAY']


x = sm.add_constant(x)
x1 = sm.add_constant(x1)
x2 = sm.add_constant(x2)
x3 = sm.add_constant(x3)
x4 = sm.add_constant(x4)

model = sm.OLS(y, x).fit()
model1 = sm.OLS(y, x1).fit()
model2 = sm.OLS(y, x2).fit()
model3 = sm.OLS(y, x3).fit()
model4 = sm.OLS(y, x4).fit()


# print(model.summary(), '\nMODEL 1')
# print(model1.summary(), '\nMODEL 2')
# print(model2.summary(), '\nMODEL 3')
# print(model3.summary(), '\nMODEL 4')
# print(model4.summary(), '\nMODEL 5')
