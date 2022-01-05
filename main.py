# # # # This is a sample Python script.
# # #
# # # # Press ⌃R to execute it or replace it with your code.
# # # # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# # #
# # #
# # # def print_hi(name):
# # #     # Use a breakpoint in the code line below to debug your script.
# # #     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
# # #
# # #
# # # # Press the green button in the gutter to run the script.
# # # if __name__ == '__main__':®®
# # #     print_hi('PyCharm')
# # # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# import cv2
# import face_recognition
# import face_recognition as fr
# import numpy as np
#
# print("Package imported")
#
# imgbill = face_recognition.load_image_file('ImagesRegistered/billgates.jpeg')
# # img = cv2.imread("/Users/achiyant/Downloads/Narendarmodi.jpeg")
# imgbill = cv2.cvtColor(imgbill, cv2.COLOR_BGR2RGB)
#
# imgbill_test = face_recognition.load_image_file('ImagesRegistered/billgates_test.jpeg')
# imgbill_test = cv2.cvtColor(imgbill_test, cv2.COLOR_BGR2RGB)
#
# faceLocation = face_recognition.face_locations(imgbill)[0]
# encodeBill = face_recognition.face_encodings(imgbill)[0]
# #top,right,bottom,left
# cv2.rectangle(imgbill, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]), (58, 255, 38), 2)
#
# faceLocationTest = face_recognition.face_locations(imgbill_test)[0]
# encodeBillTest = face_recognition.face_encodings(imgbill_test)[0]
# cv2.rectangle(imgbill_test, (faceLocationTest[3], faceLocationTest[0]), (faceLocationTest[1], faceLocationTest[2]), (58, 255, 38), 2)
#
# # print(encodeBill)
# # print("*************************")
# # print(encodeBillTest)
#
# results = face_recognition.compare_faces([encodeBill], encodeBillTest)
# faceDist = face_recognition.face_distance([encodeBill], encodeBillTest)
# cv2.putText(imgbill_test, f'{results} {round(faceDist[0], 2)}', (0, 30), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.5, (0, 255, 255), 1)
# print(results)
# print(faceDist)
#
# cv2.imshow('Bill Gates', imgbill)
# cv2.imshow('Bill Gates Test', imgbill_test)
# cv2.waitKey(0)
#
#
# # from imutils import paths
# # import face_recognition
# # import pickle
# # import cv2
# # import os
# #
# # # get paths of each file in folder named Images
# # # Images here contains my data(folders of various persons)
# # imagePaths = list(paths.list_images('images_basic'))
# # knownEncodings = []
# # knownNames = []
# # # loop over the image paths
# # for (i, imagePath) in enumerate(imagePaths):
# #     # extract the person name from the image path
# #     name = imagePath.split(os.path.sep)[-2]
# #     # load the input image and convert it from BGR (OpenCV ordering)
# #     # to dlib ordering (RGB)
# #     image = cv2.imread(imagePath)
# #     rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# #     # Use Face_recognition to locate faces
# #     boxes = face_recognition.face_locations(rgb, model='hog')
# #     # compute the facial embedding for the face
# #     encodings = face_recognition.face_encodings(rgb, boxes)
# #     # loop over the encodings
# #     for encoding in encodings:
# #         knownEncodings.append(encoding)
# #         knownNames.append(name)
# # # save emcodings along with their names in dictionary data
# # data = {"encodings": knownEncodings, "names": knownNames}
# # # use pickle to save data into a file for later use
# # f = open("face_enc", "wb")
# # f.write(pickle.dumps(data))
# # f.close()
# #
import numpy as np
import cv2


def draw_border(img, pt1, pt2, color, thickness, r, d):
    x1,y1 = pt1
    x2,y2 = pt2

    # Top left
    cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)

    # Top right
    cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)

    # Bottom left
    cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)

    # Bottom right
    cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)

# ============================================================================

img = np.zeros((256,256,3), dtype=np.uint8)

draw_border(img, (10,10), (100, 100), (127,255,255), 1, 10, 20)
draw_border(img, (128,128), (240, 160), (255,255,127), 1, 5, 5)

cv2.imwrite('round_rect.png', img)
