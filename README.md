# Computer Vision RPS

> This is an implementation of the classic rock, paper, scissors game that allows you to compete with your computer. Through your computer's camera, this application utilises a deep-learning model (Keras) that recognises the user's hand gestures. All you have to do is run the program, display your choice in front of the camera, and a winner will be determined. Almost like playing with another human! A manual version is also available, where the user is prompted to type in a choice (for those of you who are camera shy!)

## System Requirements

You **MUST** have the following installed for this to work:

- Python 3
- Tensorflow
- OpenCV-Python

### About the Deep Learning Model

The Keras model was trained using a total sample size of 5000 images. A thousand for each possible hand gesture (rock, paper, scissors) and a thousand images where no hand gesture was presented (this is so the program knows that the user has not given a choice). The model produces predictions that are 90 - 100% accurate. 

