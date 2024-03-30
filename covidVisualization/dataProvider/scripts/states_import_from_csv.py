import pandas as pd
from ..models import States, Counties, FaceMasks
# Read the csv file
state_data = pd.read_csv('/root/projects/backend/us-states.csv')

# Insert the data into the database
for index, row in state_data.iterrows():
    state = States(
        date=row['date'],
        state=row['state'],
        fips=row['fips'],
        cases=row['cases'],
        deaths=row['deaths']
    )
    state.save()
