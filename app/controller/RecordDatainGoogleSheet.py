from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
from app import config


class RecordDatainGoogleSheet:

    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.KEY = config['PATH_TO_KEY']
        self.SPREADSHEET_ID = config['spreadsheets_ID']
        
    def writeGoogleSheet(self):
        creds = None
        creds = service_account.Credentials.from_service_account_file(self.KEY, scopes=self.SCOPES)

        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        # Debe ser una matriz por eso el doble [[]]
        values = [['Prueba!', 'Prueba!', 'Prueba!', 'Prueba!' , 'Prueba!', 'Prueba!', 'Prueba!']]
        # Llamamos a la api
        result = sheet.values().append(spreadsheetId=self.SPREADSHEET_ID,
                                    range='A1',
                                    valueInputOption='USER_ENTERED',
                                    body={'values':values}).execute()
        print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")


