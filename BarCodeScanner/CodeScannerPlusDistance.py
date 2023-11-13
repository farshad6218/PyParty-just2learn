# ----------Imports----------

from collections import Counter
import numpy as np
import cv2
import imutils
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

    if not test_camera_device(vc_number):
        return

    #1
    title = "CAMERA"
    cv2.namedWindow(title, 1)

    if(vc_number == 0):
        stream = cv2.VideoCapture(vc_number)
    elif(vc_number == 1):
        ip_camera = "rtsp://username:password@IP/port"
        stream = cv2.Videoframe(ip_camera)

    ret, frame = stream.read()

    #2
    while ret:

        # barcode reader part
        ret, frame = stream.read()
        # frame = read_barcodes_pyzbar(frame)
        # cv2.imshow(title, frame)

        image, finalContours = get_contours(frame,showCanny=True,draw=False,filterShape=4,minArea=5000)
        cv2.imshow(title, image)

        if len(finalContours) != 0:
            # proxm
            biggest = finalContours[0][2]
            # print(biggest)
            w = 15
            h = 7
            imageWarp = warp_img(image,biggest,w,h)
            cv2.imshow("image Warp", imageWarp)


        #3
        if cv2.waitKey(1) & 0xFF == 27:
                break

    # After the loop release the cap object
    stream.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
# End Function main

# Start Function test_camera_device
def test_camera_device(source):
   test_capture = cv2.VideoCapture(source)
   retValue = True
   if test_capture is None or not test_capture.isOpened():
       print('Warning: unable to open video source: ', source)
       retValue = bool(0)

   return retValue
# End Function test_camera_device

# Start Function read_barcodes
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

# Start Function get_contours
def get_contours(image,cThr=[100,100],showCanny=False,minArea=10000,filterShape=0,draw=True):
    # convert the image to grayscale, blur it, and detect edges
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, cThr[0],cThr[1])
    if showCanny:
        cv2.imshow("The image canny", imgCanny)
    kernelSize = np.ones((5,5))
    imgDilate = cv2.dilate(imgCanny,kernelSize,iterations=3)
    contours,hierarchy = cv2.findContours(imgDilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    finalContours = []

    for i in contours:
        area = cv2.contourArea(i)
        if area > minArea:
            # get all information about detected object
            perimeter = cv2.arcLength(i,True)
            resulution = 0.02*perimeter
            approx = cv2.approxPolyDP(i,resulution,True)
            boundingBox = cv2.boundingRect(approx)

            if filterShape > 0:
                if len(approx) == filterShape:
                    newItem = len(approx),area,approx,boundingBox,i
                    finalContours.append( newItem )
            else:
                newItem = len(approx),area,approx,boundingBox,i
                finalContours.append(newItem)

    finalContours = sorted(finalContours,key = lambda x:x[1] ,reverse=True)
    if (draw):
        for con in finalContours:
            cv2.drawContours(image,con[4],-1,(0,0,255),1)


    return image, finalContours
# End Function get_contours

# Start Function reorder_image_corner
def reorder_rectangle_corner(imgPoints):
    print(imgPoints.shape) #(4 points,<1>,2 x,y)
    imgPointsNew = np.zeros_like(imgPoints)
    imgPoints = imgPoints.reshape((4,2)) #remove <1>
    add = imgPoints.sum(1)
    # recreate shape
    imgPointsNew[0] = imgPoints[np.argmin(add)]
    imgPointsNew[3] = imgPoints[np.argmax(add)]
    diff = np.diff(imgPoints,axis=1)
    imgPointsNew[1] = imgPoints[np.argmin(diff)]
    imgPointsNew[2] = imgPoints[np.argmax(diff)]

    return imgPointsNew



# End Function reorder_image_corner



# Start Function warp_img
def warp_img(image,points,w,h):
    # print(points)
    # print(reorder_rectangle_corner(points))
    point1 = np.float32(points)
    point2 = np.float32(([0,0],[w,0],[0,h],[w,h]))
    matrix = cv2.getPerspectiveTransform(point1,point2)
    imgWarp = cv2.warpPerspective(image,matrix,(w,h))

    return imgWarp
# End Function warp_img



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


