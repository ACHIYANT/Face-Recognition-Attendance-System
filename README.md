
# Face Recognition Attendance System

## Abstract

<p align="justify">The primary goal of this project is to create a facial recognition-based attendance monitoring system for educational institutions in order to improve and modernise the present attendance system to make it more efficient and effective than previously. The present outdated approach is riddled with ambiguity, resulting in incorrect and wasteful attendance taking. Many issues develop when the authority is unable to enforce the previous system's regulations. The facial recognition system will be the technology at work. The human face is one of the natural characteristics that may be used to individually identify a person. As a result, it is utilised to track identification because the chances of a face deviating or being replicated are limited. Face databases will be established in this project to provide data into the recognizer algorithm.<br/>
Then, during the attendance taking session, faces will be matched to the database in order to determine identify. When a person is identified, his or her attendance is immediately recorded, and the essential information is saved in an CSV file. Very Soon I will be use MongoDB ATLAS as database to store the information. The facial recognition system will be the technology at work. The human face is one of the morphological attractions that can be used to distinctively verify identity. As a result, it is utilised to track identification because the chances of a face deviating or being cloned are limited. Face databases will be built in this project to provide data into the recognition algorithm. When student successfully marked attendance then they got the automated confirmation mail to verify that they have successfully month attendance.
</p>

 
## Project Introduction and Motivation Project Introduction
<p align="justify">
This is a face recognition attendance system using Python. In this project I have using the dlib library , face_recognition library, open CV, numpy library and more libraries to run this project successfully. I have using the PyCharm IDE for making project. This project is based on the deep learning model. In this project firstly we will make the student record for making attendance later. For verifying face of different students we need there photos so that later they can be verified by the live web cam. This model works by developing the encodings of the images ,firstly it will generate the encoding of the already saved image and then generate the encoding of the live web cam face encoding if both encoding matches then it will return us true that yes the database image and the live web cam face get matched . then it register that attendance at the designated folder.<br/>
The most critical consequence, according to the existing attendance management system, is the accuracy of the data collected. This is because attendance may not be recorded precisely by the original person; in other words, a specific person's attendance may be collected by a third party without the institution's consent, which violates the integrity of the data. For example, if student A is too sluggish to attend a certain class, student B will assist him/her in signing for attendance, despite the fact that student A did not attend the class, but the system will ignore this problem owing to lack of enforcement. If the institution establishes enforcement, it may have to squander a lot of people resources and time, which is not feasible at all. As a result, all of the old system's reported attendance is untrustworthy for analytical purposes.
The old system's second flaw is that it is complicated or time intensive. Assuming that the time that it takes a person to sign his or her name on a 3-4 paged name list is roughly one minute. Only about 60 people can sign their attendance in one hour, which is plainly wasteful and time consuming. The third problem is the genuine concerned party's ability to obtain such information. For example, most parents are quite worried about tracking their child's actual locations to ensure that their youngster actually attends college/school lessons. However, there are no options for parents to get such information in the old system.<br/>
As a result, development of the previous system is required to increase efficiency, data quality, and offer access to information for those lawful parties.</p>


## Motivation
<p align="justify">
Motivation behind this project is my passion towards the Machine learning ,deep learning and the artificial intelligence. I am too much curious about how the machine do the all works ,those works done by human in such long period of time how nowadays machine doing that work in the limited time, with the real time updates. So this passion provide me the motivation to complete this project.<br/>
Again, Motivation and the knowledge provided by my Resource mam highly motivated me for doing this project. The different ideas provided by mam make this project more interesting and attract mind towards this project.</p>

