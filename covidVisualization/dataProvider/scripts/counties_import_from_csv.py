import pandas as pd
from ..models import States, Counties, FaceMasks
# Read the csv file
state_data = pd.read_csv('/root/projects/backend/us-counties.csv')
state_data = state_data.fillna(0)

count = 0
# Insert the data into the database
for index, row in state_data.iterrows():
    county = Counties(
        date=row['date'],
        county=row['county'],
        state=row['state'],
        fips=row['fips'],
        cases=row['cases'],
        deaths=row['deaths']
    )
    count += 1
    county.save()

    if count % 100 == 0:
        print(f"successfully saved {count} files")