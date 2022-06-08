

s = 'this is my very long string that needs to be separated so it doesnt take too much column'

def add_char_every_certain_num_char_in_string(sentence):  #10 is good for excel
    sentence2 = sentence.split()
    words_length = 0
    word_index = 0
    for word in sentence2:
        length = len(word)
        words_length += length
        word_index += 1
        # print("WORDS LENGTH:",words_length)
        if words_length > 35:
            sentence2.insert(word_index, '\n')  
            words_length = 0 
        else:
            continue
    
    finished = ' '.join(sentence2) 
    # print(finished)
    return finished


new = add_char_every_certain_num_char_in_string(s)
print(new)








# assessment_list =  [{'visit_type': 'Assessment'}, 
# {'date_of_qa': '2022-05-26'}, 
# {'visit_date': '5/1/2022'}, 
# {'visit_type': 'None'}, 
# {'in_person': 'true'}, 
# {'recert': 'None'}, 
# {'staff_assigned': 'Sanjay Rajpara'},
#  {'covid_screen_yes': 'None'}, 


#  {'pt_report_pos': 'None'}, 



#  {'lose_taste_no': 'None'}, 
#  {'lose_taste_yes': 'None'}, 


#  {'addit_concerns_no': 'None'}, 
#  {'addit_concerns_yes': 'None'}, 
#  {'covid_followed': 'None'}, 
#  {'utilized_ppe': 'None'}, 
#  {'pt_verbal_pain': 'None'}, 
#  {'pt_uncomfortable_no': 'None'}, 
#  {'temp': ''}, {'pulse': ''}, 
#  {'resp': ''}, {'bp': ''}, 
#  {'weight': '125.0'}, 
#  {'mac': '22.0'}, 
#  {'o2_sat': ''}, 
#  {'ambulatory': 'None'},
#   {'ambu_max_assist': 'None'}, 
#   {'non_ambulatory': 'true'}, 
#   {'bedbound': 'None'}, 
#   {'non_ambu_max_assist': 'None'},
#    {'ambulation': '2'}, 
#    {'toileting': '3'}, 
#    {'transfer': '2'}, 
#    {'dressing': '3'}, 
#    {'feeding': '1'}, 
#    {'bathing': '3'}, 
#    {'primary_dx': 'Parkinson`s disease (G20)'}, 
#    {'primary_disease': 'HIV Disease'}, {'kps': '40'}, {'pps': '40'}, {'fast': '7-A'}, 
#    {'kps_less_70': 'None'}, 
#    {'pps_less_70': 'None'}, 
#    {'fast_greater_7a': 'None'}, 
#    {'unable_ambulate': 'None'}, 
#    {'unable_dress': 'None'}, 
#    {'unable_bath': 'None'}, 
#    {'urin_fec_incont': 'None'},
#     {'unable_speak_six': 'None'}, 
#     {'aspiration_pneu': 'None'}, 
#     {'pyenophritis': 'None'}, 
#     {'septicemia': 'None'}, 
#     {'decubitis': 'None'}, 
#     {'recurrent_fever': 'None'}, 
#     {'weight_loss': 'None'}, 
#     {'reported_hx': 'None'}, 
#     {'reported_pt': 'None'}, 
#     {'reported_pcg': 'None'}, 
#     {'hx_er': 'None'}, 
#     {'is_kps_pps_less_70': 'None'}, 
#     {'dependent_on_two_more_adl': 'None'}, 
#     {'copd_comorb': 'None'},
#      {'chf_comorb': 'None'}, 
#      {'ischemic_heart_comorb': 'None'},
#       {'diabetes_mellitus_comorb': 'None'},
#        {'neuro_comorb': 'None'}, 
#        {'renal_failure_comord': 'None'},
#         {'liver_comord': 'None'}, 
#         {'neoplasia_comord': 'None'}, 
#         {'aids_comord': 'None'}, 
#         {'dementia_comord': 'None'}, {'aids/hiv_comord': 'None'}, {'refractory_autoimmune_comord': 'None'}, {'lcd_specific_determination': ''}, {'lcd_other': ''}, {'ruled_out_renal_transplant': 'None'}, {'not_seeking_dialysis': 'None'}, {'currently_on_dialysis': 'None'}, {'dialysis_for_comfort': 'None'}, {'poor_prognosis_w_dialysis': 'None'}, {'is_creatinine_greater_than_8': 'None'}, {'uremia': 'None'}, {'oliguria': 'None'}, {'intractable_hyperkalemia_over_7': 'None'}, {'uremic_pericarditis': 'None'}, {'hepatorenal_syndrome': 'None'}, {'intractable_fluid_overload': 'None'}, {'gfr_less_10': 'None'}, 
#         {'peaceful': 'None'}, {'anxious': 'None'}, {'confused': 'None'}, {'angry': 'None'}, {'restless': 'None'}, {'agitated': 'None'}, {'depressed': 'None'}, {'seizure': 'None'}, {'combative': 'None'}, {'sundowning': 'None'},
#          {'tremors': 'None'}, {'other_symptoms': ''}, {'awake': 'None'}, {'alert': 'None'}, {'lethargic': 'None'}, {'min_responsive': 'None'}, 
#          {'coma': 'None'}, {'time_oriented': 'None'}, 
#          {'place_oriented': 'None'}, 
#       {'person_oriented': 'None'}, 
#       {'disoriented': 'None'}, 
#       {'no_psych_hx': 'None'}, {'bipolar_hx': 'None'}, {'ocd_hx': 'None'}, {'schizo_hx': 'None'}, 
#       {'depression_hx': 'None'}, {'speech_normal': 'None'}, {'aphasia': 'None'}, {'slurred_speech': 'None'}, {'other_speech': ''}, {'limited_six_words': ''},
#       {'blind': 'None'}, {'hard_hearing': 'None'}, {'normal_balance': 'None'}, {'balance_impaired': 'None'}, {'normal_bp': 'None'}, {'hypotension': 'None'}, 
#       {'hypertension': 'None'}, {'apical_regular': 'None'}, {'apical_irreg': 'None'}, {'apical_weak': 'None'}, {'apical_tachy': 'None'}, {'pedal_pulse_regular': 'None'}, {'pedal_pulse_irrigular': 'None'},
#       {'pedal_weak': 'None'}, {'pedal_tachy': 'None'},
#       {'pedal_brady': 'None'}, {'pedal_absent': 'None'}, {'radial_regular': 'None'}, 
#       {'radial_irregular': 'None'}, {'radial_weak': 'None'}, {'radial_tachy': 'None'}, {'radial_brady': 'None'}, {'radial_absent': 'None'}, {'femoral_regular': 'None'},
#        {'femoral_irregular': 'None'}, 
#       {'femoral_weak': 'None'}, 
#       {'femoral_tachy': 'None'},
#       {'femoral_brady': 'None'}, 
#       {'femoral_absent': 'None'}, 
#       {'cardiac_related_pain_yes': 'None'}, 
#       {'cardiac_related_pain_specify': ''}, 
#       {'edema_yes': 'None'},
#        {'edema_yes_specify': ''}, 
#        {'pitted_level_0': 'None'},
#         {'pitted_level_1': 'None'}, 
# {'pitted_level_2': 'None'}, 
# {'pitted_level_3': 'None'}, 
# {'pitted_level_4': 'None'}, 
# {'pitted_level_4_plus': 'None'}, 
# {'skin_normal': 'None'}, {'skin_pale': 'None'}, 
# {'skin_cyanotic': 'None'},
# {'skin_other': 'None'}, 
# {'skin_other_specify': ''}, 
# {'pacemaker': 'None'}, 
# {'sleep_overly_drowsy': 'None'}, {'sleep_insomnia': 'None'}, {'excessive_sleep': 'None'}, {'lack_of_sleep': 'None'}, {'satisfactory_sleep': 'None'}, {'sleep_duration': ''}, {'sleep_other_observations': ''}, 
# {'muscle_rigidity': 'None'}, {'rom_loss': 'None'}, 
# {'muscle_weakness': 'None'}, {'joint_swelling': 'None'}, {'muscle_spasms': 'None'}, 
# {'none_musculo_issues': 'None'}, 
# {'amputation': 'None'}, {'prostheses': 'None'}, {'contractures': 'None'}, 
# {'paraplegia': 'None'}, {'quadriplegia': 'None'}, {'hemiplegias': 'None'}, 
# {'right_hemiplegia': ''}, {'left_hemiplegia': ''}, {'hemiparesis': 'None'}, {'right_hemiparesis': ''}, {'left_hemiparesis': ''}, {'skin_cool': 'None'}, {'skin_warm': 'None'}, {'skin_dry': 'None'}, {'skin_diaphoretic': 'None'}, {'skin_jaundice': 'None'}, {'skin_mottling': 'None'}, {'skin_turgor_good': 'None'}, {'skin_turgor_fair': 'None'}, 
# {'skin_turgor_poor': 'None'}, {'wound_skin_impairment_no': 'None'}, {'wound_skin_impairment_yes': 'None'}, 

