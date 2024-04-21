import os
import cv2

path = "Images/"

Images = []

for i in os.listdir(path):
    name,extension = os.path.splitext(i)
    if extension in [ '.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path + '/' + i
        Images.append(file_name)

count = len(Images)
        
frame = cv2.imread(Images[0]) 
height,width,channels = frame.shape
size = (width,height)
        
out = cv2.VideoWriter('Projectfriendship.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for j in range(0,count-1):                                          
    frame = cv2.imread(Images[j])
    out.write(frame)
        
out.release()
print("Done!")