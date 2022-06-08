from selenium_functions import login_hospice,find_soc,find_dx,check_missing_visits,gather_nurse_assessment_data,gather_visit_notes_data,get_idg_data
from datetime import datetime
from datetime import date, timedelta
startTime = datetime.now()
today = date.today()
today = str(today)

############################## BEGINNING############################ 
login_hospice()
soc = find_soc()  
diagnosis = find_dx()    
check_missing_visits(soc)  
assessment_list = gather_nurse_assessment_data()   
visit_notes_list = gather_visit_notes_data()
get_idg_data()

print("PROGRAM COMPLETED: NEED TO see how parsing does on RN then add parsing on idg and meds and poc.. ")
# Then go back to practice.py and impliment new functions and add more
print("TOTAL TIME:", datetime.now() - startTime)
























##########################################
########### NOTES TO FIX LATER ############

# have it search dicts based on the discipline of visit note to save tons of time


#### COLLECT COMP OR RECERT BASELINE ####
# GET DX , PROBLEMS,
### PUT BASELINE INFO IN SQL ###


# COLECT PHYSICIAN ORDERS

# COLLECT IDG


# COLLECT COMM LOG

# COLLECT VISIT NOTES
