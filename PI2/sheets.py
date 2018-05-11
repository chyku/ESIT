"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Google Sheets API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/sheets
2. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

from pprint import pprint

from googleapiclient import discovery

# TODO: Change placeholder below to generate authentication credentials. See
# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.com/auth/spreadsheets'
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('credentials.json')
credentials= store.get()
if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    credentials = tools.run_flow(flow, store)
    
service = build('sheets', 'v4', http=credentials.authorize(Http()))

service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to update.
spreadsheet_id = '1Cyxfg7UIq2_1-mnb55ibDHYYxznCUos1RNqyq_ff2Y0'
# The A1 notation of the values to update.
range_ = 'Sheet1!A1:D4'  # TODO: Update placeholder value.

# How the input data should be interpreted.
value_input_option = 'USER_ENTERED'  # TODO: Update placeholder value.

value_range_body = {
    # TODO: Add desired entries to the request body. All existing entries
    # will be replaced.
    {"Item", "Cost", "Stocked", "Ship Date"},
    {"Wheel", "$20.50", "4", "3/1/2016"},
    {"Door", "$15", "2", "3/15/2016"},
    {"Engine", "$100", "1", "30/20/2016"}
}

request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)
