from scipy.stats import f_oneway
import pandas as pd
data = pd.read_excel("C:/Users/admin/Documents/data for reverse engineering.xlsx")
data.columns
f_oneway(data.survey_p1,data.survey_p2,data.survey_p3)
