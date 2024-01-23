from datetime import datetime
class AttributeOfGoogleSheets: 
    
    def __init__(self, wI, NID, fN, lN):
        self.__workIndentifition__ = wI
        self.__nationaIdentifyDocument__ = NID
        self.__firstName__ = fN
        self.__lastName__ = lN
        self.__passin__ = datetime.now().strftime('%H:%M:%S')
        self.__date__ = datetime.now().strftime('%Y-%m-%d')

    def __str__(self) -> str:
        return f'{self.__workIndentifition__} - {self.__firstName__} {self.__lastName__} - {self.__date__} { self.__passin__}'

    def getData(self, wI):
        data = (
            self.__workIndentifition__,
            self.__nationaIdentifyDocument__,
            self.__firstName__,
            self.__lastName__,
            self.__passin__,
            self.__date__
        )
        return data



