import cv2
import os
import random

test_cases = int(input("How many images?: "))
file_directory = input("Where are the files located (full path): ")
cwd = os.getcwd()

try:
    if(not os.path.exists("processed")):
        os.mkdir("processed")
    for filename in os.listdir(file_directory):
        f = os.path.join(file_directory, filename)
        img = cv2.imread(f, 1)
        for i in range(test_cases):
            match random.randint(1,10):
                case 1:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                case 2:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
                case 3:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_Lab2BGR)
                case 4:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_Lab2LBGR)
                case 5:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                case 6:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_Luv2LBGR)
                case 7:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                case 8:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_XYZ2RGB)
                case 9:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_XYZ2BGR)
                case 10:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
            cv2.imwrite(os.path.join(os.getcwd(), "processed", f"{filename}-sot-image-{i}.{os.path.splitext(filename)[1]}"), edited_img)
except:
    print("An error occurred!")

 