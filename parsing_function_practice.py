from p1py import visit_list


# Cleans data and writes to excel
parse_findings = []
add_to_write_list = ['visit_date', 'date_of_qa', 'staff_assigned', 'discipline', 'temp','pulse','resp','bp','weight','mac','ambulation','toileting','trasfer','dressing','feeding','bathing']
write_list = []
problem_list = []
text_list = []

def parse_list(list_of_dicts):
    print("checking for blank rows")
    def append_blank_row(*row_values):
        
        # convert list of dict to one dict
        result_dict = {}
        for d in list_of_dicts:
            # print(d)
            result_dict.update(d)

        count_num = 0
        row_len = len(row_values)
        for row in row_values:

            for key, value in result_dict.items():
                if row == key:

                    if value == 'None':
                        count_num += 1
                        # print("added")
                        # print("count_num:", count_num)
                        if count_num == row_len:
                            parse_findings.append("No selection on:" + row)
    append_blank_row('covid_screen_yes', 'covid_screen_no')
    append_blank_row('pt_report_pos_no','pt_report_pos_yes')
    append_blank_row('pain_controlled_yes', 'pain_controlled_no', 'pain_controlled_n/a')
    append_blank_row('pt_anxiety_none', 'pt_anxiety_mild', 'pt_anxiety_mod', 'pt_anxiety_sev')
    append_blank_row('depression_none', 'depression_mild', 'depression_mod', 'depression_sev')
    append_blank_row('agitation_none', 'agitation_mild', 'agitation_mod', 'agitation_sev')
    append_blank_row('confusion_none', 'confusion_mild', 'confusion_mod', 'confusion_sev')
    append_blank_row('speech_impair_none', 'speech_impair_mild', 'speech_impair_mod', 'speech_impair_sev')
    append_blank_row('other_neuro_none','other_neuro_mild','other_neuro_mod','other_neuro_sev')
    append_blank_row('arrhythmia_none', 'arrhythmia_mild', 'arrhythmia_mod', 'arrhythmia_sev')
    append_blank_row('edema_none', 'edema_mild', 'edema_mod', 'edema_sev')
    append_blank_row('chest_pain_none', 'chest_pain_mild', 'chest_pain_mod', 'chest_pain_sev')
    append_blank_row('cardio_other_none', 'cardio_other_mild', 'cardio_other_mod', 'cardio_other_sev')
    append_blank_row('infection_none', 'infection_mild', 'infection_mod', 'infection_sev')
    append_blank_row('nausea_none', 'nausea_mild', 'nausea_mod', 'nausea_sev')
    append_blank_row('vomiting_none', 'vomiting_mild', 'vomiting_mod', 'vomiting_sev')
    append_blank_row('constipation_none', 'constipation_mild', 'constipation_mod', 'constipation_sev')
    append_blank_row('diarrhea_none', 'diarrhea_mild', 'diarrhea_mod', 'diarrhea_sev')
    append_blank_row('gastro_other_none', 'gastro_other_mild', 'gastro_other_mod', 'gastro_other_sev')
    append_blank_row('percent_intake_none', 'percent_intake_mild', 'percent_intake_mod', 'percent_intake_sev')
    append_blank_row('nutrition_other_none', 'nutrition_other_mild', 'nutrition_other_mod', 'nutrition_other_sev')
    append_blank_row('blood_sugar_none', 'blood_sugar_mild', 'blood_sugar_mod', 'blood_sugar_sev')
    append_blank_row('endocrine_other_none', 'endocrine_other_mild', 'endocrine_other_mod', 'endocrine_other_sev')
    append_blank_row('urinary_problem_none', 'urinary_problem_mild', 'urinary_problem_mod', 'urinary_problem_sev')
    append_blank_row('urinary_other_symptom_none', 'urinary_other_symptom_mild', 'urinary_other_symptom_mod', 'urinary_other_symptom_sev')
    append_blank_row('insomnia_none', 'insomnia_mild', 'insomnia_mod', 'insomnia_sev')
    append_blank_row('somnolence_none', 'somnolence_mild', 'somnolence_mod', 'somnolence_sev')
    append_blank_row('sleep_other_none', 'sleep_other_mild', 'sleep_other_mod', 'sleep_other_sev')
    append_blank_row('muskulo_weakness_none', 'muskulo_weakness_mild', 'muskulo_weakness_mod', 'muskulo_weakness_sev')
    append_blank_row('muskulo_contracture_none', 'muskulo_contracture_mild', 'muskulo_contracture_mod', 'muskulo_contracture_sev')
    append_blank_row('muskulo_other_none', 'muskulo_other_mild', 'muskulo_other_mod', 'muskulo_other_sev')
    append_blank_row('rash_none', 'rash_mild', 'rash_mod', 'rash_sev')
    append_blank_row('wound_none', 'wound_mild', 'wound_mod', 'wound_sev')
    append_blank_row('ulcer_none', 'ulcer_mild', 'ulcer_mod', 'ulcer_sev')
    append_blank_row('other_skin_none', 'other_skin_mild', 'other_skin_mod', 'other_skin_sev')
    append_blank_row('any_fall_yes','any_fall_no')
    append_blank_row('change_in_safety_yes','change_in_safety_no')
    append_blank_row('update_family_yes','update_family_no')
    append_blank_row('update_cm_yes','update_cm_no')
    append_blank_row('comfort_pack_yes','comfort_pack_no')
    append_blank_row('dme_inspected_yes','dme_inspected_faulty')
    append_blank_row('check_foley_yes','check_foley_no','check_foley_n/a')
    append_blank_row('check_gi_tube_no','check_gi_tube_yes','check_gi_tube_n/a')
    append_blank_row('confirmed_sched_yes','confirmed_sched_no')
    append_blank_row('bp_sit','bp_lying','bp_standing')
    append_blank_row('mac_left','mac_right')

    


    for dictionary in list_of_dicts:
        for key, val in dictionary.items():

            for word in add_to_write_list:
                if key == word:
                    write_list.append(val)

            def append_if_wrong(key_name, correct_value):

                if key == key_name:
                    # print(key_name, val)
                    if val == correct_value:
                        pass
                    else:
                        parse_findings.append(key + " not selected.")
            append_if_wrong('form_type', '--Select One--')
            append_if_wrong('covid_screened_yes', 'true')
            append_if_wrong('pt_report_pos_no', 'true')
            append_if_wrong('covid_followed', 'true')
            append_if_wrong('utilized_ppe', 'true')
            append_if_wrong('physical_comfort', 'true')
            append_if_wrong('emotional_support','true')
            append_if_wrong('safety_instructions', 'true')
            append_if_wrong('environmental_needs', 'true')
            append_if_wrong('knowledge_related_needs','true')
            
            

       
            #### IF ANY ARE UNSELECTED IT NOTIFIES
            if key == 'form_type':
                pass

            else: 
                if val == '--Select One--':
                    parse_findings.append(key + " unselected")
            

            def if_true_add_problem_list():
                true_list = ['language_comm_needs','check_foley_yes','dme_inspected_faulty','comfort_pack_need','update_cm_no','update_family_no','change_in_safety_yes','pt_report_pos_yes','lose_taste','addit_concerns','pain_controlled_no','pain_controlled_n/a','artificially_fed_peg','artificially_fed_ng','artificially_fed_jtube','artificially_fed_pump','artificially_fed_tpn','artificially_fed_specify','ambu_max_assist','non_ambulatory','bedbound','non_ambu_max_assist','any_fall_yes']
                if val == 'true':

                    if 'mild' in key:
                        problem_list.append(key)

                    elif 'mod' in key:
                        problem_list.append(key)

                    elif 'sev' in key:
                        problem_list.append(key)

                
                    for item in true_list:
                        if key == item:
                            problem_list.append(key)

            if_true_add_problem_list()

            def print_txt_other():
                if 'txt' in key:
                  
                    if val == '':
                        pass
                    else:
                        print("KEY",key,val)
                        text_list.append(key + val)

                elif 'obs' in key:
                    if val == '':
                        pass
                    else:

                        text_list.append(key + val)
            print_txt_other()

            def parse_vitals():
                vital_list = ['temp','pulse','resp','bp','mac']
            
                if key in vital_list:
                    if val == '':
                        parse_findings.append('key' + 'is blank')
                    else:
                        pass

                try:
                    if key == 'bp':
                    
                        bp = val
                        bp = bp.split("/")
                        print(bp)
                        bp[0] = int(bp[0])
                        print(bp[0])
                        print("here")
                        if bp[0] >= 140:  # 140/90 up hyper  90/60
                            blood_pressure = "hypertensive"
                            print("hyper bp")
                            problem_list.append("pt bp hyper" + val)
                        elif bp[0] <= 90:
                            blood_pressure = "hypotensive"
                            print('hypo bp')
                            problem_list.append("pt bp hypo" + val)
                        elif bp[0] < 140 and bp[0] > 90:
                            blood_pressure = "normal"

                            print('normal bp')
                        else:
                            print("BP NOT FOUND")
                    
                    if key == 'temp':
                        temp = float(val)

                        if temp < 96.5:
                            print('low temp')
                            problem_list.append('low temp '+ val)

                        elif temp > 99:
                            print('high temp')
                            problem_list.append('high temp '+ val)

                        else:
                            print('temp ok')
                    
                    if key == 'pulse':
                        pulse = int(val)

                        if pulse < 55:
                            problem_list.append("Bradycardia pulse " + val)

                        elif pulse > 105:
                            problem_list.append("Tachycardia pulse " + val)
                    if key == 'resp':
                        
                        resp = int(val)

                        if resp < 10:
                            problem_list.append("pt has bradypnea "+ val)
                        elif resp > 22:
                            problem_list.append("pt has tachypnea "+ val)

                except:
                    print("missing vital maybe? it passed it")
                 
    return parse_findings, write_list
parse_list(visit_list)

print("")
print("write_list: ", write_list)
print("")
print("parse_findings", parse_findings)
print("")
print("problem_list",problem_list)
print("")
print('text_list',text_list)
