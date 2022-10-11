# Age_and_gender_detection_using_cnn
 This is the Capstone Project done under the JOVAC program by the GLA University. 

## What does this project covers?

* Train a CNN model on the popular UTKFace image dataset. The dataset covers more than 23k images to train the model.
* Using the model to Predict the age and gender of the person in the image

## How to run ?

* Clone the repository to your device by using git clone ```https://github.com/yashpathakcs/Age_and_gender_detection_using_cnn.git``` command.
* Download the required modules mentioned in the ``Requirements.txt`` file.
* Run the ``Train.ipynb`` file.
* Run the ``Predict.ipynb`` file and specify the path to your image in the file.
* Run the ``Webcam-demo.py`` file for live feed.

### Platform used :

The platform used for building this project is Kaggle, since it provides easier access to a wide variety of datasets including the UTKFace as well as lets you use their GPU to train your model.

### Important Links:

UTKFace Dataset : ```https://drive.google.com/file/d/0BxYys69jI14kYVM3aVhKS1VhRUk/view?resourcekey=0-dabpv_3J0C0cditpiAfhAw```

Model = ```https://drive.google.com/drive/folders/1S89dsEglBfcJoY2UH-Zdj6tbdGbBjYsX?usp=sharing```

### Important Note :
If you wish to train the model use GPU for execution as it is much faster, do not use the CPU. 
If you do not have a GPU use Google Colab or Kaggle or any other online platform that lets you use their GPU.

### Other informations:
* The GPU used to train the model is Kaggle's Nvidia K80.
* The approximate time taken to train the model to 50 epochs was 2 hours.
* Since the files are made on kaggle you might want to change the paths specified in the files, as per your device.
* If you use the Anaconda Navigator, make a new environment and in that environment install ipykernal, tensorflow-gpu and the jupyter notebook.
* You also need to download the CUDA toolkit and cudnn files in your system to use the GPU in jupyter notebook. Procedures can be found on the youtube.
