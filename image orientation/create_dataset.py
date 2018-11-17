#importing the necessary packages
from imutils import paths 
import numpy as np
import progressbar
import argparse
import imutils
import random 
import cv2
import os


# construct the argument parser and pass the arguments 
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, 
                help = "path to input directory of images")
ap.add_argument("-o", "--output", required = True, 
               help = "path to output ratated images")
args = vars(ap.parse_args())

# sample 10000 images and create training and testing dataset
imagePaths = list(paths.list_images(args ["dataset"]))[:10000]
random.shuffle(imagePaths)

# initialize a dictionary to keep track of number of each angle
# chosen so far, then initialize the progress bar
angles = {}
widgets = ["Building Dataset: ", progressbar.Percentage(), " ",
           progressbar.Bar(), " ", progressbar.ETA()]
pbar = progressbar.ProgressBar(maxval=len(imagePaths), 
                               widgets=widgets).start()

# now we have our sampled image path we are ready to 
# create our rotated image dataset
for (i, imagePath) in enumerate(imagePaths):
  # determine rotation angle and load the image
  angle = np.random.choice([0, 90, 180, 270])
  image = cv2.imread(imagePath)
  
  if image is None:
    continue
  
  # rotate the image to randomly selected angle and construct
  # the path to the base output directory
  image = imutils.rotate_bound(image, angle)
  base = os.path.sep.join([args["output"], str(angle)])
  
  # if the base path doesn't exist already create it 
  if not os.path.exists(base):
    os.makedirs(base)
  
  # extract the image file extension, then construct the full path
  # to the output file
  ext = imagePath[imagePath.rfind(".") :]
  outputPath = [base, "image_{}{}".format(str(angles.get(angle, 0)).zfill(5), ext)]
  outputPath = os.path.sep.join(outputPath)
  
  #save the image
  cv2.imwrite(outputPath, image)
  
  # update the count for the angle
  c = angles.get(angle, 0)
  angles[angle] = c + 1 
  pbar.update(i)
  
  #finish the progress bar
  pbar.finish()
  
  # loop over the angles and display counts for each of them
  for angle in sorted(angles.keys()):
  print("[INFO] angle={}: {:,}".format(angle, angles[angle]))