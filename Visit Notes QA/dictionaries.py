assessment_xp_dict = {
    'visit_date': '//*[@id="ctl00_ContentPlaceHolder1_txtHDate"]',
    # 'visit_type': '//*[@id="ctl00_ContentPlaceHolder1_LblHeader"]',
    'in_person': '//*[@id="ctl00_ContentPlaceHolder1_Assesscodeid_0"]',
    'discipline': '//*[@id="ctl00_ContentPlaceHolder1_DropDiscipline"]',
    # 'recert': '//*[@id="ctl00_ContentPlaceHolder1_AssessmentType_2"]',
    'staff_assigned': '//*[@id="ctl00_ContentPlaceHolder1_DropStaffAssigned"]',
    'covid_screen_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbPriorScreening_1"]',## NOT GETTING THESE but theyre accurate
    'covid_screen_no': '//*[@id="ctl00_ContentPlaceHolder1_rbPriorScreening_2"]',

    'pt_report_pos_no': '//*[@id="ctl00_ContentPlaceHolder1_rbPositive_0"]',## NOT GETTING THESE but theyre accurate
    'pt_report_pos_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbPositive_1"]',

    'lose_taste_no': '//*[@id="ctl00_ContentPlaceHolder1_rbCoronaVirus_0"]',## NOT GETTING THESE but theyre accurate
    'lose_taste_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbCoronaVirus_1"]',

    'addit_concerns_no': '//*[@id="ctl00_ContentPlaceHolder1_rbPatientPcgVisit_0"]',
    'addit_concerns_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbPositive_1"]',
    
    'covid_followed': '//*[@id="ctl00_ContentPlaceHolder1_chkCoronaInstructions"]',
    'utilized_ppe': '//*[@id="ctl00_ContentPlaceHolder1_chkPpe"]',

    ### Pain Screen ###
    'pt_verbal_pain': '//*[@id="ctl00_ContentPlaceHolder1_RD_PN_PAL_0"]',
    'pt_uncomfortable_no': '//*[@id="ctl00_ContentPlaceHolder1_RD_PN_UN_0"]',
    'pt_uncomfortable_yes':'//*[@id="ctl00_ContentPlaceHolder1_RD_PN_UN_1"]',

    ### VITALS ###
    'temp': '//*[@id="ctl00_ContentPlaceHolder1_Vital_temp"]',
    'pulse': '//*[@id="ctl00_ContentPlaceHolder1_Vital_Pulse"]',
    'resp': '//*[@id="ctl00_ContentPlaceHolder1_Vital_Resp"]',
    'bp': '//*[@id="ctl00_ContentPlaceHolder1_Vital_BP"]',
    'weight': '//*[@id="ctl00_ContentPlaceHolder1_Vital_Wt"]',
    'mac': '//*[@id="ctl00_ContentPlaceHolder1_Vital_Mac"]',
    'o2_sat': '//*[@id="ctl00_ContentPlaceHolder1_Vital_O2SAT"]',

    ### MOBILITY ###
    'ambulatory': '//*[@id="ctl00_ContentPlaceHolder1_RAD_CEMO_AN"]',
    'ambu_max_assist': '//*[@id="ctl00_ContentPlaceHolder1_Chk_CEMO_MX"]',

    'non_ambulatory': '//*[@id="ctl00_ContentPlaceHolder1_RAD_CEMO_AN1"]',
    'bedbound': '//*[@id="ctl00_ContentPlaceHolder1_ChK_CEMO_BB"]',
    'non_ambu_max_assist': '//*[@id="ctl00_ContentPlaceHolder1_Chk_CEMO_MXA"]',

    ### ADL ASSESSMENT ###
    'ambulation': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_A"]',
    'toileting': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_C"]',
    'transfer': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_T"]',
    'dressing': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_D"]',
    'feeding': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_F"]',
    'bathing': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_B"]',

    ### UPDATE CHANGE IN DIAGNOSIS ###
    'primary_dx': '//*[@id="ctl00_ContentPlaceHolder1_PrimaryDx"]',
    'primary_disease': '//*[@id="ctl00_ContentPlaceHolder1_DrpPDDisease0"]',

    ### KPS PPS FAST NYHA ###
    'kps': '//*[@id="ctl00_ContentPlaceHolder1_KPSList"]',
    'pps': '//*[@id="ctl00_ContentPlaceHolder1_PPSList"]',
    'fast': '//*[@id="ctl00_ContentPlaceHolder1_FASTList"]',

    ### NATURE # CONDITION OF TERMINAL ILLNESS /LCD Eligibility ###

    # DEMENTIA
    'kps_less_70': '//*[@id="ctl00_ContentPlaceHolder1_Dem_7"]',
    'pps_less_70': '//*[@id="ctl00_ContentPlaceHolder1_Dem_8"]',
    'fast_greater_7a': '//*[@id="ctl00_ContentPlaceHolder1_Dem_9"]',
    'unable_ambulate': '//*[@id="ctl00_ContentPlaceHolder1_Dem_10"]',
    'unable_dress': '//*[@id="ctl00_ContentPlaceHolder1_Dem_11"]',
    'unable_bath': '//*[@id="ctl00_ContentPlaceHolder1_Dem_12"]',


    'urin_fec_incont': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URCin"]',
    'unable_speak_six': '//*[@id="ctl00_ContentPlaceHolder1_Dem_14"]',
    'aspiration_pneu': '//*[@id="ctl00_ContentPlaceHolder1_NC_PDrp"]',
    'pyenophritis': '//*[@id="ctl00_ContentPlaceHolder1_Dem_16"]',
    'septicemia': '//*[@id="ctl00_ContentPlaceHolder1_NC_SDrp"]',
    'decubitis': '//*[@id="ctl00_ContentPlaceHolder1_NC_UDrp"]',
    'recurrent_fever': '//*[@id="ctl00_ContentPlaceHolder1_NC_RDrp"]',
    'weight_loss': '//*[@id="ctl00_ContentPlaceHolder1_NC_WDrp"]',

    # CANCER
    'reported_hx': '//*[@id="ctl00_ContentPlaceHolder1_NC_Chk1"]',
    'reported_pt': '//*[@id="ctl00_ContentPlaceHolder1_NC_Chk2"]',
    'reported_pcg': '//*[@id="ctl00_ContentPlaceHolder1_NC_Chk3"]',

    'hx_er': '//*[@id="ctl00_ContentPlaceHolder1_NC_HxDrp"]',
    'is_kps_pps_less_70': '//*[@id="ctl00_ContentPlaceHolder1_DRP_IF"]',
    'dependent_on_two_more_adl': '//*[@id="ctl00_ContentPlaceHolder1_DRP_DA"]',

    # comordities
    'copd_comorb': '//*[@id="ctl00_ContentPlaceHolder1_CHK_COPD"]',
    'chf_comorb': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CHF"]',
    'ischemic_heart_comorb': '//*[@id="ctl00_ContentPlaceHolder1_CHK_IHD"]',
    'diabetes_mellitus_comorb': '//*[@id="ctl00_ContentPlaceHolder1_CHK_DM"]',
    'neuro_comorb': '//*[@id="ctl00_ContentPlaceHolder1_CHK_N"]',
    'renal_failure_comord': '//*[@id="ctl00_ContentPlaceHolder1_CHK_RF"]',
    'liver_comord': '//*[@id="ctl00_ContentPlaceHolder1_CHK_LD"]',
    'neoplasia_comord': '//*[@id="ctl00_ContentPlaceHolder1_CHK_NE"]',
    'aids_comord': '//*[@id="ctl00_ContentPlaceHolder1_CHK_A"]',
    'dementia_comord': '//*[@id="ctl00_ContentPlaceHolder1_CHK_D"]',
    'aids/hiv_comord': '//*[@id="ctl00_ContentPlaceHolder1_CHK_AV"]',
    'refractory_autoimmune_comord': '//*[@id="ctl00_ContentPlaceHolder1_CHK_RSA"]',
    'lcd_specific_determination': '//*[@id="ctl00_ContentPlaceHolder1_NC_PDDrp"]',
    'lcd_other': '//*[@id="ctl00_ContentPlaceHolder1_TXT_NA_IL"]',

    # RENAL LCD
    'ruled_out_renal_transplant': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_RT"]',
    'not_seeking_dialysis': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_DD"]',
    'currently_on_dialysis': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_CD"]',
    'dialysis_for_comfort': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_CO"]',
    'poor_prognosis_w_dialysis': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_UD"]',
    'is_creatinine_greater_than_8': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_CC"]',
    'uremia': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_U"]',
    'oliguria': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_O"]',
    'intractable_hyperkalemia_over_7': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_HG"]',
    'uremic_pericarditis': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_UP"]',
    'hepatorenal_syndrome': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_HS"]',
    'intractable_fluid_overload': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_IFO"]',
    'gfr_less_10': '//*[@id="ctl00_ContentPlaceHolder1_CRNDL_GFR"]',


    # ADD ALL OTHER DISEASE NATURE AND CONDITION IF ASSESSING RECERTS AND ASSESSMENTS





    ### BODY SYSTEM ###
                           ## SYMPTOMS ##
    'peaceful': '//*[@id="ctl00_ContentPlaceHolder1_Nue_DEMpe"]',
    'anxious': '//*[@id="ctl00_ContentPlaceHolder1_Nue_DEMan"]',
    'confused': '//*[@id="ctl00_ContentPlaceHolder1_Nue_DEMco"]',
    'angry': '//*[@id="ctl00_ContentPlaceHolder1_Nue_DEMag"]',
    'restless': '//*[@id="ctl00_ContentPlaceHolder1_Nue_DEMre"]',
    'agitated': '//*[@id="ctl00_ContentPlaceHolder1_Nue_DEMat"]',
    'depressed': '//*[@id="ctl00_ContentPlaceHolder1_Nue_DEMot"]',
    'seizure': '//*[@id="ctl00_ContentPlaceHolder1_Nue_OTHse"]',
    'combative': '//*[@id="ctl00_ContentPlaceHolder1_Nue_OTHco"]',
    'sundowning': '//*[@id="ctl00_ContentPlaceHolder1_Nue_OTHsu"]',
    'tremors': '//*[@id="ctl00_ContentPlaceHolder1_Nue_OTHtr"]',
    'other_symptoms': '//*[@id="ctl00_ContentPlaceHolder1_Nue_OTHotText"]',

    # LEVEL OF CONSCIOUSNESS:
    'awake': '//*[@id="ctl00_ContentPlaceHolder1_Nue_LOCaw"]',
    'alert': '//*[@id="ctl00_ContentPlaceHolder1_Nue_LOCal"]',
    'lethargic': '//*[@id="ctl00_ContentPlaceHolder1_Nue_LOCle"]',
    'min_responsive': '//*[@id="ctl00_ContentPlaceHolder1_Nue_LOCmr"]',
    'coma': '//*[@id="ctl00_ContentPlaceHolder1_Nue_LOCco"]',

    ### ORIENTED TO ###
    'time_oriented': '//*[@id="ctl00_ContentPlaceHolder1_Nue_ORTtm"]',
    'place_oriented': '//*[@id="ctl00_ContentPlaceHolder1_Nue_ORTpl"]',
    'person_oriented': '//*[@id="ctl00_ContentPlaceHolder1_Nue_ORTpr"]',
    'disoriented': '//*[@id="ctl00_ContentPlaceHolder1_Nue_ORTds"]',

                ### PSYCH HX ###
    'no_psych_hx': '//*[@id="ctl00_ContentPlaceHolder1_Nue_PHXno"]',
    'bipolar_hx': '//*[@id="ctl00_ContentPlaceHolder1_Nue_PHXbi"]',
    'ocd_hx': '//*[@id="ctl00_ContentPlaceHolder1_Nue_PHXoc"]',
    'schizo_hx': '//*[@id="ctl00_ContentPlaceHolder1_Nue_PHXsc"]',
    'depression_hx': '//*[@id="ctl00_ContentPlaceHolder1_Nue_PHXde"]',

                ### Communication voice speech ###
    'speech_normal': '//*[@id="ctl00_ContentPlaceHolder1_Nue_CVPno"]',
    'aphasia': '//*[@id="ctl00_ContentPlaceHolder1_Nue_CVPap"]',
    'slurred_speech': '//*[@id="ctl00_ContentPlaceHolder1_Nue_CVPsl"]',
    'other_speech': '//*[@id="ctl00_ContentPlaceHolder1_Nue_CVPotText"]',
    'limited_six_words': '//*[@id="ctl00_ContentPlaceHolder1_Nue_SS"]',

                ## SENSORY DEFICIT ##
    'blind': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CE_BD"]',
    'hard_hearing': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CE_HH"]',

                ## BALANCE ##
    'normal_balance': '//*[@id="ctl00_ContentPlaceHolder1_Nue_Balni_0"]',
    'balance_impaired': '//*[@id="ctl00_ContentPlaceHolder1_Nue_Balni_1"]',

    ### CARDIOVASCULAR ###
    'normal_bp': '//*[@id="ctl00_ContentPlaceHolder1_BPLevel_0"]',
    'hypotension': '//*[@id="ctl00_ContentPlaceHolder1_BPLevel_1"]',
    'hypertension': '//*[@id="ctl00_ContentPlaceHolder1_BPLevel_2"]',

    #Pulse#
    'apical_regular': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULar"]',
    'apical_irreg': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULai"]',
    'apical_weak': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULaw"]',
    'apical_tachy': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULat"]',

    'pedal_pulse_regular': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULpr"]',
    'pedal_pulse_irrigular': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULpi"]',
    'pedal_weak': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULpw"]',
    'pedal_tachy': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULpt"]',
    'pedal_brady': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULpb"]',
    'pedal_absent': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULps"]',

    'radial_regular': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULrr"]',
    'radial_irregular': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULr"]',
    'radial_weak': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULrw"]',
    'radial_tachy': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULrt"]',
    'radial_brady': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULrb"]',
    'radial_absent': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULrs"]',

    'femoral_regular': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULfr"]',
    'femoral_irregular': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULfi"]',
    'femoral_weak': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULfw"]',
    'femoral_tachy': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULft"]',
    'femoral_brady': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULfb"]',
    'femoral_absent': '//*[@id="ctl00_ContentPlaceHolder1_Car_PULfs"]',

    # CARDIAC RELATED PAIN
    'cardiac_related_pain_yes': '//*[@id="ctl00_ContentPlaceHolder1_Car_Carsp_1"]',
    'cardiac_related_pain_specify': '//*[@id="ctl00_ContentPlaceHolder1_Car_CarspText"]',

    'edema_yes': '//*[@id="ctl00_ContentPlaceHolder1_Car_Caresp_1"]',
    'edema_yes_specify': '//*[@id="ctl00_ContentPlaceHolder1_Car_CarespText"]',

    'pitted_level_0': '//*[@id="ctl00_ContentPlaceHolder1_Car_Carept_0"]',
    'pitted_level_1': '//*[@id="ctl00_ContentPlaceHolder1_Car_Carept_1"]',
    'pitted_level_2': '//*[@id="ctl00_ContentPlaceHolder1_Car_Carept_2"]',
    'pitted_level_3': '//*[@id="ctl00_ContentPlaceHolder1_Car_Carept_3"]',
    'pitted_level_4': '//*[@id="ctl00_ContentPlaceHolder1_Car_Carept_4"]',
    'pitted_level_4_plus': '//*[@id="ctl00_ContentPlaceHolder1_Car_Carept_5"]',

    # SKIN COLOR
    'skin_normal': '//*[@id="ctl00_ContentPlaceHolder1_Car_SKNco_0"]',
    'skin_pale': '//*[@id="ctl00_ContentPlaceHolder1_Car_SKNco_1"]',
    'skin_cyanotic': '//*[@id="ctl00_ContentPlaceHolder1_Car_SKNco_2"]',
    'skin_other': '//*[@id="ctl00_ContentPlaceHolder1_Car_SKNco_3"]',
    'skin_other_specify': '//*[@id="ctl00_ContentPlaceHolder1_Car_SKNcoText"]',

    # OTHER CARDIO FACTORS

    'pacemaker': '//*[@id="ctl00_ContentPlaceHolder1_Car_OFCpm"]',
    'defibrillator': '//*[@id="ctl00_ContentPlaceHolder1_Car_OFCid"]',
    'jvd': '//*[@id="ctl00_ContentPlaceHolder1_Car_OFCjv"]',
    'varicose': '//*[@id="ctl00_ContentPlaceHolder1_Car_OFCva"]',
    'central_venous_line': '//*[@id="ctl00_ContentPlaceHolder1_Car_OFCcv"]',
    'extremeties_cool': '//*[@id="ctl00_ContentPlaceHolder1_Car_OFCec"]',
    'stasis_ulcer': '//*[@id="ctl00_ContentPlaceHolder1_Car_OFCsu"]',
    'other_cardiac_observations': '//*[@id="ctl00_ContentPlaceHolder1_OO_Car"]',

    ### RESPIRATORY ###

    'dyspnea_none': '//*[@id="ctl00_ContentPlaceHolder1_Car_DYS_0"]',
    'dyspnea_mild': '//*[@id="ctl00_ContentPlaceHolder1_Car_DYS_1"]',
    'dyspnea_mod': '//*[@id="ctl00_ContentPlaceHolder1_Car_DYS_2"]',
    'dyspnea_sev': '//*[@id="ctl00_ContentPlaceHolder1_Car_DYS_3"]',
    'HIS_even_though_sob': '//*[@id="ctl00_ContentPlaceHolder1_SOBDDP"]',

    'exertion_level_rest': '//*[@id="ctl00_ContentPlaceHolder1_Car_AEL_0"]',
    'exertion_level_mild_exert': '//*[@id="ctl00_ContentPlaceHolder1_Car_AEL_1"]',
    'exertion_level_w_speech': '//*[@id="ctl00_ContentPlaceHolder1_Car_AEL_2"]',
    'exertion_level_push_of_speech': '//*[@id="ctl00_ContentPlaceHolder1_Car_AEL_3"]',
    'exertion_level_pursed_lip': '//*[@id="ctl00_ContentPlaceHolder1_Car_AEL_4"]',
    'exertion_level_other_specify': '//*[@id="ctl00_ContentPlaceHolder1_Car_AELText"]',

    ## LUNGS SOUNDS ##
    'lungs_clear': '//*[@id="ctl00_ContentPlaceHolder1_Car_LUScl"]',
    'lungs_a_diminished': '//*[@id="ctl00_ContentPlaceHolder1_Car_LUSad"]',
    'lungs_b_wheeze': '//*[@id="ctl00_ContentPlaceHolder1_Car_LUSbw"]',
    'lungs_d_rales': '//*[@id="ctl00_ContentPlaceHolder1_Car_LUSdr"]',
    'lungs_e_rhonchi': '//*[@id="ctl00_ContentPlaceHolder1_Car_LUSer"]',

    'resp_normal': '//*[@id="ctl00_ContentPlaceHolder1_Car_RESnm"]',
    'resp_labored': '//*[@id="ctl00_ContentPlaceHolder1_Car_RESlb"]',
    'resp_agonal': '//*[@id="ctl00_ContentPlaceHolder1_Car_RESag"]',
    'resp_tachy': '//*[@id="ctl00_ContentPlaceHolder1_Car_RESta"]',
    'resp_brady': '//*[@id="ctl00_ContentPlaceHolder1_Car_RESbd"]',
    'resp_cheyenne': '//*[@id="ctl00_ContentPlaceHolder1_Car_REScs"]',
    'resp_orthopnea': '//*[@id="ctl00_ContentPlaceHolder1_Car_RESot"]',

    'cough_none': '//*[@id="ctl00_ContentPlaceHolder1_Car_CGHno"]',
    'cough_dry_nonproductive': '//*[@id="ctl00_ContentPlaceHolder1_Car_CGHdp"]',
    'cough_productive': '//*[@id="ctl00_ContentPlaceHolder1_Car_CGHhm"]',
    'cough_hemoptysis': '//*[@id="ctl00_ContentPlaceHolder1_Car_CGHhm"]',
    'cough_barrel_chest': '//*[@id="ctl00_ContentPlaceHolder1_Car_CGHbc"]',
    'cough_sputum': '//*[@id="ctl00_ContentPlaceHolder1_Car_CGHsp"]',
    'cough_specify_color': '//*[@id="ctl00_ContentPlaceHolder1_Car_CGHspText"]',

    'is_pt_on_o2_yes': '//*[@id="ctl00_ContentPlaceHolder1_Car_PO2_1"]',
    'is_pt_immunosuppressed': '//*[@id="ctl00_ContentPlaceHolder1_Imm_IMP_1"]',

    'current_resistant_infection_none': '//*[@id="ctl00_ContentPlaceHolder1_Imm_CASno"]',
    'mrsa': '//*[@id="ctl00_ContentPlaceHolder1_Imm_CASmr"]',
    'c_diff': '//*[@id="ctl00_ContentPlaceHolder1_Imm_CAScd"]',
    'other_antibiotic_resistant_infection': '//*[@id="ctl00_ContentPlaceHolder1_Imm_CASot"]',

    "current_inf_none": '//*[@id="ctl00_ContentPlaceHolder1_Imm_CAIno"]',
    'current_inf_sepsis': '//*[@id="ctl00_ContentPlaceHolder1_Imm_CAIsp"]',
    'uti': '//*[@id="ctl00_ContentPlaceHolder1_Imm_CAIut"]',
    'respiratory_infection': '//*[@id="ctl00_ContentPlaceHolder1_Imm_CAIrt"]',
    'iv_infection': '//*[@id="ctl00_ContentPlaceHolder1_Imm_CAIiv"]',
    'wound_infection': '//*[@id="ctl00_ContentPlaceHolder1_Imm_CAIwn"]',
    'hiv': '//*[@id="ctl00_ContentPlaceHolder1_Imm_CAIhv"]',
    'pressure_area': '//*[@id="ctl00_ContentPlaceHolder1_Imm_CAIpr"]',
    'other_active_infection': '//*[@id="ctl00_ContentPlaceHolder1_Imm_CAIot"]',
    'other_immunological': '//*[@id="ctl00_ContentPlaceHolder1_OO_Imm"]',

    ### GASTRO ###
    'nausea_none': '//*[@id="ctl00_ContentPlaceHolder1_Gas_NAU_0"]',
    'nausea_yes': '//*[@id="ctl00_ContentPlaceHolder1_Gas_NAU_1"]',

    'vomitting_none': '//*[@id="ctl00_ContentPlaceHolder1_Gas_VOM_0"]',
    'vomit_yes': '//*[@id="ctl00_ContentPlaceHolder1_Gas_VOM_1"]',
    'vomit_x_24hr': '//*[@id="ctl00_ContentPlaceHolder1_Gas_VOMhr"]',
    'vomit_comment': '//*[@id="ctl00_ContentPlaceHolder1_Gas_VOMhrText"]',

    'abd_soft': '//*[@id="ctl00_ContentPlaceHolder1_Gas_ABDso"]',
    'abd_firm': '//*[@id="ctl00_ContentPlaceHolder1_Gas_ABDfm"]',
    'abd_tympanic': '//*[@id="ctl00_ContentPlaceHolder1_Gas_ABDty"]',
    'abd_tender': '//*[@id="ctl00_ContentPlaceHolder1_Gas_ABDte"]',
    'abd_nontender': '//*[@id="ctl00_ContentPlaceHolder1_Gas_ABDnt"]',
    'abd_ascites': '//*[@id="ctl00_ContentPlaceHolder1_Gas_ABDag"]',
    'abd_cm': '//*[@id="ctl00_ContentPlaceHolder1_Gas_ABDText"]',

    ## BOWEL ##
    'bowel_sound_normal': '//*[@id="ctl00_ContentPlaceHolder1_Gas_SND_0"]',
    'bowel_hyper': '//*[@id="ctl00_ContentPlaceHolder1_Gas_SND_1"]',
    'bowel_hypo': '//*[@id="ctl00_ContentPlaceHolder1_Gas_SND_2"]',
    'bowel_absent': '//*[@id="ctl00_ContentPlaceHolder1_Gas_SND_3"]',

    'stool_normal': '//*[@id="ctl00_ContentPlaceHolder1_Gas_SND_0"]',
    'stool_bloody': '//*[@id="ctl00_ContentPlaceHolder1_Gas_STLbl"]',
    'colostomy': '//*[@id="ctl00_ContentPlaceHolder1_Gas_STLcl"]',
    'ileostomy': '//*[@id="ctl00_ContentPlaceHolder1_Gas_STLil"]',

    'diarrhea': '//*[@id="ctl00_ContentPlaceHolder1_Gas_BWMdi"]',
    'constipation': '//*[@id="ctl00_ContentPlaceHolder1_Gas_BWMco"]',
    'impaction': '//*[@id="ctl00_ContentPlaceHolder1_Gas_BWMim"]',

    'continent': '//*[@id="ctl00_ContentPlaceHolder1_Gas_STS_0"]',
    'incontinent': '//*[@id="ctl00_ContentPlaceHolder1_Gas_STS_1"]',
    'bowel_bladder_program': '//*[@id="ctl00_ContentPlaceHolder1_Gas_STS_2"]',
    'bm_frequency': '//*[@id="ctl00_ContentPlaceHolder1_Gas_FRQ"]',
    'last_bm': '//*[@id="ctl00_ContentPlaceHolder1_Gas_LBM"]',
    'HIS_even_though_opiods_prescribed': '//*[@id="ctl00_ContentPlaceHolder1_ChkBRI"]',

    ### NUTRITION ###

    'weight_loss_greater_than_10%': '//*[@id="ctl00_ContentPlaceHolder1_GAS_RWL"]',
    'appetite_good': '//*[@id="ctl00_ContentPlaceHolder1_Gas_APPgd"]',
    'appetite_fair': '//*[@id="ctl00_ContentPlaceHolder1_Gas_APPfr"]',
    'appetite_poor': '//*[@id="ctl00_ContentPlaceHolder1_Gas_APPpr"]',
    'anorexia': '//*[@id="ctl00_ContentPlaceHolder1_Gas_APPan"]',
    'cachexia': '//*[@id="ctl00_ContentPlaceHolder1_Gas_APPca"]',
    'npo': '//*[@id="ctl00_ContentPlaceHolder1_CheckBox174"]',


    'hiccoughs': '//*[@id="ctl00_ContentPlaceHolder1_Gas_SWLhi"]',
    'dysphagia': '//*[@id="ctl00_ContentPlaceHolder1_Gas_SWLdy"]',
    'aspiration_precautions': '//*[@id="ctl00_ContentPlaceHolder1_Gas_SWLas"]',
    'hx_of_aspirations': '//*[@id="ctl00_ContentPlaceHolder1_Gas_SWLhx"]',
    'choking_on_liquids': '//*[@id="ctl00_ContentPlaceHolder1_Gas_SWLch"]',
    'hydration_inadequate': '//*[@id="ctl00_ContentPlaceHolder1_Gas_HYDin"]',
    'membranes_dry': '//*[@id="ctl00_ContentPlaceHolder1_Gas_HYDmm"]',
    'poor_skin_turgor': '//*[@id="ctl00_ContentPlaceHolder1_Gas_HYDps"]',
    'iv_fluids': '//*[@id="ctl00_ContentPlaceHolder1_Gas_HYDiv"]',

    'diet_no_concern': '//*[@id="ctl00_ContentPlaceHolder1_Gas_IND_0"]',
    'diet_pt_concerns': '//*[@id="ctl00_ContentPlaceHolder1_Gas_IND_1"]',
    'diet_pcg_concerns': '//*[@id="ctl00_ContentPlaceHolder1_Gas_IND_2"]',

    'artificially_fed_no': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_0"]',
    'peg_tube': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_1"]',
    'ng_tube': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_2"]',
    'j_tube': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_3"]',
    'feeding_pump': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_4"]',
    'tpn': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_5"]',
    'artificially_fed_specify': '//*[@id="ctl00_ContentPlaceHolder1_Gas_IFTText"]',

    'diet': '//*[@id="ctl00_ContentPlaceHolder1_DrpDietType"]',
    'normal_oral_cavity': '//*[@id="ctl00_ContentPlaceHolder1_Gas_ORCnm"]',
    'toothless': '//*[@id="ctl00_ContentPlaceHolder1_Gas_ORCto"]',
    'stomatitis': '//*[@id="ctl00_ContentPlaceHolder1_Gas_ORCst"]',
    'thrush': '//*[@id="ctl00_ContentPlaceHolder1_Gas_ORCth"]',
    'poor_dentition': '//*[@id="ctl00_ContentPlaceHolder1_Gas_ORCpo"]',

    'dentures_none': '//*[@id="ctl00_ContentPlaceHolder1_Gas_DENno"]',
    'dentures_upper': '//*[@id="ctl00_ContentPlaceHolder1_Gas_DENup"]',
    'dentures_lower': '//*[@id="ctl00_ContentPlaceHolder1_Gas_DENlo"]',

    'dentures_other': '//*[@id="ctl00_ContentPlaceHolder1_Gas_DENotText"]',
    'oral_other_observ': '//*[@id="ctl00_ContentPlaceHolder1_OO_Nut"]',

    ### ENDOCRINE ###

    'thyroid_impairment': '//*[@id="ctl00_ContentPlaceHolder1_End_IMPty"]',
    'parathyroid_impairment': '//*[@id="ctl00_ContentPlaceHolder1_End_IMPpa"]',
    'pituitary_impairment': '//*[@id="ctl00_ContentPlaceHolder1_End_IMPpi"]',
    'adrenal_impairment': '//*[@id="ctl00_ContentPlaceHolder1_End_IMPad"]',
    'pancreas_impairment': '//*[@id="ctl00_ContentPlaceHolder1_End_IMPpn"]',

    'iddm': '//*[@id="ctl00_ContentPlaceHolder1_End_DBL_0"]',
    'niddm': '//*[@id="ctl00_ContentPlaceHolder1_End_DBL_1"]',
    'diabetes_other': '//*[@id="ctl00_ContentPlaceHolder1_OO_End"]',

    # GENITOURINARY
    'urinary_continent': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URCco"]',
    'urine_incontinent': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URCin"]',
    'bladder_program': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URCbp"]',
    'urostomy': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URCur"]',
    'retention': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URCre"]',
    'painful_urine': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URCpa"]',
    'nocturia': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URCnc"]',

    'clear_urine': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URNcl"]',
    'cloudy_urine': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URNcd"]',
    'pale_urine': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URNpa"]',
    'urine_color_checkbox': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URNco"]',
    'urine_color_textbox': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URNcoText"]',
    'blood_urine': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URNcoText"]',
    'odor_urine': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URNod"]',

    'catheter_none': '//*[@id="ctl00_ContentPlaceHolder1_Gen_CATno"]',
    'catheter_foley': '//*[@id="ctl00_ContentPlaceHolder1_Gen_CATfo"]',
    'condom_cath': '//*[@id="ctl00_ContentPlaceHolder1_Gen_CATco"]',
    'suprapubic': '//*[@id="ctl00_ContentPlaceHolder1_Gen_CATsu"]',
    'urostomy': '//*[@id="ctl00_ContentPlaceHolder1_Gen_CATus"]',
    'foley_size': '//*[@id="ctl00_ContentPlaceHolder1_Gen_FSU"]',
    'foley_date_changed': '//*[@id="ctl00_ContentPlaceHolder1_Gen_FSUlc"]',
    'irrigation_solution': '//*[@id="ctl00_ContentPlaceHolder1_Gen_FSUst"]',
    'irrigation_frequency': '//*[@id="ctl00_ContentPlaceHolder1_Gen_FSUfr"]',
    'irrigation_duration': '//*[@id="ctl00_ContentPlaceHolder1_Gen_FSUdu"]',

    # SLEEP REST #
    'sleep_pattern_none': '//*[@id="ctl00_ContentPlaceHolder1_Slp_PAT_0"]',
    'sleep_overly_drowsy': '//*[@id="ctl00_ContentPlaceHolder1_Slp_PAT_1"]',
    'sleep_insomnia': '//*[@id="ctl00_ContentPlaceHolder1_Slp_PAT_2"]',
    'excessive_sleep': '//*[@id="ctl00_ContentPlaceHolder1_Slp_PAT_3"]',
    'lack_of_sleep': '//*[@id="ctl00_ContentPlaceHolder1_Slp_PAT_4"]',
    'satisfactory_sleep': '//*[@id="ctl00_ContentPlaceHolder1_Slp_PAT_5"]',

    'sleep_duration': '//*[@id="ctl00_ContentPlaceHolder1_Slp_DURhr"]',
    'sleep_other_observations': '//*[@id="ctl00_ContentPlaceHolder1_OO_Slp"]',

    ### MUSKULOSKELETAL ###
    # ISSUES NOTED:

    'muscle_rigidity': '//*[@id="ctl00_ContentPlaceHolder1_Mus_ISSar"]',
    'rom_loss': '//*[@id="ctl00_ContentPlaceHolder1_Mus_ISSbr"]',
    'muscle_weakness': '//*[@id="ctl00_ContentPlaceHolder1_Mus_ISScw"]',
    'joint_swelling': '//*[@id="ctl00_ContentPlaceHolder1_Mus_ISSdj"]',
    'muscle_spasms': '//*[@id="ctl00_ContentPlaceHolder1_Mus_ISSes"]',
    'none_musculo_issues': '//*[@id="ctl00_ContentPlaceHolder1_Mus_ISSno"]',
    'amputation': '//*[@id="ctl00_ContentPlaceHolder1_Mus_ISSfa"]',
    'prostheses': '//*[@id="ctl00_ContentPlaceHolder1_Mus_ISSgp"]',
    'contractures': '//*[@id="ctl00_ContentPlaceHolder1_Mus_ISShc"]',

    # DISABILITY
    'paraplegia': '//*[@id="ctl00_ContentPlaceHolder1_Mus_DIBpl"]',
    'quadriplegia': '//*[@id="ctl00_ContentPlaceHolder1_Mus_DIBqd"]',
    'hemiplegias': '//*[@id="ctl00_ContentPlaceHolder1_Mus_DIBhm"]',
    'right_hemiplegia': '//*[@id="ctl00_ContentPlaceHolder1_Mus_DIBhmRt"]',
    'left_hemiplegia': '//*[@id="ctl00_ContentPlaceHolder1_Mus_DIBhmLt"]',
    'hemiparesis': '//*[@id="ctl00_ContentPlaceHolder1_Mus_DIBhp"]',
    'right_hemiparesis': '//*[@id="ctl00_ContentPlaceHolder1_Mus_DIBhpRt"]',
    'left_hemiparesis': '//*[@id="ctl00_ContentPlaceHolder1_Mus_DIBHplt"]',

    ### INTEGUMENTARY ###
    'skin_normal': '//*[@id="ctl00_ContentPlaceHolder1_Int_SKSnm"]',
    'skin_cool': '//*[@id="ctl00_ContentPlaceHolder1_Int_SKSco"]',
    'skin_warm': '//*[@id="ctl00_ContentPlaceHolder1_Int_SKSwm"]',
    'skin_dry': '//*[@id="ctl00_ContentPlaceHolder1_Int_SKSdr"]',
    'skin_diaphoretic': '//*[@id="ctl00_ContentPlaceHolder1_Int_SKSdi"]',
    'skin_jaundice': '//*[@id="ctl00_ContentPlaceHolder1_Int_SKSja"]',
    'skin_mottling': '//*[@id="ctl00_ContentPlaceHolder1_Int_SKSmt"]',
    'skin_turgor_good': '//*[@id="ctl00_ContentPlaceHolder1_Int_SKT_0"]',
    'skin_turgor_fair': '//*[@id="ctl00_ContentPlaceHolder1_Int_SKT_1"]',
    'skin_turgor_poor': '//*[@id="ctl00_ContentPlaceHolder1_Int_SKT_2"]',
    'wound_skin_impairment_no': '//*[@id="ctl00_ContentPlaceHolder1_Int_SKI_0"]',
    'wound_skin_impairment_yes': '//*[@id="ctl00_ContentPlaceHolder1_Int_SKI_1"]',

    # BRADEN SCALE
    # sensory perception
    'sensory_completely_limited': '//*[@id="ctl00_ContentPlaceHolder1_Int_SNP1"]',
    'sensory_very_limited': '//*[@id="ctl00_ContentPlaceHolder1_Int_SNP2"]',
    'sensory_slightly_limited': '//*[@id="ctl00_ContentPlaceHolder1_Int_SNP3"]',
    'sensory_no_impairment': '//*[@id="ctl00_ContentPlaceHolder1_Int_SNP4"]',

    'skin_completely_moist': '//*[@id="ctl00_ContentPlaceHolder1_Int_MOS1"]',
    'skin_very_moist': '//*[@id="ctl00_ContentPlaceHolder1_Int_MOS2"]',
    'skin_occas_moist': '//*[@id="ctl00_ContentPlaceHolder1_Int_MOS3"]',
    'skin_rarely_moist': '//*[@id="ctl00_ContentPlaceHolder1_Int_MOS4"]',

    # activity
    'bedfast': '//*[@id="ctl00_ContentPlaceHolder1_Int_ACT1"]',
    'chairfast': '//*[@id="ctl00_ContentPlaceHolder1_Int_ACT2"]',
    'walks_occasionally': '//*[@id="ctl00_ContentPlaceHolder1_Int_ACT3"]',
    'walks_frequently': '//*[@id="ctl00_ContentPlaceHolder1_Int_ACT4"]',

    # MOBILITY
    'completely_immobile': '//*[@id="ctl00_ContentPlaceHolder1_Int_MOB1"]',
    'very_limited_mobility': '//*[@id="ctl00_ContentPlaceHolder1_Int_MOB2"]',
    'slightly_limited_mobility': '//*[@id="ctl00_ContentPlaceHolder1_Int_MOB3"]',
    'no_mobility_limitations': '//*[@id="ctl00_ContentPlaceHolder1_Int_MOB4"]',

    # NUTRITION
    'very_poor_nutrition': '//*[@id="ctl00_ContentPlaceHolder1_Int_NUT1"]',
    'probably_inadequate_nutrition': '//*[@id="ctl00_ContentPlaceHolder1_Int_NUT2"]',
    'adequate_nutrition': '//*[@id="ctl00_ContentPlaceHolder1_Int_NUT3"]',
    'excellent_nutrition': '//*[@id="ctl00_ContentPlaceHolder1_Int_NUT4"]',
    'friction_problem': '//*[@id="ctl00_ContentPlaceHolder1_Int_FRI1"]',
    'friction_potential_problem': '//*[@id="ctl00_ContentPlaceHolder1_Int_FRI2"]',
    'friction_no_apparent_problem': '//*[@id="ctl00_ContentPlaceHolder1_Int_FRI3"]',
    # 'braden_total_score': '//*[@id="ctl00_ContentPlaceHolder1_lblTotalScore"]',  # DOESNT WORK DONT THINK I NEED IT
    'skin_other_observations': '//*[@id="ctl00_ContentPlaceHolder1_OO_Int"]',

    # IMMINENTLY DYING  # only if they have last 24hrs of life.
    'decreased_loc': '//*[@id="ctl00_ContentPlaceHolder1_CHK_ID_DC"]',
    'decreased_bowel_bladder_function': '//*[@id="ctl00_ContentPlaceHolder1_CHK_ID_DA"]',
    'decreased_food_fluid_intake': '//*[@id="ctl00_ContentPlaceHolder1_CHK_ID_DF"]',
    'increased_fatigue': '//*[@id="ctl00_ContentPlaceHolder1_CHK_ID_IF"]',
    'increased_respiratory_distress': '//*[@id="ctl00_ContentPlaceHolder1_CHK_ID_IR"]',
    'imminently_dying_other': '//*[@id="ctl00_ContentPlaceHolder1_OO_Imd"]',

    ### ENVIRONMENTAL SAFETY ###
    'safety_assessment_completed_yes': '//*[@id="ctl00_ContentPlaceHolder1_Env_SAC_0"]',
    'safety_assessment_completed_no': '//*[@id="ctl00_ContentPlaceHolder1_Env_SAC_1"]',
    'fall_risk_assessment_completed_yes': '//*[@id="ctl00_ContentPlaceHolder1_Env_FRA_0"]',
    'fall_risk_completed_no': '//*[@id="ctl00_ContentPlaceHolder1_Env_FRA_1"]',
    'disaster_triage_1': '//*[@id="ctl00_ContentPlaceHolder1_Env_DST_0"]',
    'disaster_triage_2': '//*[@id="ctl00_ContentPlaceHolder1_Env_DST_1"]',
    'disaster_triage_3': '//*[@id="ctl00_ContentPlaceHolder1_Env_DST_2"]',

    'if_level_1_confined_to_bed_chair_wc': '//*[@id="ctl00_ContentPlaceHolder1_Env_DSTl3cb"]',
    'if_level_1_dependent_on_walker_cane': '//*[@id="ctl00_ContentPlaceHolder1_Env_DSTl3dw"]',
    'if_level_1_lives_above_ground_floor': '//*[@id="ctl00_ContentPlaceHolder1_Env_DSTl2la"]',
    'if_level_1_requires_electricity_for_medical_equipment': '//*[@id="ctl00_ContentPlaceHolder1_Env_DSTl2re"]',

    'if_level_2_confined_to_wc': '//*[@id="ctl00_ContentPlaceHolder1_Env_DSTl2cb"]',
    'if_level_2_lives_above': '//*[@id="ctl00_ContentPlaceHolder1_Env_DSTl2la"]',
    'if_level_2_dependent_walker': '//*[@id="ctl00_ContentPlaceHolder1_Env_DSTl2dw"]',
    'if_level_2_requires_electricity': '//*[@id="ctl00_ContentPlaceHolder1_Env_DSTl2re"]',
    'if_level_3_lives_facility': '//*[@id="ctl00_ContentPlaceHolder1_Env_DSTl1_0"]',
    'if_level_3_has_place_to_go': '//*[@id="ctl00_ContentPlaceHolder1_Env_DSTl1_1"]',

    # PERSONAL CARE AND SUPPORT
    'need_for_hospice_aide_none': '//*[@id="ctl00_ContentPlaceHolder1_Pcs_NHAno"]',
    'hospice_aide_grooming': '//*[@id="ctl00_ContentPlaceHolder1_Pcs_NHAgr"]',
    'aide_meal_prep': '//*[@id="ctl00_ContentPlaceHolder1_Pcs_NHAlm"]',
    'meed_for_volunteer_none': '//*[@id="ctl00_ContentPlaceHolder1_Pcs_NFVno"]',
    'need_for_community_support_none': '//*[@id="ctl00_ContentPlaceHolder1_Pcs_NCSno"]',

    # TEACHING NEEDS
    'diagnosis_disease_teaching': '//*[@id="ctl00_ContentPlaceHolder1_Tea_PFPda"]',
    'medications_teaching': '//*[@id="ctl00_ContentPlaceHolder1_Tea_PFPme"]',
    'oxygen_teaching': '//*[@id="ctl00_ContentPlaceHolder1_Tea_PFPox"]',
    'dme_teaching': '//*[@id="ctl00_ContentPlaceHolder1_Tea_PFPdm"]',
    'infection_control_teaching': '//*[@id="ctl00_ContentPlaceHolder1_Tea_PFPin"]',
    'safe_use_meds_teaching': '//*[@id="ctl00_ContentPlaceHolder1_Tea_MSU"]',
    'other_teaching_box': '//*[@id="ctl00_ContentPlaceHolder1_Tea_PFPot"]',
    'other_teaching_txt': '//*[@id="ctl00_ContentPlaceHolder1_Tea_PFPotText"]',

    # CARE PROVIDED
    'physical_comfort': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_PHY"]',
    'structural_support': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Str"]',
    'emotional_support': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Emo"]',
    'spiritual_support': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_SPI"]',
    'safety_instructions': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Saf"]',
    'interpersonal_relationship': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Int"]',
    'environmental_needs': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Env"]',
    'self_determination': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_SDe"]',
    'knowledge_related_needs': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Kno"]',
    'language_comm_needs': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Lan"]',
    'offered_psychosocial': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_PSy"]',
    'offered_spiritual': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_SPIR"]',
    'offered_bereavement': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_BRV"]',
    'offered_other': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Oth"]',
    'offered_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_TxtCAP_PHYOther"]',

    ### NARRATIVE DISEASE TRAJECTORY ###
    'rapid_decline': '//*[@id="ctl00_ContentPlaceHolder1_DiseaseTraj_0"]',
    'saw_toothed_decline': '//*[@id="ctl00_ContentPlaceHolder1_DiseaseTraj_1"]',
    'slow_decline': '//*[@id="ctl00_ContentPlaceHolder1_DiseaseTraj_2"]',

    'narrative_txt': '//*[@id="ctl00_ContentPlaceHolder1_AssessNotes"]',

    'sign_submit_button': '//*[@id="ctl00_ContentPlaceHolder1_btnSignAndLock"]',
    # KEEP ADDING ALL COMPREHENSIVE XPS HERE
}

