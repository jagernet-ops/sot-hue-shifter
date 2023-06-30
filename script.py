import cv2
import os
import random

test_cases = int(input("How many images?: "))
file_directory = input("Where are the files located (full path): ")

try: 
    for filename in os.listdir(file_directory):
        f = os.path.join(file_directory, filename)
        img = cv2.imread(f, 1)
        for i in range(test_cases):
            match random.randint(1,10):
                case 1:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                    cv2.imwrite(f"{filename}-sot-image-{i}.{os.path.splitext(filename)[1]}", edited_img)
                case 2:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
                    cv2.imwrite(f"{filename}-sot-image-{i}.{os.path.splitext(filename)[1]}", edited_img)
                case 3:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_Lab2BGR)
                    cv2.imwrite(f"{filename}-sot-image-{i}.{os.path.splitext(filename)[1]}", edited_img)
                case 4:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_Lab2LBGR)
                    cv2.imwrite(f"{filename}-sot-image-{i}.{os.path.splitext(filename)[1]}", edited_img)
                case 5:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV_I420)
                    cv2.imwrite(f"{filename}-sot-image-{i}.{os.path.splitext(filename)[1]}", edited_img)
                case 6:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_Luv2LBGR)
                    cv2.imwrite(f"{filename}-sot-image-{i}.{os.path.splitext(filename)[1]}", edited_img)
                case 7:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    cv2.imwrite(f"{filename}-sot-image-{i}.{os.path.splitext(filename)[1]}", edited_img)
                case 8:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_XYZ2RGB)
                    cv2.imwrite(f"{filename}-sot-image-{i}.{os.path.splitext(filename)[1]}", edited_img)
                case 9:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_XYZ2BGR)
                    cv2.imwrite(f"{filename}-sot-image-{i}.{os.path.splitext(filename)[1]}", edited_img)
                case 10:
                    edited_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
                    cv2.imwrite(f"{filename}-sot-image-{i}.{os.path.splitext(filename)[1]}", edited_img)
except:
    print("An error occurred!")

