from p1py import visit_list

print(visit_list)
# ## NOW ADJUST IT FOR THE SW @ PARSING



def parse_list_sw(list_of_dicts):
    add_to_write_list = ['visit_date', 'visit_type','date_of_qa', 'staff_assigned', 'discipline']
    parse_findings = []
    write_list = []
    problem_list = []
    text_list = []
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
                true_list = ['language_comm_needs','pt_report_pos_yes','pain_controlled_no','pain_controlled_n/a']
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
                        if val != 'None':
                            print("KEY",key,val)
                            text_list.append(key + val)
                        else:
                            pass

                elif 'obs' in key:
                    if val == '':
                        pass
                    else:

                        text_list.append(key + val)
            print_txt_other()

        
    write_list.append(problem_list)
    write_list.append(text_list)
    print("")
    print("write_list: ", write_list)
    print("")
    print("parse_findings", parse_findings)
    print("")
    print("problem_list",problem_list)
    print("")
    print('text_list',text_list)         
    return write_list

write_list =parse_list_sw(visit_list)

print("WRITE :",write_list)


