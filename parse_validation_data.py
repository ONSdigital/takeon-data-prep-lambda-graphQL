import json

def parse_validation_data(json_input):

    validation_config_list = []
    for i in json_input:
        rule_dict = {}
        rule_dict['template'] = i['rule']
        rule_dict['formula'] = i['baseformula']
        question_list_temp = i['validationformsByRule']['nodes']
        question_list = []
        question_details_dict = {}
        parameters_list = []
        for j in question_list_temp:
            question_details_dict['validationid'] = j['validationid']
            question_details_dict['primary_question'] = j['primaryquestion']
            question_details_dict['default'] = j['defaultvalue']
            parameters_list_temp = j['validationparametersByValidationid']['nodes']
            for k in parameters_list_temp:
                parameters_list.append(k)
            question_details_dict['parameters'] = parameters_list

        question_list.append(question_details_dict)
        rule_dict['question_details'] = question_list
        val_config_list.append(rule_dict)


    return validation_config_list
