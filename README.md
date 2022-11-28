# Semester project - Object detection in agricultural environment
### Report can be found on files or online here: https://drive.google.com/file/d/12gkcoYX8QvJfVZ3jbeg8iklrug8QqA7b/view?usp=share_link

## Yolov3 and TinyYolov3 for Linux
### This repository is based on https://github.com/AlexeyAB/darknet and https://github.com/AlexeyAB/darknet

* Requirements
* Installation
* How to use
* Datasets

#### Requirements (copied from https://github.com/AlexeyAB/darknet)

* **Linux**
* **CMake >= 3.8** for modern CUDA support: https://cmake.org/download/
* **CUDA 10.0**: https://developer.nvidia.com/cuda-toolkit-archive (on Linux do [Post-installation Actions](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions))
* **OpenCV >= 2.4**: use your preferred package manager (brew, apt), build from source using [vcpkg](https://github.com/Microsoft/vcpkg) or download from [OpenCV official site](https://opencv.org/releases.html) (on Windows set system variable `OpenCV_DIR` = `C:\opencv\build` - where are the `include` and `x64` folders [image](https://user-images.githubusercontent.com/4096485/53249516-5130f480-36c9-11e9-8238-a6e82e48c6f2.png))
* **cuDNN >= 7.0 for CUDA 10.0** https://developer.nvidia.com/rdp/cudnn-archive (on **Linux** copy `cudnn.h`,`libcudnn.so`... as desribed here https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installlinux-tar , on **Windows** copy `cudnn.h`,`cudnn64_7.dll`, `cudnn64_7.lib` as desribed here https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installwindows )
* **GPU with CC >= 3.0**: https://en.wikipedia.org/wiki/CUDA#GPUs_supported
* on Linux **GCC or Clang**, on Windows **MSVC 2015/2017/2019** https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community

#### Installation

Navigate inside 'code/Yolov3_d' directory and run `make`.

#### How to use

Navigate inside 'code/executables' directory. 

* **Test on image**: Run `./detect_image.sh` to test on default image, or `./detect_image.sh image_path` for any image. 

* **Test on video**: Run `./detect_video.sh` to test on default video, or `./detect_video.sh video_path` for any video. 

* **Test on multiple images**: Run `./detect_multiple_images.sh` to test on default multiple images, or `./detect_multiple_images.sh txt_file_path` to run by reading a .txt file that contains multiple paths of images. 

Some sample images and videos exist inside 'code/data/test_files' directory. The image/video paths are relative to 'code/Yolov3_d' directory. (ex. to run on image image1.jpg which is located inside the 'code/data/test_files' directory, one should provide the path '../data/test_files/image1.jpg')

#### Datasets

Link for dataset: To be uploaded

To use the tools created to augment the dataset and to use the dataset for training the suggested location of the 'dataset' directory would be in the same directory as the 'code':

* Main_folder
    * code
        * additional_features
        * data
        * executables
        * README.txt
        * Yolov3_d
    * dataset
        * randers_nov
        * randers_sep
        * yt_and_google_data
