additional_features: Different features used as tools to accelerate and improve object detection.

data: All configuration files, images/videos to test the detector on, and weights of different trainings.

executables: Shell executable files for training, testing detector on images/videos and calculate mean Average precision

Yolov3_d: The core part of the object detector


General information/use: (This project is based on https://github.com/AlexeyAB/darknet. For more information on installation or usage, refer to that)

Only for the first time, move into the Yolov3_d directory. Run 'make' inside the directory. (CUDA GPU and OPENCV are required)

To run the detector for testing, some configuration files and weights based on previous trainings need to be provided.
The configuration files needed for testing are 'config_data' which contains information on objects/classes and the yolov3-...-obj.cfg which is used to differentiate between full Yolov3 or tiny Yolov3
The weights contain what the detector learned during the training. The correct weights need to be provided depending on tiny or full yolov3 

Move into the executables folder run:

./detect_image.sh {OPTIONAL_ARGUMENT} 
(By providing an image location the detector will predict on that image. Otherwise, a default image will be loaded)

./detect_video.sh {OPTIONAL_ARGUMENT} 
(By providing a video location the detector will predict on that video. Otherwise, a default video will be loaded)

Inside the above files, different parameters can be set (weights,configuration files, etc).