## Methodology Followed
<p align="justify">
Face detection is the initial stage in our pipeline. Obviously, we must first discover the faces in a snapshot before attempting to distinguish them!<br/>
To detect faces in a picture, we'll first convert it to black and white because we don't require colour data to do so.<br/>
Then we'll examine each pixel in our image one by one. We want to look at the pixels that are directly surrounding each pixel. Our objective is to determine how dark the current pixel is in comparison to the pixels immediately around it. Then we'll create an arrow to demonstrate which way the image is becoming darker. If you repeat that procedure for every pixel in the image, every pixel will be replaced by an arrow. These arrows are known as gradients, and they depict the transition from bright to dark across the page.<br/>
We will employ a technique known as facial landmark estimation. There are other approaches to this, but we will adopt the one developed in 2014 by Vahid Kazemi and Josephine Sullivan.<br/>
The main concept is that we will identify 68 precise spots (called landmarks) on every face, such as the tip of the chin, the outer edge of each eye, the inside edge of each brow, and so on. Then, we'll train a machine learning system to locate these 68 particular locations on any face.<br/>
So all we have to do is feed our face photos into their pre-trained network to retrieve the 128 measures for each face. Here are the dimensions for our test image.
To construct a reduced version of an image, encode it with the HOG algorithm. Find the portion of the picture that most closely resembles a general HOG encoding of a face using this simplified image.<br/>
    
Find the primary landmarks in the face to determine the face's position. Once we've located those landmarks, we can utilise them to distort the picture to centre the eyes and mouth.<br/>
Run the centred face picture through a neural network that understands how to measure facial traits. Keep track of the 128 measurements.<br/>
Examine all of the faces we've already examined to find who's measurements are the most similar to ours.<br/>
</p>



## Screenshots

#### Login Page
![Screenshots/Screenshot 2021-12-25 at 10.48.17 PM.png](https://github.com/ACHIYANT/Face-Recognition-Attendance-System/blob/f755da3336021569abfa757d624c7c1ffaea8740/Screenshots/LoginPage.png)

#### SignUp
![Screenshots/Screenshot 2021-12-25 at 10.48.17 PM.png](https://github.com/ACHIYANT/Face-Recognition-Attendance-System/blob/f755da3336021569abfa757d624c7c1ffaea8740/Screenshots/SignUp.png)

#### Forget Password
![Screenshots/Screenshot 2021-12-25 at 10.48.17 PM.png](https://github.com/ACHIYANT/Face-Recognition-Attendance-System/blob/f755da3336021569abfa757d624c7c1ffaea8740/Screenshots/ForgetPwd.png)

#### Terminal Window
![Screenshots/Screenshot 2021-12-25 at 10.48.17 PM.png](https://github.com/ACHIYANT/Face-Recognition-Attendance-System/blob/f755da3336021569abfa757d624c7c1ffaea8740/Screenshots/TerminalWindow.png)

#### Webcam Window
![Screenshots/Screenshot 2021-12-25 at 10.48.17 PM.png](https://github.com/ACHIYANT/Face-Recognition-Attendance-System/blob/f755da3336021569abfa757d624c7c1ffaea8740/Screenshots/WebcamWindow.png)


#### Not Eligible Error

Screenshot of one of the feature that if you logged in with one student account you can’t mark the attendance of another student :-

![Screenshots/Screenshot 2021-12-25 at 10.48.17 PM.png](https://github.com/ACHIYANT/Face-Recognition-Attendance-System/blob/f755da3336021569abfa757d624c7c1ffaea8740/Screenshots/NotEligibleError.png)


#### Mail Confirmation

As in below screen shot Account is logged in with the credentials of Tim Cook but in the image there is Steve Jobs So it shows the error that you are not the eligible person for this account.

![Screenshots/Screenshot 2021-12-25 at 10.48.17 PM.png](https://github.com/ACHIYANT/Face-Recognition-Attendance-System/blob/f755da3336021569abfa757d624c7c1ffaea8740/Screenshots/MailScreenshot.png)


  
 


 
## References
• https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78

• https://scholar.google.com/citations?view_op=view_citation&hl=en&user=3NztoZAAAAAJ&citation_for_view=3NztoZAAAAAJ:u5HHmVD_uO8C

• https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/

• https://www.analyticsvidhya.com/blog/2021/06/learn-how-to-implement-face-recognition-using-opencv-with-python/

• https://face-recognition.readthedocs.io/en/latest/readme.html

