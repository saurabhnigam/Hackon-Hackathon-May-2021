Data cleansing code attempts.
In the end, the data was cleansed, but we were unable to automatically add parent IDs to each row in a way that made sense.
We opted for manual parent ID labelling. This was possible because the dataset was organized in a manageable way. 

Q: What is a parentID?
ParentID referring to the job in question's parent category, i.e.:
Job: "Chief Executive"
Parent Category: "Management, etc..."

The reason we needed this ParentID labelling is because we planned to recursively add new data to a job and its respective parent categories whenever a user input their job data.
