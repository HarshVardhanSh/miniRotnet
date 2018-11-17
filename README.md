# miniRotnet
Inspired from Rotnet, I implemented VGG16 + LogisticRegressionClassifier to detect orientation of images (Indoor CVPR dataset) but only limited to four angles ie. 0, 90, 180, 270 and correct them. 

Files included in the project folder:
1. create_dataset.py: The script randomly selects 10000 images from the CVPR dataset, rotates them by randomly selected angle and stores them into the disk.

2. extract_features.py: This script uses pretrained VGGNet for extracting features from the images and stores them with the help of HDF5DataWriter in to h5py format.

3. train_mode.py: This script intializes the logistic classifier and trains it for four class classification and stores the model pickle in models folder.

4. orient_images.py: This script finally orient the test images. 

The results of the VGG16+Logregclassifiers on test data are :
precision: 93%, recall: 93% and F1-score: 93% 
