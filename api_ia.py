# -*- coding: utf-8 -*-
"""APi_IA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OnHMWwnorVn_s7mQBFeaZ-mjnIlE3T-W
"""

iphone sleep 2sec iphone sleep 2sec Nivea 2sec Miss dior 2sec Nivea 2sec iphone 2sec Miss dior 2sec nike 2sec samsung 2sec samsung

pip install boto3

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
List = ['Male','Female']

def Average(lst):
    return sum(lst) / len(lst)

import csv
import boto3

with open('credentials.csv', 'r') as input:
  next(input)
  reader = csv.reader(input)
  for line in reader:
    access_key_id = line[2]
    secret_access_key = line[3]

Gender = []
Glasses = []
Sunglasses = []
Age = []
Beard = []

for frame in frames:
  photo = frame
  Gender = []
  AgeR = []
  Age = []

  client = boto3.client('rekognition',
                        aws_access_key_id = access_key_id,
                        aws_secret_access_key = secret_access_key,
                        region_name = 'us-east-2')
  with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

  response = client.detect_faces(Image={'Bytes': source_bytes}, Attributes=['ALL'])

  for info in response['FaceDetails']:
    if info['Gender']['Confidence'] > 90:
      Gender.append(info['Gender']['Value'])
    AgeR.append(info['AgeRange']['Low'])
    AgeR.append(info['AgeRange']['High'])
  
  Age = [Average(AgeR)]
  CURRENT_MEAN_AGE = Age
  print(Age)
  if len(Gender)!=0 :
    print(most_frequent(Gender))
    CURRENT_MOST_GENDER = most_frequent(Gender)
  else :
    
    CURRENT_MOST_GENDER = 'Male'
    print(CURRENT_MOST_GENDER)

pip install opencv-python

count

import cv2
vidcap = cv2.VideoCapture('video3.mp4')
success,image = vidcap.read()
#count=0
while success:
  if count%50 == 0:
    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

framesv1 = ['frame0.jpg','frame50.jpg','frame100.jpg','frame150.jpg','frame200.jpg','frame250.jpg','frame300.jpg','frame350.jpg','frame400.jpg','frame450.jpg']

framesv2 = ['frame500.jpg','frame550.jpg','frame600.jpg','frame650.jpg','frame700.jpg','frame750.jpg','frame800.jpg','frame850.jpg','frame900.jpg','frame950.jpg','frame1000.jpg']

framesv3 = ['frame1050.jpg','frame1100.jpg','frame1150.jpg','frame1200.jpg','frame1250.jpg','frame1300.jpg','frame1350.jpg','frame1400.jpg']

import cv2

im = cv2.imread('frame0.jpg')

print(type(im))
# <class 'numpy.ndarray'>

print(im.shape)
print(type(im.shape))
# (225, 400, 3)
# <class 'tuple'>

imgHeight, imgWidth = (2160, 3840)  
    draw = ImageDraw.Draw(im)  
                    

    # calculate and display bounding boxes for each detected face       
    print('Detected faces for ' + photo)    
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        
        box = faceDetail['BoundingBox']
        left = imgWidth * box['Left']
        top = imgHeight * box['Top']
        width = imgWidth * box['Width']
        height = imgHeight * box['Height']
                

        print('Left: ' + '{0:.0f}'.format(left))
        print('Top: ' + '{0:.0f}'.format(top))
        print('Face Width: ' + "{0:.0f}".format(width))
        print('Face Height: ' + "{0:.0f}".format(height))

        points = (
            (left,top),
            (left + width, top),
            (left + width, top + height),
            (left , top + height),
            (left, top)

        )
        draw.line(points, fill='#00d400', width=2)

        # Alternatively can draw rectangle. However you can't set line width.
        #draw.rectangle([left,top, left + width, top + height], outline='#00d400') 

    image.show()

    return len(response['FaceDetails'])

import boto3
import io
from PIL import Image, ImageDraw, ExifTags, ImageColor

def show_faces(photo,bucket):
     

    client=boto3.client('rekognition')

    # Load image from S3 bucket
    s3_connection = boto3.resource('s3')
    s3_object = s3_connection.Object(bucket,photo)
    s3_response = s3_object.get()

    stream = io.BytesIO(s3_response['Body'].read())
    image=Image.open(stream)
    
    #Call DetectFaces 
    response = client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        Attributes=['ALL'])

    imgWidth, imgHeight = image.size  
    draw = ImageDraw.Draw(image)  
                    

    # calculate and display bounding boxes for each detected face       
    print('Detected faces for ' + photo)    
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        
        box = faceDetail['BoundingBox']
        left = imgWidth * box['Left']
        top = imgHeight * box['Top']
        width = imgWidth * box['Width']
        height = imgHeight * box['Height']
                

        print('Left: ' + '{0:.0f}'.format(left))
        print('Top: ' + '{0:.0f}'.format(top))
        print('Face Width: ' + "{0:.0f}".format(width))
        print('Face Height: ' + "{0:.0f}".format(height))

        points = (
            (left,top),
            (left + width, top),
            (left + width, top + height),
            (left , top + height),
            (left, top)

        )
        draw.line(points, fill='#00d400', width=2)

        # Alternatively can draw rectangle. However you can't set line width.
        #draw.rectangle([left,top, left + width, top + height], outline='#00d400') 

    image.show()

    return len(response['FaceDetails'])

def main():
    bucket="bucket"
    photo="photo"

    faces_count=show_faces(photo,bucket)
    print("faces detected: " + str(faces_count))


if __name__ == "__main__":
    main()