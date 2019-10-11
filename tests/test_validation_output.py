'''
Unit tests to check format of output data
'''
from parse_validation_data import parse_validation_data
import pytest
import json

@pytest.fixture
def input_validation_data():
    return [
        {
          'rule': 'POPM',
          'baseformula': 'abs(question - comparison_question) > threshold AND question > 0 AND comparison_question > 0',
          'validationformsByRule': {
            'nodes': [
              {
                'validationid': 20,
                'primaryquestion': '1000',
                'defaultvalue': '0',
                'validationparametersByValidationid': {
                  'nodes': [
                    {
                      'parameter': 'comparison_question',
                      'value': '1000',
                      'source': 'response',
                      'periodoffset': 1
                    },
                    {
                      'parameter': 'question',
                      'value': '1000',
                      'source': 'response',
                      'periodoffset': 0
                    },
                    {
                      'parameter': 'threshold',
                      'value': '20000',
                      'source': '',
                      'periodoffset': 0
                    }
                  ]
                }
              },
              {
                'validationid': 21,
                'primaryquestion': '1001',
                'defaultvalue': '0',
                'validationparametersByValidationid': {
                  'nodes': [
                    {
                      'parameter': 'comparison_question',
                      'value': '1001',
                      'source': 'response',
                      'periodoffset': 1
                    },
                    {
                      'parameter': 'question',
                      'value': '1001',
                      'source': 'response',
                      'periodoffset': 0
                    },
                    {
                      'parameter': 'threshold',
                      'value': '0',
                      'source': '',
                      'periodoffset': 0
                    }
                  ]
                }
              }
            ]
          }
        }
      ]

@pytest.fixture
def output_validation_data():
    return [
  {
    'template': 'POPM',
    'formula': 'abs(question - comparison_question) > threshold AND question > 0 AND comparison_question > 0',
    'question_details': [
      {
        'validationid': 21,
        'primary_question': '1001',
        'default': '0',
        'parameters': [
          {
            'periodoffset': 1,
            'parameter': 'comparison_question',
            'source': 'response',
            'value': '1000'
          },
          {
            'periodoffset': 0,
            'parameter': 'question',
            'source': 'response',
            'value': '1000'
          },
          {
            'periodoffset': 0,
            'parameter': 'threshold',
            'source': '',
            'value': '20000'
          },
          {
            'periodoffset': 1,
            'parameter': 'comparison_question',
            'source': 'response',
            'value': '1001'
          },
          {
            'periodoffset': 0,
            'parameter': 'question',
            'source': 'response',
            'value': '1001'
          },
          {
            'periodoffset': 0,
            'parameter': 'threshold',
            'source': '',
            'value': '0'
          }
        ]
      }
    ]
  }
]

def test_output(input_validation_data, output_validation_data):
    '''
    Checks to see if parse_validation_data function returns expected format for
    Wrangler
    :param input_validation_data
    :return None
    '''
    print(type(input_validation_data))
    returned_data = parse_validation_data(input_validation_data)
    assert returned_data == output_validation_data
