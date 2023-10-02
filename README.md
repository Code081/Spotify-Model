# Spotify-Model
This model recognizes your facial expressions and trains on the data provided on Kaggle for fer 2013. This project refers to the notebook Detect Mood & Recommend Music from Saurabh Kumar on Kaggle. 
I have made a few changes to the notebook and successfully ran it on my system. 
I also tried a different approach of taking input for the mood from the user manually and scraping data from lyrics of songs using the Genius API and recommending songs based on the user input which then provides data to the Spotify model.

## To Run the Final Model 
- open the emotion-based-music-recommender-resnet50v2.ipynb
- run all of the code blocks
- you will need Tensorflow, numpy, pandas, keras, matplotlib, sklearn, cv2 as prerequisits to run the model.
- if you wish to run the model on a local machine you can use Miniconda and enable External GPU support using a Conda Virtual environment on WSL2 on Windows.

The project uses a dataset from Kaggle called fer 2013, which contains 35,887 grayscale images of human faces with seven emotion labels1.
The project uses a ResNet50V2 model, which is a deep convolutional neural network that can achieve high accuracy on image classification tasks2.
The project also uses Streamlit, which is an open-source framework that allows users to create and share web applications for machine learning and data science3.
