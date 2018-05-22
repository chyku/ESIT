"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Google Sheets API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/sheets
2. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
   https://developers.google.com/sheets/api/guides/values
   https://stackoverflow.com/questions/38949318/google-sheets-api-returns-the-caller-does-not-have-permission-when-using-serve
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time
import datetime

from pprint import pprint

from googleapiclient import discovery

# Authentication credentials
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('credentials.json')
credentials= store.get()
if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    credentials = tools.run_flow(flow, store)
    
service = build('sheets', 'v4', http=credentials.authorize(Http()))

service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to update.
spreadsheet_id = '1aiT2VB92fMMpK9RFkC6y7WStEurKKNWohLWG0sP2tgo'
# The A1 notation of the values to update.
range_ = 'Sheet1!A1:B5'  # TODO: Update placeholder value.

# How the input data should be interpreted.
value_input_option = 'USER_ENTERED'
# Append vs replace
insert_data_option = 'INSERT_ROWS'

# setup done
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

value_range_body = {
    "range": range_, # The range the values cover, in A1 notation.
      # For output, this range indicates the entire requested range,
      # even though the values will exclude trailing rows and columns.
      # When appending values, this field represents the range to search for a
      # table, after which values will be appended.
  "values": [
      # For input, with `range=A1:B2,majorDimension=ROWS` then `[[1,2],[3,4]]`
      # will set `A1=1,B1=2,A2=3,B2=4`. With `range=A1:B2,majorDimension=COLUMNS`
      # then `[[1,2],[3,4]]` will set `A1=1,B1=3,A2=2,B2=4`.
      # To set a cell to an empty value, set the string value to an empty string.
      [st,st],[3,4]
    ],
    "majorDimension": "COLUMNS"
}

# request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)
