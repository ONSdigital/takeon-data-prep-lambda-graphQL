def parse_validation_data(json_input):

    validation_config_list = []
    for rule in json_input:
        rule_dict = {}
        rule_dict['template'] = rule['rule']
        rule_dict['formula'] = rule['baseformula']
        question_list_temp = rule['validationformsByRule']['nodes']
        question_list = []
        question_details_dict = {}
        parameters_list = []
        for question in question_list_temp:
            question_details_dict['validationid'] = question['validationid']
            question_details_dict['primary_question'] = question['primaryquestion']
            question_details_dict['default'] = question['defaultvalue']
            parameters_list_temp = question['validationparametersByValidationid']['nodes']
            for validation_parameter in parameters_list_temp:
                parameters_list.append(validation_parameter)
            question_details_dict['parameters'] = parameters_list

        question_list.append(question_details_dict)
        rule_dict['question_details'] = question_list
        val_config_list.append(rule_dict)


    return validation_config_list
