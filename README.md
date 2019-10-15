# takeon-data-prep-lambda-main

## About this repository
This is a lambda function that reads from the TakeOn-DataPrep-Input queue, taking in the parameters of reference, period, survey and bpmId.  It then makes a GET HTTP call to the Business Layer service (ValidationPrepConfig endpoint) in the takeon EKS cluster and parses the JSON output from this.  The main work done in this lambda is the parsing of the Validation Output JSON.  It then combines the Validation_period, contributor_reference, survey, periodicity, bpmId, contributor_details, response_details and Validation_config and puts into a format that the Wrangler expects.  This combined output is put on to a queue ready for the Wrangler to pick up.

## Example Input
{
  "reference": "77700000001",
  "period": "201803",
  "survey": "066",
  "bpmId": "12345"
}

## Example Output


### In order to run the unit tests:
`python3 -m pytest -vv tests/`
