from p1py import visit_list


# Cleans data and writes to excel
parse_findings = []
write_list = ['visit_date', 'date_of_qa', 'staff_assigned', 'discipline', ]


def parse_list(list_of_dicts):

    def append_blank_row(*row_values):
        # convert list of dict to one dict
        result_dict = {}
        for d in list_of_dicts:
            result_dict.update(d)

        count_num = 0
        row_len = len(row_values)
        for row in row_values:

            for key, value in result_dict.items():
                if row == key:

                    if value == 'None':
                        count_num += 1
                        print("added")
                        print("count_num:", count_num)
                        if count_num == row_len:
                            parse_findings.append("No selection on:" + row)
    append_blank_row('covid_screen_yes', 'covid_screen_no')

    for dictionary in list_of_dicts:
        for key, val in dictionary.items():

            for word in write_list:
                if key == word:
                    write_list.append(val)

            def append_if_wrong(key_name, correct_value):

                if key == key_name:
                    print(key_name, val)
                    if val == correct_value:
                        pass
                    else:
                        parse_findings.append(key + " not selected.")
            append_if_wrong('form_type', '--Select One--')
            append_if_wrong('covid_screened_yes', 'true')
            append_if_wrong('pt_report_pos_no', 'true')
            append_if_wrong('covid_followed', 'true')
            append_if_wrong('utilized_ppe', 'true')

            def append_unselected(keyname):
                if key == keyname:
                    if val == '--Select One--':
                        parse_findings.append(keyname + " unselected")
            append_unselected('care_level')

    return parse_findings, write_list


parse_list(visit_list)


print("write_list: ", write_list)
print("parse_findings", parse_findings)