visit_dict_rn = {
    'visit_date': '//*[@id="ctl00_ContentPlaceHolder1_txtHDate"]',
    'in_person': '//*[@id="ctl00_ContentPlaceHolder1_Assesscodeid_0"]',
    'form_type': '//*[@id="ctl00_ContentPlaceHolder1_DrpVisitUnsc"]',
    # 'recert': '//*[@id="ctl00_ContentPlaceHolder1_AssessmentType_2"]',
    'staff_assigned': '//*[@id="ctl00_ContentPlaceHolder1_DropStaffAssigned"]',
    'discipline': '//*[@id="ctl00_ContentPlaceHolder1_DropDiscipline"]',
    'care_level': '//*[@id="ctl00_ContentPlaceHolder1_DropCareLevel"]',

    'covid_screened_no': '//*[@id="ctl00_ContentPlaceHolder1_rbPriorScreening_0"]',
    'covid_screened_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbPriorScreening_1"]',


    'pt_report_pos_no': '//*[@id="ctl00_ContentPlaceHolder1_rbPositive_0"]',
    'pt_report_pos_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbPositive_1"]',

    'lose_taste': '//*[@id="ctl00_ContentPlaceHolder1_rCoronaVirus_0"]',
    'addit_concerns_no': '//*[@id="ctl00_ContentPlaceHolder1_rbPatientPcgVisit_0"]',
    'addit_concerns_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbPatientPcgVisit_1"]',
    'covid_followed': '//*[@id="ctl00_ContentPlaceHolder1_chkCoronaInstructions"]',
    'utilized_ppe': '//*[@id="ctl00_ContentPlaceHolder1_chkPpe"]',

    'pain_controlled_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbControlled_0"]',
    'pain_controlled_no': '//*[@id="ctl00_ContentPlaceHolder1_RbControlled_1"]',
    'pain_controlled_n/a': '//*[@id="ctl00_ContentPlaceHolder1_RbControlled_3"]',

    'pain_level_at_visit': '//*[@id="ctl00_ContentPlaceHolder1_DropPainLevel"]',
    'pain_other_observations': '//*[@id="ctl00_ContentPlaceHolder1_Pain_Comtxt"]',

    'temp': '//*[@id="ctl00_ContentPlaceHolder1_txtTemp"]',
    'pulse': '//*[@id="ctl00_ContentPlaceHolder1_TxtPulse"]',
    'resp': '//*[@id="ctl00_ContentPlaceHolder1_TxtResp"]',
    'bp': '//*[@id="ctl00_ContentPlaceHolder1_TxtBp"]',
    'bp_sit': '//*[@id="ctl00_ContentPlaceHolder1_RBbpPosition_0"]',
    'bp_lying': '//*[@id="ctl00_ContentPlaceHolder1_RBbpPosition_1"]',
    'bp_standing': '//*[@id="ctl00_ContentPlaceHolder1_RBbpPosition_2"]',
    'height': '//*[@id="ctl00_ContentPlaceHolder1_TxtHt"]',
    'weight': '//*[@id="ctl00_ContentPlaceHolder1_TxtWt"]',
    'mac': '//*[@id="ctl00_ContentPlaceHolder1_TxtMac"]',
    'mac_left': '//*[@id="ctl00_ContentPlaceHolder1_RBMacPosition_0"]',
    'mac_right': '//*[@id="ctl00_ContentPlaceHolder1_RBMacPosition_1"]',
    'bmi': '//*[@id="ctl00_ContentPlaceHolder1_TxtBmi"]',
    'vitals_other_obs_txt': '//*[@id="ctl00_ContentPlaceHolder1_Vital_Comtxt"]',


    # psychosocial
    'pt_anxiety_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Anx1"]',
    'pt_anxiety_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Anx2"]',
    'pt_anxiety_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Anx3"]',
    'pt_anxiety_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Anx4"]',

    # THESE ARE GRAYED OUT WHEN I GOT THIS XP FYI
    'depression_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Dep1"]',
    'depression_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Dep2"]',
    'depression_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Dep3"]',
    'depression_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Dep4"]',

    'agitation_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_DIZ1"]',
    'agitation_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_DIZ2"]',
    'agitation_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_DIZ3"]',
    'agitation_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_DIZ4"]',

    'confusion_none': '//*[@id="ctl00_ContentPlaceHolder1_RBS_NMS_CON1"]',
    'confusion_mild': '//*[@id="ctl00_ContentPlaceHolder1_RBS_NMS_CON2"]',
    'confusion_mod': '//*[@id="ctl00_ContentPlaceHolder1_RBS_NMS_CON3"]',
    'confusion_sev': '//*[@id="ctl00_ContentPlaceHolder1_RBS_NMS_CON4"]',

    'speech_impair_none': '//*[@id="ctl00_ContentPlaceHolder1_RBS_SI_CON1"]',
    'speech_impair_mild': '//*[@id="ctl00_ContentPlaceHolder1_RBS_SI_CON2"]',
    'speech_impair_mod': '//*[@id="ctl00_ContentPlaceHolder1_RBS_SI_CON3"]',
    'speech_impair_sev': '//*[@id="ctl00_ContentPlaceHolder1_RBS_SI_CON4"]',
    'speech_impair_txt': '//*[@id="ctl00_ContentPlaceHolder1_NU_SI_txt"]',

    'other_neuro_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_OSY1"]',
    'other_neuro_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_OSY2"]',
    'other_neuro_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_OSY3"]',
    'other_neuro_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_OSY4"]',
    'other_neuro_txt': '//*[@id="ctl00_ContentPlaceHolder1_NU_O_txt"]',
    'other_obs_neuro': '//*[@id="ctl00_ContentPlaceHolder1_Neu_Comtxt"]',

    'arrhythmia_txt': '//*[@id="ctl00_ContentPlaceHolder1_CP_A"]',
    'arrhythmia_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_ARR1"]',
    'arrhythmia_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_ARR2"]',
    'arrhythmia_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_ARR3"]',
    'arrhythmia_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_ARR4"]',

    'edema_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_EDM1"]',
    'edema_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_EDM2"]',
    'edema_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_EDM3"]',
    'edema_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_EDM4"]',

    'chest_pain_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_CHP1"]',
    'chest_pain_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_CHP2"]',
    'chest_pain_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_CHP3"]',
    'chest_pain_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_CHP4"]',

    'cardio_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_OSY1"]',
    'cardio_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_OSY2"]',
    'cardio_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_OSY3"]',
    'cardio_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_OSY4"]',
    'cardio_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_CP_O_txt"]',
    'cardio_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Car_Comtxt"]',


    'infection_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_INF1"]',
    'infection_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_INF2"]',
    'infection_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_INF3"]',
    'infection_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_INF4"]',
    'infection_txt': '//*[@id="ctl00_ContentPlaceHolder1_In_O_Txt"]',

    'infection_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_II_O_Txt"]',
    'infection_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_OSY1"]',
    'infection_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_OSY2"]',
    'infection_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_OSY3"]',
    'infection_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_OSY4"]',
    'infection_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Imm_Comtxt"]',

    'nausea_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_NAU1"]',
    'nausea_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_NAU2"]',
    'nausea_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_NAU3"]',
    'nausea_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_NAU4"]',

    'vomiting_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_VOM1"]',
    'vomiting_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_VOM2"]',
    'vomiting_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_VOM3"]',
    'vomiting_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_VOM4"]',

    'constipation_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_CON1"]',
    'constipation_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_CON2"]',
    'constipation_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_CON3"]',
    'constipation_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_CON4"]',

    'diarrhea_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_DIA1"]',
    'diarrhea_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_DIA2"]',
    'diarrhea_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_DIA3"]',
    'diarrhea_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_DIA4"]',

    'gastro_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OSY1"]',
    'gastro_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OSY2"]',
    'gastro_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OSY3"]',
    'gastro_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OSY4"]',
    'gastro_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_GI_O_Txt"]',
    'last_bm': '//*[@id="ctl00_ContentPlaceHolder1_LastBM"]',
    'incontinent': '//*[@id="ctl00_ContentPlaceHolder1_Gas_STS"]',
    'gastro_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Gas_Comtxt"]',

    'percent_intake_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OI1"]',
    'percent_intake_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OI2"]',
    'percent_intake_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OI3"]',
    'percent_intake_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OI4"]',

    'nutrition_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_NUT_OSY1"]',
    'nutrition_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_NUT_OSY2"]',
    'nutrition_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_NUT_OSY3"]',
    'nutrition_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_NUT_OSY4"]',
    'nutrition_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_Nut_O_txt"]',

    'artificially_fed_no': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_0"]',
    'artificially_fed_peg': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_1"]',
    'artificially_fed_ng': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_2"]',
    'artificially_fed_jtube': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_3"]',
    'artificially_fed_pump': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_4"]',
    'artificially_fed_tpn': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_5"]',

    'artificially_fed_specify': '//*[@id="ctl00_ContentPlaceHolder1_Gas_IFTText"]',

    'diet_type': '//*[@id="ctl00_ContentPlaceHolder1_DrpDietType"]',
    'diet_specify': '//*[@id="ctl00_ContentPlaceHolder1_Gas_DTPText"]',
    'diet_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Nut_Comtxt"]',

    'blood_sugar_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_DIA1"]',
    'blood_sugar_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_DIA2"]',
    'blood_sugar_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_DIA3"]',
    'blood_sugar_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_DIA4"]',

    'endocrine_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_OSY1"]',
    'endocrine_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_OSY2"]',
    'endocrine_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_OSY3"]',
    'endocrine_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_OSY4"]',
    'endocrine_other_symptom': '//*[@id="ctl00_ContentPlaceHolder1_E_O_txt"]',
    'endocrine_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Endo_Comtxt"]',

    'urinary_problem_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_URP1"]',
    'urinary_problem_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_URP2"]',
    'urinary_problem_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_URP3"]',
    'urinary_problem_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_URP4"]',

    'urinary_other_symptom_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_OSY1"]',
    'urinary_other_symptom_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_OSY2"]',
    'urinary_other_symptom_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_OSY3"]',
    'urinary_other_symptom_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_OSY4"]',
    'urinary_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_GR_O_Txt"]',
    'urinary_incontinent': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URCin"]',
    'urinary_other_obser': '//*[@id="ctl00_ContentPlaceHolder1_Gen_Comtxt"]',

    'insomnia_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_INS1"]',
    'insomnia_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_INS2"]',
    'insomnia_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_INS3"]',
    'insomnia_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_INS4"]',

    'somnolence_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_SOM1"]',
    'somnolence_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_SOM2"]',
    'somnolence_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_SOM3"]',
    'somnolence_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_SOM4"]',

    'sleep_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_OSY1"]',
    'sleep_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_OSY2"]',
    'sleep_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_OSY3"]',
    'sleep_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_OSY4"]',
    'sleep_other_text': '//*[@id="ctl00_ContentPlaceHolder1_SR_O_txt"]',
    'sleep_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Sleep_Comtxt"]',

    'muskulo_weakness_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_WKN1"]',
    'muskulo_weakness_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_WKN2"]',
    'muskulo_weakness_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_WKN3"]',
    'muskulo_weakness_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_WKN4"]',

    'muskulo_contracture_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_CON1"]',
    'muskulo_contracture_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_CON2"]',
    'muskulo_contracture_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_CON3"]',
    'muskulo_contracture_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_CON4"]',

    'muskulo_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_M_O_txt"]',
    'muskulo_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_OSY1"]',
    'muskulo_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_OSY2"]',
    'muskulo_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_OSY3"]',
    'muskulo_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_OSY4"]',

    'muskulo_other_obs_txt': '//*[@id="ctl00_ContentPlaceHolder1_Musc_Comtxt"]',

    'rash_txt': '//*[@id="ctl00_ContentPlaceHolder1_ISW_R_Txt"]',
    'rash_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_PRU1"]',
    'rash_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_PRU2"]',
    'rash_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_PRU3"]',
    'rash_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_PRU4"]',

    'wound_txt': '//*[@id="ctl00_ContentPlaceHolder1_ISW_O_txt"]',
    'wound_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_WND1"]',
    'wound_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_WND2"]',
    'wound_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_WND3"]',
    'wound_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_WND4"]',

    'ulcer_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_ULC1"]',
    'ulcer_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_ULC2"]',
    'ulcer_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_ULC3"]',
    'ulcer_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_ULC4"]',

    'other_skin_symptom': '//*[@id="ctl00_ContentPlaceHolder1_IS_O_txt"]',
    'other_skin_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_OSY1"]',
    'other_skin_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_OSY2"]',
    'other_skin_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_OSY3"]',
    'other_skin_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_OSY4"]',
    'skin_other_obs_txt': '//*[@id="ctl00_ContentPlaceHolder1_Int_Comtxt"]',

    'ambulatory': '//*[@id="ctl00_ContentPlaceHolder1_RAD_CEMO_AN"]',
    'ambu_max_assist': '//*[@id="ctl00_ContentPlaceHolder1_Chk_CEMO_MX"]',

    'non_ambulatory': '//*[@id="ctl00_ContentPlaceHolder1_RAD_CEMO_AN1"]',
    'bedbound': '//*[@id="ctl00_ContentPlaceHolder1_ChK_CEMO_BB"]',
    'non_ambu_max_assist': '//*[@id="ctl00_ContentPlaceHolder1_Chk_CEMO_MXA"]',
    'mobility_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Mob_Comtxt"]',

    ### ADL ASSESSMENT ###
    'ambulation': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_A"]',
    'toileting': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_C"]',
    'transfer': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_T"]',
    'dressing': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_D"]',
    'feeding': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_F"]',
    'bathing': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_B"]',
    'total_adl': '//*[@id="ctl00_ContentPlaceHolder1_TotalADL"]',
    'adl_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Adl_Comtxt"]',

    'imminently_dying_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Dy_Comtxt"]',
    'any_fall_yes': '//*[@id="ctl00_ContentPlaceHolder1_Env_FRA_0"]',
    'any_fall_no': '//*[@id="ctl00_ContentPlaceHolder1_Env_FRA_1"]',
    'fall_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Fall_Comtxt"]',

    'change_in_safety_yes': '//*[@id="ctl00_ContentPlaceHolder1_Env_SAFA_0"]',
    'change_in_safety_no': '//*[@id="ctl00_ContentPlaceHolder1_Env_SAFA_1"]',
    'safety_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Saf_Comtxt"]',

    # visit checklist
    'update_family_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbVC1_0"]',
    'update_family_no': '//*[@id="ctl00_ContentPlaceHolder1_RbVC1_1"]',

    'update_cm_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbVC2_0"]',
    'update_cm_no': '//*[@id="ctl00_ContentPlaceHolder1_RbVC2_1"]',

    'comfort_pack_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbVC3_0"]',
    'comfort_pack_need': '//*[@id="ctl00_ContentPlaceHolder1_RbVC3_1"]',
    
    'dme_inspected_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbVC4_0"]',
    'dme_inspected_faulty': '//*[@id="ctl00_ContentPlaceHolder1_RbVC4_1"]',

    'check_foley_yes': '//*[@id="ctl00_ContentPlaceHolder1_RBVC6_0"]',
    'check_foley_no': '//*[@id="ctl00_ContentPlaceHolder1_RBVC6_1"]',
    'check_foley_n/a': '//*[@id="ctl00_ContentPlaceHolder1_RBVC6_2"]',

    'check_gi_tube_yes': '//*[@id="ctl00_ContentPlaceHolder1_RBVC7_0"]',
    'check_gi_tube_no': '//*[@id="ctl00_ContentPlaceHolder1_RBVC7_1"]',
    'check_gi_tube_n/a': '//*[@id="ctl00_ContentPlaceHolder1_RBVC7_2"]',

    'confirmed_sched_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbVC5_0"]',
    'confirmed_sched_request_change': '//*[@id="ctl00_ContentPlaceHolder1_RbVC5_1"]',
    # need to add anxiety down to bottom for LVN

    'kps': '//*[@id="ctl00_ContentPlaceHolder1_DDKPS"]',
    'pps': '//*[@id="ctl00_ContentPlaceHolder1_DDPPS"]',
    'fast': '//*[@id="ctl00_ContentPlaceHolder1_DDFast"]',
    'nyha': '//*[@id="ctl00_ContentPlaceHolder1_DDNYHA"]',


    'physical_comfort': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_PHY"]',
    'structural_support': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Str"]',
    'emotional_support': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Emo"]',
    'spiritual_support': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_SPI"]',
    'safety_instructions': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Saf"]',
    'interpersonal_relationship': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Int"]',
    'environmental_needs': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Env"]',
    'self_determination': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_SDe"]',
    'knowledge_related_needs': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Kno"]',
    'language_comm_needs': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Lan"]',


    'narrative_txt': '//*[@id="ctl00_ContentPlaceHolder1_TxtComments"]',
}

