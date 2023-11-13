# ----------Imports----------

import numpy
import cv2 
from pyzbar import pyzbar
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol

import time
import os

# ----------Functions----------

# Start Function main
def main():
    
    global vc_number
    vc_number = 0

    if not testCameraDevice(vc_number):
        return

    #1
    title = "Barcode/QR code reader"
    cv2.namedWindow(title, 1)

    if(vc_number == 0):
        stream = cv2.VideoCapture(vc_number)
    elif(vc_number == 1):
        ip_camera = "rtsp://username:password@IP/port"
        stream = cv2.Videoframe(ip_camera)

    ret, frame = stream.read()

    #2
    while ret:

        ret, frame = stream.read()
        frame = read_barcodes_pyzbar(frame)
        cv2.imshow(title, frame)
        
        #3
        if cv2.waitKey(1) & 0xFF == 27:
                break

    # After the loop release the cap object
    stream.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
# End Function main


# Start Function read_barcodes
def testCameraDevice(source):
   test_capture = cv2.VideoCapture(source) 
   retValue = True
   if test_capture is None or not test_capture.isOpened():
       print('Warning: unable to open video source: ', source)
       retValue = bool(0)
   
   return retValue

def read_barcodes_pyzbar(frame):
    start_time = time.time()
    # barcodes = pyzbar.decode(frame,symbols=[ZBarSymbol.QRCODE])
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        print(barcode.type)
        if barcode is not None:
            x, y , w, h = barcode.rect
            #1
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 0, 255), 2)
            
            #2
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 0.5, (0, 0, 255), 1)
            #3
            # with open("c:\temp\barcode_result.txt", mode ='w') as file:
            #     file.write("Recognized Barcode:" + barcode_info)
            decode_time = round((time.time() - start_time)*1000,3)
            data_list.append(decode_time)
            print(barcode_info +" : --- %s millisecond ---" % decode_time)
    return frame
# End Function read_barcodes




# ----------MAIN----------

# Start __MAIN__
if __name__ == '__main__':

    os.system("cls")

    data_list = []

    main()

    list_len = int(len(data_list))
    if(list_len > 0):
        print("\r\n")
        print("Number of elements in the list: %i" % list_len)
        print("Minimum decode time: %i millisecond" % min(data_list))
        print("Maximum decode time: %i millisecond" % max(data_list))
        print("\r\n")

  
