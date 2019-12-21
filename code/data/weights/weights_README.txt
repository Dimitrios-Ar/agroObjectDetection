TESTING:
To be used to test images, videos and mean Average Precision of model.
config_1.weights : weights after training with youtube and google data.      -filtered_400_TRAINING_YT_100-
config_2.weights : weights after training with youtube and goole data and also some images from randers_nov folder (recordings in randers on november). The Randers_nov data have been augmented with equalized images and rotated images. - augmented_only_on_Randers_NOV_filtered_400_TRAINING_YT_100_NOV -

TRAINING:
yolov3-tiny.conv.15 : to be used once starting training tiny yolo
darknet53.conv.74 : to be used once starting training full yolo
last_training_weights folder is used when training on new data. The weights for different iterations of training procedure are saved inside this folder.