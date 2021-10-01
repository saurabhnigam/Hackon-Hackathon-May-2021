#Adds new records & updates persistent Storage
#@100rabh.nigam
#Team Basketball

#This program stores records onto persistent storage & updates its parent categories
import pandas as pd


class RecordKeeper:


    def addRecord(df, gender, race, occupation_id, source):
        """
        Adds a new record onto df & stores df to csv
        """
        #Lookup to that SN
        occupation_df=df[df.SN==occupation_id]
        if(len(occupation_df) >= 1):
            #Update the record
            print(occupation_df)
            #Get Semaphore
            #lock.acquire()
            total_employed = occupation_df['TotalEmployed'].values[0]+1
            df.TotalEmployed[df.SN==occupation_id]=total_employed
            print('udpated')
            if(gender == 2): #women 2 men 1
                women_total=((occupation_df['Women'].values[0]/100)*total_employed )+1
                df.loc[df.SN==occupation_id, 'Women']= (women_total/total_employed)*100

            if(race == 3): #Asian3 
                asian_total=((occupation_df['Asian'].values[0]/100)*total_employed )+1
                df.loc[df.SN==occupation_id, 'Asian']= (asian_total/total_employed)*100
            elif(race == 2): #Black2
                asian_total=((occupation_df['BlackorAfricanAmerican'].values[0]/100)*total_employed )+1
                df.loc[df.SN==occupation_id, 'BlackorAfricanAmerican']= (asian_total/total_employed)*100
            elif(race == 1): #White 1
                asian_total=((occupation_df['White'].values[0]/100)*total_employed )+1
                df.loc[df.SN==occupation_id, 'White']= (asian_total/total_employed)*100
            #Write to csv
            df.to_csv(source, index = False)
            #lock.release()
            #Release
            
    def grade_calculation(occupation_id):
        occupation_df=df[df.SN==occupation_id]
        women_percent = occupation_df['Women'].values[0]
        parent_id= occupation_df['ParentId'].values[0]
        #df[df.SN==parent_id]


    #df = pd.read_csv("/home/impadmin/Saurabh/Projects/BasketBall/Corey/cpsaat11_2.csv")
    #print(df)

    #addRecord(df,2, 3,7)
