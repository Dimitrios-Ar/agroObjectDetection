cd ../Yolov3_d

if [ $# -eq 0 ]
  then
    echo "No arguments supplied, running tinyYolov3 on default '../data/test_files/randers_tractor.mp4' video"
    ./darknet detector demo ../data/config_files/config.data ../data/config_files/yolov3-tiny-obj.cfg ../data/weights/config_1.weights -ext_output ../data/test_files/randers_tractor.mp4
elif [ $# -eq 1 ]
	then
    ./darknet detector demo ../data/config_files/config.data ../data/config_files/yolov3-tiny-obj.cfg ../data/weights/config_1.weights -ext_output $1
else
	echo "Please run again and provide one argument with the video path you which to detect, or no argument to use default '../data/test_files/randers_tractor.mp4'"
fi