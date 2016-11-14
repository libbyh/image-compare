import cv2
import numpy
import glob
import pandas as pd

# Used this: http://miriamposner.com/classes/medimages/3-use-opencv-to-find-the-average-color-of-an-image/

# where are the images?
path = "images/*.jpg"
# create an empty dictionary in which to store image info
images = {}
# loop through all the images in the file
for fname in glob.glob(path):
    # get the BGR info for each pixel in the image
    img = cv2.imread(fname)
    # get average BGR for each row of pixels
    avg_row = numpy.average(img, axis=0)
    # get average BGR for images by averaging the rows
    avg_color = numpy.uint8(numpy.average(avg_row, axis=0))
    # store the average BGR of the image in the dictionary
    images[fname] = avg_color.tolist()
   
# create dataframe from dictionary where index is the file name, cols are BGR
img = pd.DataFrame.from_dict(data=images, orient='index')
# name the columns
img.columns = ['blue', 'green', 'red']
# show us some data so we know we have the right stuff
print(img.head())
# print summary statistics for the data
print(img.describe())