visit_dict_lvn = {
    'visit_date': '//*[@id="ctl00_ContentPlaceHolder1_txtHDate"]',
    'in_person': '//*[@id="ctl00_ContentPlaceHolder1_Assesscodeid_0"]',
    'form_type': '//*[@id="ctl00_ContentPlaceHolder1_DrpVisitUnsc"]',
    # 'recert': '//*[@id="ctl00_ContentPlaceHolder1_AssessmentType_2"]',
    'staff_assigned': '//*[@id="ctl00_ContentPlaceHolder1_DropStaffAssigned"]',
    'discipline': '//*[@id="ctl00_ContentPlaceHolder1_DropDiscipline"]',
    'care_level': '//*[@id="ctl00_ContentPlaceHolder1_DropCareLevel"]',

    'covid_screened_no': '//*[@id="ctl00_ContentPlaceHolder1_rbPriorScreening_0"]',
    'covid_screened_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbPriorScreening_1"]',


    'pt_report_pos_no': '//*[@id="ctl00_ContentPlaceHolder1_rbPositive_0"]',
    'pt_report_pos_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbPositive_1"]',

    'lose_taste': '//*[@id="ctl00_ContentPlaceHolder1_rCoronaVirus_0"]',
    'addit_concerns_no': '//*[@id="ctl00_ContentPlaceHolder1_rbPatientPcgVisit_0"]',
    'addit_concerns_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbPatientPcgVisit_1"]',
    'covid_followed': '//*[@id="ctl00_ContentPlaceHolder1_chkCoronaInstructions"]',
    'utilized_ppe': '//*[@id="ctl00_ContentPlaceHolder1_chkPpe"]',

    'pain_controlled_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbControlled_0"]',
    'pain_controlled_no': '//*[@id="ctl00_ContentPlaceHolder1_RbControlled_1"]',
    'pain_controlled_n/a': '//*[@id="ctl00_ContentPlaceHolder1_RbControlled_3"]',

    'pain_level_at_visit': '//*[@id="ctl00_ContentPlaceHolder1_DropPainLevel"]',
    'pain_other_observations': '//*[@id="ctl00_ContentPlaceHolder1_Pain_Comtxt"]',

    'temp': '//*[@id="ctl00_ContentPlaceHolder1_txtTemp"]',
    'pulse': '//*[@id="ctl00_ContentPlaceHolder1_TxtPulse"]',
    'resp': '//*[@id="ctl00_ContentPlaceHolder1_TxtResp"]',
    'bp': '//*[@id="ctl00_ContentPlaceHolder1_TxtBp"]',
    'bp_sit': '//*[@id="ctl00_ContentPlaceHolder1_RBbpPosition_0"]',
    'bp_lying': '//*[@id="ctl00_ContentPlaceHolder1_RBbpPosition_1"]',
    'bp_standing': '//*[@id="ctl00_ContentPlaceHolder1_RBbpPosition_2"]',
    'height': '//*[@id="ctl00_ContentPlaceHolder1_TxtHt"]',
    'weight': '//*[@id="ctl00_ContentPlaceHolder1_TxtWt"]',
    'mac': '//*[@id="ctl00_ContentPlaceHolder1_TxtMac"]',
    'mac_left': '//*[@id="ctl00_ContentPlaceHolder1_RBMacPosition_0"]',
    'mac_right': '//*[@id="ctl00_ContentPlaceHolder1_RBMacPosition_1"]',
    'bmi': '//*[@id="ctl00_ContentPlaceHolder1_TxtBmi"]',
    'vitals_other_obs_txt': '//*[@id="ctl00_ContentPlaceHolder1_Vital_Comtxt"]',



    # psychosocial
    'pt_anxiety_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Anx1"]',
    'pt_anxiety_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Anx2"]',
    'pt_anxiety_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Anx3"]',
    'pt_anxiety_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Anx4"]',

    # THESE ARE GRAYED OUT WHEN I GOT THIS XP FYI
    'depression_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Dep1"]',
    'depression_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Dep2"]',
    'depression_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Dep3"]',
    'depression_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_Dep4"]',

    'agitation_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_DIZ1"]',
    'agitation_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_DIZ2"]',
    'agitation_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_DIZ3"]',
    'agitation_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_DIZ4"]',

    'confusion_none': '//*[@id="ctl00_ContentPlaceHolder1_RBS_NMS_CON1"]',
    'confusion_mild': '//*[@id="ctl00_ContentPlaceHolder1_RBS_NMS_CON2"]',
    'confusion_mod': '//*[@id="ctl00_ContentPlaceHolder1_RBS_NMS_CON3"]',
    'confusion_sev': '//*[@id="ctl00_ContentPlaceHolder1_RBS_NMS_CON4"]',

    'speech_impair_none': '//*[@id="ctl00_ContentPlaceHolder1_RBS_SI_CON1"]',
    'speech_impair_mild': '//*[@id="ctl00_ContentPlaceHolder1_RBS_SI_CON2"]',
    'speech_impair_mod': '//*[@id="ctl00_ContentPlaceHolder1_RBS_SI_CON3"]',
    'speech_impair_sev': '//*[@id="ctl00_ContentPlaceHolder1_RBS_SI_CON4"]',
    'speech_impair_txt': '//*[@id="ctl00_ContentPlaceHolder1_NU_SI_txt"]',

    'other_neuro_none:': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_OSY1"]',
    'other_neuro_:': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_OSY1"]',
    'other_neuro:': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_OSY1"]',
    'other_neuro:': '//*[@id="ctl00_ContentPlaceHolder1_RB_NMS_OSY1"]',
    'other_neuro_txt:': '//*[@id="ctl00_ContentPlaceHolder1_NU_O_txt"]',
    'other_obs_neuro': '//*[@id="ctl00_ContentPlaceHolder1_Neu_Comtxt"]',

    'arrhythmia_txt': '//*[@id="ctl00_ContentPlaceHolder1_CP_A"]',
    'arrhythmia_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_ARR1"]',
    'arrhythmia_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_ARR2"]',
    'arrhythmia_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_ARR3"]',
    'arrhythmia_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_ARR4"]',

    'edema_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_EDM1"]',
    'edema_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_EDM2"]',
    'edema_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_EDM3"]',
    'edema_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_EDM4"]',

    'chest_pain_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_CHP1"]',
    'chest_pain_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_CHP2"]',
    'chest_pain_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_CHP3"]',
    'chest_pain_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_CHP4"]',

    'cardio_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_OSY1"]',
    'cardio_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_OSY2"]',
    'cardio_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_OSY3"]',
    'cardio_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_CAR_OSY4"]',
    'cardio_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_CP_O_txt"]',
    'cardio_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Car_Comtxt"]',


    'infection_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_INF1"]',
    'infection_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_INF2"]',
    'infection_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_INF3"]',
    'infection_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_INF4"]',
    'infection_txt': '//*[@id="ctl00_ContentPlaceHolder1_In_O_Txt"]',

    'infection_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_II_O_Txt"]',
    'infection_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_OSY1"]',
    'infection_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_OSY2"]',
    'infection_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_OSY3"]',
    'infection_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_IMG_OSY4"]',
    'infection_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Imm_Comtxt"]',

    'nausea_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_NAU1"]',
    'nausea_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_NAU2"]',
    'nausea_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_NAU3"]',
    'nausea_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_NAU4"]',

    'vomiting_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_VOM1"]',
    'vomiting_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_VOM2"]',
    'vomiting_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_VOM3"]',
    'vomiting_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_VOM4"]',

    'constipation_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_CON1"]',
    'constipation_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_CON2"]',
    'constipation_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_CON3"]',
    'constipation_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_CON4"]',

    'diarrhea_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_DIA1"]',
    'diarrhea_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_DIA2"]',
    'diarrhea_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_DIA3"]',
    'diarrhea_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_DIA4"]',

    'gastro_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OSY1"]',
    'gastro_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OSY2"]',
    'gastro_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OSY3"]',
    'gastro_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OSY4"]',
    'gastro_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_GI_O_Txt"]',
    'last_bm': '//*[@id="ctl00_ContentPlaceHolder1_LastBM"]',
    'incontinent': '//*[@id="ctl00_ContentPlaceHolder1_Gas_STS"]',
    'gastro_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Gas_Comtxt"]',

    'percent_intake_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OI1"]',
    'percent_intake_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OI2"]',
    'percent_intake_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OI3"]',
    'percent_intake_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GAS_OI4"]',

    'nutrition_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_NUT_OSY1"]',
    'nutrition_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_NUT_OSY2"]',
    'nutrition_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_NUT_OSY3"]',
    'nutrition_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_NUT_OSY4"]',
    'nutrition_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_Nut_O_txt"]',

    'artificially_fed_no': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_0"]',
    'artificially_fed_peg': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_1"]',
    'artificially_fed_ng': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_2"]',
    'artificially_fed_jtube': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_3"]',
    'artificially_fed_pump': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_4"]',
    'artificially_fed_tpn': '//*[@id="ctl00_ContentPlaceHolder1_Gas_AFF_5"]',

    'artificially_fed_specify': '//*[@id="ctl00_ContentPlaceHolder1_Gas_IFTText"]',

    'diet_type': '//*[@id="ctl00_ContentPlaceHolder1_DrpDietType"]',
    'diet_specify': '//*[@id="ctl00_ContentPlaceHolder1_Gas_DTPText"]',
    'diet_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Nut_Comtxt"]',

    'blood_sugar_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_DIA1"]',
    'blood_sugar_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_DIA2"]',
    'blood_sugar_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_DIA3"]',
    'blood_sugar_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_DIA4"]',

    'endocrine_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_OSY1"]',
    'endocrine_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_OSY2"]',
    'endocrine_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_OSY3"]',
    'endocrine_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_IND_OSY4"]',
    'endocrine_other_symptom': '//*[@id="ctl00_ContentPlaceHolder1_E_O_txt"]',
    'endocrine_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Endo_Comtxt"]',

    'urinary_problem_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_URP1"]',
    'urinary_problem_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_URP2"]',
    'urinary_problem_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_URP3"]',
    'urinary_problem_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_URP4"]',

    'urinary_other_symptom_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_OSY1"]',
    'urinary_other_symptom_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_OSY2"]',
    'urinary_other_symptom_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_OSY3"]',
    'urinary_other_symptom_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_GEN_OSY4"]',
    'urinary_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_GR_O_Txt"]',
    'urinary_incontinent': '//*[@id="ctl00_ContentPlaceHolder1_Gen_URCin"]',
    'urinary_other_obser': '//*[@id="ctl00_ContentPlaceHolder1_Gen_Comtxt"]',

    'insomnia_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_INS1"]',
    'insomnia_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_INS2"]',
    'insomnia_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_INS3"]',
    'insomnia_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_INS4"]',

    'somnolence_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_SOM1"]',
    'somnolence_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_SOM2"]',
    'somnolence_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_SOM3"]',
    'somnolence_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_SOM4"]',

    'sleep_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_OSY1"]',
    'sleep_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_OSY2"]',
    'sleep_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_OSY3"]',
    'sleep_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_SLP_OSY4"]',
    'sleep_other_text': '//*[@id="ctl00_ContentPlaceHolder1_SR_O_txt"]',
    'sleep_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Sleep_Comtxt"]',

    'muskulo_weakness_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_WKN1"]',
    'muskulo_weakness_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_WKN2"]',
    'muskulo_weakness_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_WKN3"]',
    'muskulo_weakness_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_WKN4"]',

    'muskulo_contracture_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_CON1"]',
    'muskulo_contracture_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_CON2"]',
    'muskulo_contracture_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_CON3"]',
    'muskulo_contracture_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_CON4"]',

    'muskulo_other_txt': '//*[@id="ctl00_ContentPlaceHolder1_M_O_txt"]',
    'muskulo_other_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_OSY1"]',
    'muskulo_other_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_OSY2"]',
    'muskulo_other_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_OSY3"]',
    'muskulo_other_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_MUS_OSY4"]',

    'muskulo_other_obs_txt': '//*[@id="ctl00_ContentPlaceHolder1_Musc_Comtxt"]',

    'rash_txt': '//*[@id="ctl00_ContentPlaceHolder1_ISW_R_Txt"]',
    'rash_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_PRU1"]',
    'rash_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_PRU2"]',
    'rash_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_PRU3"]',
    'rash_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_PRU4"]',

    'wound_txt': '//*[@id="ctl00_ContentPlaceHolder1_ISW_O_txt"]',
    'wound_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_WND1"]',
    'wound_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_WND2"]',
    'wound_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_WND3"]',
    'wound_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_WND4"]',

    'ulcer_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_ULC1"]',
    'ulcer_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_ULC2"]',
    'ulcer_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_ULC3"]',
    'ulcer_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_ULC4"]',

    'other_skin_symptom': '//*[@id="ctl00_ContentPlaceHolder1_IS_O_txt"]',
    'other_skin_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_OSY1"]',
    'other_skin_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_OSY2"]',
    'other_skin_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_OSY3"]',
    'other_skin_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_INT_OSY4"]',
    'skin_other_obs_txt': '//*[@id="ctl00_ContentPlaceHolder1_Int_Comtxt"]',

    'ambulatory': '//*[@id="ctl00_ContentPlaceHolder1_RAD_CEMO_AN"]',
    'ambu_max_assist': '//*[@id="ctl00_ContentPlaceHolder1_Chk_CEMO_MX"]',

    'non_ambulatory': '//*[@id="ctl00_ContentPlaceHolder1_RAD_CEMO_AN1"]',
    'bedbound': '//*[@id="ctl00_ContentPlaceHolder1_ChK_CEMO_BB"]',
    'non_ambu_max_assist': '//*[@id="ctl00_ContentPlaceHolder1_Chk_CEMO_MXA"]',
    'mobility_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Mob_Comtxt"]',

    ### ADL ASSESSMENT ###
    'ambulation': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_A"]',
    'toileting': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_C"]',
    'transfer': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_T"]',
    'dressing': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_D"]',
    'feeding': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_F"]',
    'bathing': '//*[@id="ctl00_ContentPlaceHolder1_DRP_CEAD_B"]',
    'total_adl': '//*[@id="ctl00_ContentPlaceHolder1_TotalADL"]',
    'adl_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Adl_Comtxt"]',

    'imminently_dying_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Dy_Comtxt"]',
    'any_fall_yes': '//*[@id="ctl00_ContentPlaceHolder1_Env_FRA_0"]',
    'any_fall_no': '//*[@id="ctl00_ContentPlaceHolder1_Env_FRA_1"]',
    'fall_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Fall_Comtxt"]',

    'change_in_safety_yes': '//*[@id="ctl00_ContentPlaceHolder1_Env_SAFA_0"]',
    'change_in_safety_no': '//*[@id="ctl00_ContentPlaceHolder1_Env_SAFA_1"]',
    'safety_other_obs': '//*[@id="ctl00_ContentPlaceHolder1_Saf_Comtxt"]',

    # visit checklist
    'update_family_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbVC1_0"]',
    'update_family_no': '//*[@id="ctl00_ContentPlaceHolder1_RbVC1_1"]',

    'update_cm_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbVC2_0"]',
    'update_cm_no': '//*[@id="ctl00_ContentPlaceHolder1_RbVC2_1"]',

    'comfort_pack_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbVC3_0"]',
    'comfort_pack_need': '//*[@id="ctl00_ContentPlaceHolder1_RbVC3_1"]',
    
    'dme_inspected_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbVC4_0"]',
    'dme_inspected_faulty': '//*[@id="ctl00_ContentPlaceHolder1_RbVC4_1"]',

    'check_foley_yes': '//*[@id="ctl00_ContentPlaceHolder1_RBVC6_0"]',
    'check_foley_no': '//*[@id="ctl00_ContentPlaceHolder1_RBVC6_1"]',
    'check_foley_n/a': '//*[@id="ctl00_ContentPlaceHolder1_RBVC6_2"]',

   
    'check_gi_tube_yes': '//*[@id="ctl00_ContentPlaceHolder1_RBVC7_0"]',
    'check_gi_tube_no': '//*[@id="ctl00_ContentPlaceHolder1_RBVC7_1"]',
    'check_gi_tube_n/a': '//*[@id="ctl00_ContentPlaceHolder1_RBVC7_2"]',

    'confirmed_sched_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbVC5_0"]',
    'confirmed_sched_request_change': '//*[@id="ctl00_ContentPlaceHolder1_RbVC5_1"]',


    # STOP ADDING HERE

    'physical_comfort': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_PHY"]',
    'structural_support': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Str"]',
    'emotional_support': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Emo"]',
    'spiritual_support': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_SPI"]',
    'safety_instructions': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Saf"]',
    'interpersonal_relationship': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Int"]',
    'environmental_needs': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Env"]',
    'self_determination': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_SDe"]',
    'knowledge_related_needs': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Kno"]',
    'language_comm_needs': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Lan"]',
    
 
    'narrative_txt': '//*[@id="ctl00_ContentPlaceHolder1_TxtComments"]',
}

