# EXAMPLE
# line= """'pt_anxiety': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Anx1"]',"""


line= """'other_skin': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_OSY1"]',"""

def create_dicts(string):
    num = 0
    for i in range(4):
        num += 1
        semi= line.find(':')
        bracket = line.find("]")
        xp = line[semi:bracket]
        new_xp = xp[1:-2]
        # print(new_xp)

        # print(semi)
        variable = line[:semi-1]
        # print(variable)
        if num == 1:
            new_var = variable + "_none" + "'" + ":" + new_xp + '1"' + "]',"
        if num == 2:
            new_var = variable + "_mild" + "'" + ":" + new_xp + '2"' + "]',"

        if num == 3:
            new_var = variable + "_mod" + "'" + ":" + new_xp + '3"' + "]',"

        if num == 4:
            new_var = variable + "_sev" + "'" + ":" + new_xp + '4"' + "]',"

        print(new_var)
       
create_dicts(line)

 










# visit_list = [{'visit_date': '5/12/2022'},
#               {'visit_type': 'Visit'},
#               {'date_of_qa': '2022-05-23'},
#               {'in_person': 'None'},
#               {'form_type': '--Select One--'},
#               {'staff_assigned': 'Yamilet Suarez'},
#               {'discipline': 'LVN'},
#               {'care_level': 'RC'},
#               {'covid_screened_no': 'None'},
#               {'covid_screened_yes': 'true'},
#               {'pt_report_pos_no': 'true'},
#               {'pt_report_pos_yes': 'None'},
#               {'lose_taste': 'None'},
#               {'addit_concerns': 'true'},
#               {'covid_followed': 'true'},
#               {'utilized_ppe': 'true'},
#               {'pain_controlled_yes': 'true'},
#               {'pain_controlled_no': 'None'},
#               {'pain_controlled_n/a': 'None'},
#               {'pain_level_at_visit': '0'},
#               {'pain_other_observations': ''},
#               {'pt_anxiety_none': 'true'},
#               {'pt_anxiety_mild': 'None'},
#               {'pt_anxiety_mod': 'None'},
#               {'pt_anxiety_sev': 'None'},
#               {'pcg_anxiety_none': 'None'},
#               {'pcg_anxiety_mild': 'None'},
#               {'pcg_anxiety_mod': 'None'},
#               {'pcg_anxiety_sev': 'None'}, {'physical_comfort': 'true'}, {'structural_support': 'None'}, {'emotional_support': 'true'}, {'spiritual_support': 'None'}, {'safety_instructions': 'true'}, {'interpersonal_relationship': 'None'}, {'environmental_needs': 'true'}, {'self_determination': 'None'}, {'knowledge_related_needs': 'true'}, {'language_comm_needs': 'None'}, {'offered_psychosocial': 'None'}, {'offered_spiritual': 'None'}, {'offered_bereavement': 'None'}, {'offered_other': 'None'}, {'offered_other_txt': ''}, {'narrative_txt': 'Visit coordinated with patient`s daughter Linda , upon arrival at patient`s home , followed covid 19 guidelines . Directed to patient `s room who is lying down in bed , Patient denies pain at this time, verbalised of feeling weak, poor appetite . She requires moderate to extensive assistance with ADLs, ambulates very slow with walker. Patient is continent to bladder and bowel with bed side commode available. Reinforced education regarding fall/safety precaution, skin care, pain management, covid 19 preventive measures, proper uses of nebuliser treatment and DMEs ,encouraged daughter to call our 24 hours service number with any questions, concerns or changes in condition, Linda verbalised understanding. Left patient well palliated, comfortable under family care. POC collaborated with RNCM.'}]
# # 