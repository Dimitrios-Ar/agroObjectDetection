Different features used as tools to accelerate and improve object detection.

augment_data: Randomly applies contrast limited adaptive histogram equalization or rotation on some images. Also, handles changes in bounding boxes in case of rotation.
To use augment_data: create a folder called 'data_augmentation' and inside that folder, create a new folder 'original_photos'. Place the images inside 'data_augmentation/original_photos/'

class_counter: Counts instances of each class in the dataset
The usage of class_counter can be done either on the test and train of config_data, or on any folder containg annotations.

class_removal: Removes a specific class from dataset

cvat_format: Creates the .zip file for importing annotations into CVAT annotation tool

delete_non_annotated: Deletes any images that are not annotated

detected_annotations_converted: Converts predictions of the detector on new images into proper annotation txt files

detection_preparer: Creates the txt file that will be feeded to the detector for new images

filter_annotations: Filters annotations based on size of bounding box (pixels).

google_images_rename_to_jpg: Renames and converts all downloaded google images into jpg. Also checks filters out small images.

move_files_folders: Moves or copies files or folders from a destination to another (sometimes the file manager crasheswhen trying to copy hundreds of images and txt files). For that reason this script exists.

save_trainings: Saves important files of last training for later use.

test_train_files_creator: Creates the test and train txt files based on the dataset.

youtube_downloader: Saves frames of youtube video to be used as training/testing data.