visit_dict_sw = {
    'visit_date': '//*[@id="ctl00_ContentPlaceHolder1_txtHDate"]',
    'in_person': '//*[@id="ctl00_ContentPlaceHolder1_Assesscodeid_0"]',
    'form_type': '//*[@id="ctl00_ContentPlaceHolder1_DrpVisitUnsc"]',
    'chief_complaint': '//*[@id="ctl00_ContentPlaceHolder1_TxtPsgStatesChiefComplaint"]',
    # 'recert': '//*[@id="ctl00_ContentPlaceHolder1_AssessmentType_2"]',
    'staff_assigned': '//*[@id="ctl00_ContentPlaceHolder1_DropStaffAssigned"]',
    'discipline': '//*[@id="ctl00_ContentPlaceHolder1_DropDiscipline"]',
    'care_level': '//*[@id="ctl00_ContentPlaceHolder1_DropCareLevel"]',

    'covid_screened_no': '//*[@id="ctl00_ContentPlaceHolder1_rbPriorScreening_0"]',
    'covid_screened_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbPriorScreening_1"]',

    'pt_report_pos_no': '//*[@id="ctl00_ContentPlaceHolder1_rbPositive_0"]',
    'pt_report_pos_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbPositive_1"]',


    'lose_taste_no': '//*[@id="ctl00_ContentPlaceHolder1_rbCoronaVirus_0"]',
    'lose_taste_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbCoronaVirus_1"]',


    'addit_concerns_no': '//*[@id="ctl00_ContentPlaceHolder1_rbPatientPcgVisit_0"]',
    'addit_concerns_yes': '//*[@id="ctl00_ContentPlaceHolder1_rbPositive_1"]',


    'covid_followed': '//*[@id="ctl00_ContentPlaceHolder1_chkCoronaInstructions"]',
    'utilized_ppe': '//*[@id="ctl00_ContentPlaceHolder1_chkPpe"]',

    'pain_controlled_yes': '//*[@id="ctl00_ContentPlaceHolder1_RbControlled_0"]',
    'pain_controlled_no': '//*[@id="ctl00_ContentPlaceHolder1_RbControlled_1"]',
    'pain_controlled_n/a': '//*[@id="ctl00_ContentPlaceHolder1_RbControlled_3"]',

    'pain_level_at_visit': '//*[@id="ctl00_ContentPlaceHolder1_DropPainLevel"]',
    'pain_other_observations': '//*[@id="ctl00_ContentPlaceHolder1_Pain_Comtxt"]',

    # psychosocial

    # ## NEED TO ADD ANXIETY DOWN TO THESE PHYSICAL COMFORT XP
    'pt_anxiety_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_PSY_PA1"]',
    'pt_anxiety_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_PSY_PA2"]',
    'pt_anxiety_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_PSY_PA3"]',
    'pt_anxiety_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_PSY_PA4"]',

    'pcg_anxiety_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_PSY_GA1"]',
    'pcg_anxiety_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_PSY_GA2"]',
    'pcg_anxiety_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_PSY_GA3"]',
    'pcg_anxiety_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_PSY_GA4"]',

    'distress_rating_none': '//*[@id="ctl00_ContentPlaceHolder1_RB_PSY_PD1"]',
    'distress_rating_mild': '//*[@id="ctl00_ContentPlaceHolder1_RB_PSY_PD2"]',
    'distress_rating_mod': '//*[@id="ctl00_ContentPlaceHolder1_RB_PSY_PD3"]',
    'distress_rating_sev': '//*[@id="ctl00_ContentPlaceHolder1_RB_PSY_PD4"]',


    # NEED TO ADD DOWN TO FAST NYHA

    'physical_comfort': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_PHY"]',
    'structural_support': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Str"]',
    'emotional_support': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Emo"]',
    'spiritual_support': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_SPI"]',
    'safety_instructions': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Saf"]',
    'interpersonal_relationship': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Int"]',
    'environmental_needs': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Env"]',
    'self_determination': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_SDe"]',
    'knowledge_related_needs': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Kno"]',
    'language_comm_needs': '//*[@id="ctl00_ContentPlaceHolder1_CHK_CAP_Lan"]',
    'narrative_txt': '//*[@id="ctl00_ContentPlaceHolder1_TxtComments"]',
}


