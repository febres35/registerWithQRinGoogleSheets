# -*- coding utf-8 -*-
from pyqrcode import create

class GeneratorQR(object):
    
    id = 1000
    
    

    def __init__(self, ascii, args = []):
        """
            @param ascii: code ascii in String
        """
        code = ascii +str(id)
        self.qr = create(int(ascii) and code, error = 'L')
        self.qr.png(chr(int(ascii))+str(self.id)+'.png', scale = 6)
        
        self.increment()

    @classmethod
    def increment(cls):
        cls.id += 1

