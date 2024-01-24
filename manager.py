
from app.controller.RecordDatainGoogleSheet import RecordDatainGoogleSheet
from app import create_app

app = RecordDatainGoogleSheet(create_app())
app.writeInGoogleSheet()
