# Convolutional Neural Network Deep Learning Project

This is a project where I built the LE-NET 5 Convolutional Neural Network Deep Learning Model to classify the MNIST Dataset. The project has two parts.   
There will be both an implementation using the Tensorflow API aswell as by scratch. 

## Project Overview

### Objective

The main goal of this project is to train a LE-NET 5 Convolutional Neural Network to classify the MNIST Dataset.  
A normal Neural Network will be utilised to compare against LE-NET 5.

### The MNIST Dataset

The MNIST (Modified National Institute of Standards and Technology) dataset is a widely used benchmark dataset in the field of machine learning and computer vision.  
It consists of a collection of 28x28 pixel grayscale images of handwritten digits (0 through 9).  
The dataset is divided into two main subsets: a training set with 60,000 images and a test set with 10,000 images.  
Each image is labeled with the corresponding digit it represents. 
Data was downloaded from here : http://yann.lecun.com/exdb/mnist/

### Features

- **data_ingestion_tools:** Toolkit used for data ingestion.
- **Model Implementation:** The LE-NET 5 Convolutional neural network model is implemented using Numpy and also using Tensorflow.
- **Visualization:** The results and performance of all models are visualized using Matplotlib.

## Project Structure

- **`data_ingestion_tools.py`:** Python Class to assist with Data Ingestion.
- **`cnnbsMNISTImplementation.ipynb`:** CNN vs NN by scratch.
- **`tensorflowMNISTImplementation.ipynb`:** CNN vs NN Using Tensorflow.

## Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/GIGACHADhoon/ConvNets.git
    cd ConvNets
    ```

2. **Install Dependencies:**

    ```bash
    pip install numpy
    pip install matplotlib
    pip install gzip
    pip install idx2numpy
    pip install pandas
    pip install tensorflow
    pip install sklearn
    ```

## Acknowledgments

This project was created as a weekend exploration and learning experience. Feel free to use, modify, or extend it for your own projects.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
