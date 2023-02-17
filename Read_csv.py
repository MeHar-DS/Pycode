import pandas as pd

# df = pd.read_csv('C:\\Users\\mervinh\PycharmProjects\\pythonProject\\patient_enrollments.csv',sep ='\t')
# df_youtube = pd.read_csv("C:\\Mervin\\Python Training\\archive\\topSubscribed.csv")
# df_ex = pd.read_excel()

# df.columns = [c.replace(' ', '_') for c in df.columns]
# lst_Date = df.Date_Key.unique().tolist()
# print(lst_Date)

#print(df_youtube.head())
#print(df.columns.values)
#print(df.head())

#Convert csv file to excel

df_csv_to_exc= pd.read_csv("C:\\Users\\mervinh\\PycharmProjects\\pythonProject\\venv\Files\\Covid Live.csv")
df_csv_to_exc.to_excel("C:\\Mervin\\Python Training\Covid.xlsx", index=False)

print(df_csv_to_exc)