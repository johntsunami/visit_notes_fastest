l = ['Visit', '2022-06-17', '6/6/2022', 'Michael Gray', 'SC', '[]', 'narrative_txtSC conducted routine visit with patient \n Eduardo. Patient was alert, awake, very responsive to \n visit. SC discussed patient`s safety as he has freedom \n to leave the B & C home when he wants. Patient stated that \n he likes to ride the bus throughout the day but knows where \n his home is and will always return. SC educated patient \n on safety issues and how important it is to stay in the house. \n Patient seemed to understand. SC also gave patient a Study \n Bible that he was very happy about. He enjoyed reading \n it and discussing. Also provided music and songs. SC prayed \n for patient`s protection. Patient was very happy for \n the visit. POC will continue with 1 x month visitation. \n', 'No selection on:pt_anxiety_sev\ncovid_screened_yes not selected.\nutilized_ppe not selected.\nphysical_comfort not selected.\nenvironmental_needs not selected.\nknowledge_related_needs not selected.']

for i in l:
    print(i)

# for i in range(10):
#     l.insert(-1, 'none')
 

def add_value_list(listname):
    print("LIST IS HERE +++++++++++++")
    print(listname)
    for i in range(10):   # THIS IS NEEDED TO PUT THE FINDINGS IN THE S COLUMN ON SHEET
            listname.insert(-1, 'none')



# print(l)



