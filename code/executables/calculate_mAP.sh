cd ../Yolov3_d

if [ $# -eq 0 ]
  then
    echo "No arguments supplied, calculating default weights '../data/weights/config_1.weights'"
    ./darknet detector map ../data/config_files/config.data ../data/config_files/yolov3-tiny-obj.cfg ../data/weights/config_1.weights
    #./darknet detector map ../data/config_files/config.data ../data/config_files/yolov3-tiny-obj.cfg ../../saved_trainings/test_2/yolov3-tiny-obj_best.weights
elif [ $# -eq 1 ]
	then
    ./darknet detector map ../data/config_files/config.data ../data/config_files/yolov3-tiny-obj.cfg $1
else
	echo "Please run again and provide one argument with the image path you which to detect, or no argument to use default '../data/weights/config_1.weights'"
	echo "Available weights in '../data/weights/':"
	dir ../data/weights/
fi

