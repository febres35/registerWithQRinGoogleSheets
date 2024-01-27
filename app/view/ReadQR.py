from cv2 import VideoCapture
from pyzbar.pyzbar import decode
from datetime import datetime
import numpy



class ReadQR(object):
    
    def __init__(self):
        self.cap = VideoCapture(-1)
    

    def cam(self):
        
        while True:
            ret, frame = self.cap

            for codes in decode(frame):
                
                data = codes.data.decode('utf-8')

                type = chr(int(data[:2]))
                code = int(data[2:])
                
                #create reading area
                pts= numpy.array([codes.polygon], numpy.int32)

                xi, yi = codes.rect.left, codes.rect.top

                #resizing
                pts = pts.reshage((-1,1,2))

                self.defineActivy(type, code)


    def defineActivy(self, area, code, ):
        if 'A' == type:
            print(f'The worker with code {code} belongs to the general management of systems ({area})')
