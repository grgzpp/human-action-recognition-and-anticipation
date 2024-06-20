# Recognition and anticipation of human actions in a human-robot collaborative assembly scenario

This project aims to make human-robot collaboration more natural and intuitive by accurately recognizing, predicting and anticipating human actions in a collaborative assembly scenario, using the neural network architectures developed.

This project has been developed as part of my master's thesis work. The results of the experiments, including model performance metrics and visualizations, are documented in the thesis. I will add a link so you can consult it as soon as it is completed.

## Project Overview Video

[![Project Overview Video](https://img.youtube.com/vi/grU0Z88kiMg/0.jpg)](https://www.youtube.com/watch?v=grU0Z88kiMg)

## Introduction

This project focuses on developing, training and evaluating two neural network models for recognizing and predicting human actions in real-time to facilitate effective human-robot collaboration. The primary goals are:
- To accurately recognize a set of human actions.
- To predict subsequent human actions based on current observations.
- To make the robot perform the predicted actions to anticipate the human, to improve collaboration in a natural and intuitive way.

## Project Structure

The repository is organized as follows:

```
.
├── weights/
│   ├── model_ap.pt
│   ├── model_ar_bilstm.pt
│   ├── model_ar_complex_lstm.pt
│   ├── model_ar_conv1d.pt
│   ├── model_ar_lstm_objects.pt
│   ├── model_ar_simple_lstm.pt
│   └── yolov9c_fine_tuned.pt
├── robot_program.ipynb
├── action_prediction_model_train.ipynb
├── action_recognition_model_train.ipynb
├── data_acquisition.ipynb
├── yolo_train.ipynb
├── local_landmark.py
├── realsense_camera.py
├── robot_controller.py
├── camera_calibration.m
├── README.md
└── requirements.txt
```

## Setup

To get started, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/grgzpp/human-action-recognition-and-anticipation.git
pip install -r requirements.txt
```

## Dependencies

The project relies on the following major dependencies:

- [PyTorch](https://pytorch.org/)
- [MediaPipe](https://mediapipe.dev/)
- [YOLO v9 (ultralytics)](https://docs.ultralytics.com/models/yolov9/)
- [numpy](https://numpy.org/)
- [opencv](https://opencv.org/)
- [pandas](https://pandas.pydata.org/)
- [tqdm](https://tqdm.github.io/)

and for model evaluation and visualization:

- [matplotlib](https://matplotlib.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [seaborn](https://seaborn.pydata.org/)
- [torchinfo](https://github.com/TylerYep/torchinfo)

You can install them via `requirements.txt` file (recommended) or manually using pip.

The project also depends on the [iiwaPy3](https://github.com/Modi1987/iiwaPy3) library to control the KUKA iiwa robot and on the [object tracker](https://github.com/grgzpp/yolo-mp-object-tracker) I developed specifically for this application. Make sure to install both before using the program.

## Usage

The main program used for the autonomous real-time implementation is *robot_program.ipynb*. This connects the robot and the camera, uses both models developed for action recognition and prediction, and commands the robot to anticipate them.

### Training and Evaluation

#### Action Recognition Model

The notebook *action_recognition_model_train.ipynb* contains the functions used to train and evaluate the action recognition model.

#### Action Prediction Model

The notebook *action_prediction_model_train.ipynb* contains the functions used to train and evaluate the action prediction model.

## Datasets

The dataset used to train the action recognition model has been built with data acquired using the *data_acquisition.ipynb* notebook. The dataset to train the action prediction model was also built; the functions used can be found in *action_prediction_model_train.ipynb*.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.