import pandas as pd

df = pd.read_csv("data/adult.csv")

print(df["education"].unique())
# ['HS-grad' 'Some-college' '7th-8th' '10th' 'Doctorate' 'Prof-school'
#  'Bachelors' 'Masters' '11th' 'Assoc-acdm' 'Assoc-voc' '1st-4th' '5th-6th'
#  '12th' '9th' 'Preschool']