idg_notes_xp_dict = {
                'visit_date': '//*[@id="ctl00_ContentPlaceHolder1_txtHDate"]',
                'nursing_disc': '//*[@id="ctl00_ContentPlaceHolder1_TxtComments"]',
                'spiritual_disc': '//*[@id="ctl00_ContentPlaceHolder1_TxtCommentsSPC"]',
                'psychosocial_disc': '//*[@id="ctl00_ContentPlaceHolder1_TxtCommentsPSY"]',
                'physician_disc': '//*[@id="ctl00_ContentPlaceHolder1_TxtCommentsOTH"]',
                'primary_dx': '//*[@id="ctl00_ContentPlaceHolder1_PrimaryDx"]',
                'primary_disease': '//*[@id="ctl00_ContentPlaceHolder1_DrpPDDisease0"]',
                'level_of_care': '//*[@id="ctl00_ContentPlaceHolder1_lblLevelOfCare"]',
                'frequency_of_visit': '//*[@id="ctl00_ContentPlaceHolder1_lblFrequencyOfVisit"]',
                'staff_assignment': '//*[@id="ctl00_ContentPlaceHolder1_lblStaffAssignment"]',
                'sign1': '//*[@id="ctl00_ContentPlaceHolder1_BtnSignatureMD"]',
                'sign2': '//*[@id="ctl00_ContentPlaceHolder1_BtnSignatureMSW"]',
                'sign3': '//*[@id="ctl00_ContentPlaceHolder1_BtnSignaturePCP"]',
                'sign4': '//*[@id="ctl00_ContentPlaceHolder1_BtnSignatureRN"]',
                'sign5': '//*[@id="ctl00_ContentPlaceHolder1_BtnSignatureChaplain"]',
            }