# {'sensory_completely_limited': 'true'}, {'sensory_very_limited': 'None'}, {'sensory_slightly_limited': 'None'}, 
# {'sensory_no_impairment': 'None'}, 
# {'skin_completely_moist': 'true'},
#  {'skin_very_moist': 'None'}, 
#  {'skin_occas_moist': 'None'}, 
#  {'skin_rarely_moist': 'None'}, 
#  {'bedfast': 'true'}, {'chairfast': 'None'},
#   {'walks_occasionally': 'None'},
#    {'walks_frequently': 'None'}, 
#    {'completely_immobile': 'true'}, 
#    {'very_limited_mobility': 'None'}, 
#    {'slightly_limited_mobility': 'None'}, 
#    {'no_mobility_limitations': 'None'}, 
#    {'very_poor_nutrition': 'true'},
#     {'probably_inadequate_nutrition': 'None'},
#      {'adequate_nutrition': 'None'},
# {'excellent_nutrition': 'None'},
# {'friction_problem': 'true'},
# {'friction_potential_problem': 'None'},
# {'friction_no_apparent_problem': 'None'},
# {'skin_other_observations': ''}, 
# {'decreased_loc': 'None'}, 
# {'decreased_bowel_bladder_function': 'None'}, 
# {'decreased_food_fluid_intake': 'None'}, {'increased_fatigue': 'None'}, 
# {'increased_respiratory_distress': 'None'},
#  {'imminently_dying_other': ''}, 
#  {'safety_assessment_completed_yes': 'None'},
#   {'safety_assessment_completed_no': 'None'}, 
#   {'fall_risk_assessment_completed_yes': 'None'},
#    {'fall_risk_completed_no': 'None'}, 
#    {'disaster_triage_1': 'None'}, 
#    {'disaster_triage_2': 'None'},
#     {'disaster_triage_3': 'None'},
#      {'if_level_1_confined_to_bed_chair_wc': 'None'}, 
#      {'if_level_1_dependent_on_walker_cane': 'None'}, 
#      {'if_level_1_lives_above_ground_floor': 'None'}, 
#      {'if_level_1_requires_electricity_for_medical_equipment': 'None'},
#       {'if_level_2_confined_to_wc': 'None'}, {'if_level_2_lives_above': 'None'}, {'if_level_2_dependent_walker': 'None'}, {'if_level_2_requires_electricity': 'None'}, {'if_level_3_lives_facility': 'None'}, {'if_level_3_has_place_to_go': 'None'}, {'need_for_hospice_aide_none': 'None'}, {'hospice_aide_grooming': 'None'}, {'aide_meal_prep': 'None'}, {'meed_for_volunteer_none': 'None'}, {'need_for_community_support_none': 'None'}, {'diagnosis_disease_teaching': 'None'}, {'medications_teaching': 'None'}, {'oxygen_teaching': 'None'}, {'dme_teaching': 'None'}, {'infection_control_teaching': 'None'}, {'safe_use_meds_teaching': 'None'}, {'other_teaching_box': 'None'}, {'other_teaching_txt': ''}, {'physical_comfort': 'None'}, {'structural_support': 'None'}, {'emotional_support': 'None'}, {'spiritual_support': 'None'}, {'safety_instructions': 'None'}, {'interpersonal_relationship': 'None'}, {'environmental_needs': 'None'}, {'self_determination': 'None'}, {'knowledge_related_needs': 'None'}, {'language_comm_needs': 'None'},
#        {'offered_psychosocial': 'None'}, {'offered_spiritual': 'None'}, {'offered_bereavement': 'None'}, {'offered_other': 'None'}, {'offered_other_txt': ''}, {'rapid_decline': 'None'}, {'saw_toothed_decline': 'None'}, {'slow_decline': 'None'},
# {'narrative_txt': ''}, 
# {'sign_submit_button': 'None'}]
