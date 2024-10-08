# Conversion of Pakistan Sign Language into text and speech using Machine Learning
[Government College University Faisalabad (Department of CS)](https://gcuf.edu.pk/) (Fall 2016 – 2020) - Final Year Project

#### The project is divided into 3 main modules
- RealTime sign detection module - convert Pakistan Sign Language (PSL) alphabet and words into text and speech in realtime.
- Capture Dataset module - Automated system for capturing and adding new data to the dataset
- PSl learning module - Learn PSL interactively

## Dependencies
##### The system uses [OpenPose v1.5.0](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases) library for extacting skelatal features.
##### The code was developed with python 3.7 and has been tested with the libraries/versions in requirements.txt file.

## Dataset Used
We have made our own Pakistan Sign Language (PSL) dataset containing multiple samples of 37 urdu aplhabets and 12 urdu words. The dataset is made publically available at: https://www.kaggle.com/saadbutt321/pakistan-sign-language-dataset

## External resources
OpenPose GitHub repo: https://github.com/CMU-Perceptual-Computing-Lab/openpose
Origin of OpenPose: https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation
Paper describing the method: https://arxiv.org/abs/1611.08050
Keras implementation of the Realtime Multi-Person Pose Estimation (my major inspiration): https://github.com/michalfaber/keras_Realtime_Multi-Person_Pose_Estimation.
