from os import path


dirName = 'conf'
fileName = 'key.json'

def create_app():
    PATH_TO_KEY = (path.realpath(f'{dirName}'))
    PATH_TO_KEY = path.join(PATH_TO_KEY, f'{fileName}')

    spreadsheets_ID = '1PEpbe_uRVjoUIJ_dXcoy3owV2K3yRr-2wzksUcShdm8'
    
    config = {
    'PATH_TO_KEY' : PATH_TO_KEY,
    'spreadsheets_ID': spreadsheets_ID
    }

    return config



