# Brain Tumor MRI Detection using YOLOv8

This project implements a Brain Tumor MRI Detection system using the YOLOv8 model. The workflow includes data preparation, model training, and deployment through a Tkinter application and a Flask web application. The entire process is documented in a Jupyter Notebook for ease of understanding and reproducibility.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Training the Model](#training-the-model)
  - [Deploying the Model](#deploying-the-model)
    - [Tkinter Application](#tkinter-application)
    - [Flask Web Application](#flask-web-application)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Brain tumors are a critical health issue, and early detection is crucial for effective treatment. This project leverages the YOLOv8 model, a state-of-the-art object detection algorithm, to identify brain tumors from MRI scans. The project is implemented in Python and provides both a desktop and web interface for users to interact with the model.

## Dataset

The dataset used for this project consists of MRI scans labeled for the presence of brain tumors. You can download the dataset from [Kaggle](https://www.kaggle.com/) or any other open-source medical image repository. Ensure that the dataset is organized in a format compatible with YOLOv8 training requirements.
The dataset I personally used : [My dataset](https://www.kaggle.com/datasets/ahmedsorour1/mri-for-brain-tumor-with-bounding-boxes)

## Requirements

- Python 3.7+
- Jupyter Notebook
- TensorFlow or PyTorch (depending on the YOLOv8 implementation)
- OpenCV
- Tkinter
- Flask
- Other dependencies specified in `requirements.txt`

## Project Structure
Brain-Tumor-Detection/
├── dataset/                 # Directory containing the MRI dataset
├── brain_tumor_detection.ipynb
├── tkinter.py
├── webapp/                  # Flask web application code
│   ├── static/
│   ├── templates/
├── app.py
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

## Installation

### Clone the repository

```bash
git clone https://github.com/aPassie/Brain_Tumor_MRI_modeltest11.git
cd Brain-Tumor-Detection
```
### Install the required packages
```bash
pip install -r requirements.txt
```

## Usage

### Training the Model
1. Open the Jupyter Notebook:
```bash
jupyter notebook final2/Brain_Tumor_MRI_Detection.ipynb
```
2. Follow the instructions in the notebook to preprocess the data, configure the YOLOv8 model, and train it using the dataset.

### Deploying the Model
#### Tkinter Application
1. Run the Tkinter application:
```bash
python tkinter.py
```
2. Use the GUI to upload MRI images and get predictions.

#### Flask Web Application
1. Start the Flask server:
```bash
python app.py
```
2. Open your web browser and navigate to http://127.0.0.1:5000 to use the web interface.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details

