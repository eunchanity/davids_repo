# Interpreting Speech Emotion for the Hearing-Impaired

## Project 5 at Metis

**Objective**: Use a convoluted neural network (CNN) model to classify speech emotion and speaker gender. Create an app that processes input audio and notifies user of speech emotion, speaker gender, and speech transcription.

**Overview**:

- Acquire and process the speech-emotion audio dataset
- Create feature vectors for each gender-emotion label
- Train a CNN model on various hyperparameters to optimize accuracy
- Test the CNN model on new audio files
- Create a "Speech Emotion Interpreter" app using Streamlit that processes input audio and returns speech emotion and speaker gender.
  - _Speech transcription is in the app's code but could not be implemented due to Streamlit's limitations._

### Setup

#### 1) Access project5_speech_emotion.ipynb in the <a href="https://github.com/eunchanity/davids_repo/tree/master/projects/project5_speech_emotion/notebooks" target="_blank">notebooks folder</a> to follow data analysis and modeling

- Preparation and processing of audio files using librosa
- CNN model creation and hyperparameter tuning
- Model testing on new audio files
- Google Speech Recognition to transcribe audio to text

#### 2) Access the models in the <a href="https://github.com/eunchanity/davids_repo/tree/master/projects/project5_speech_emotion/src/models" target="_blank">src/models folder</a> to follow the modeling process and code

- CNN model in json format
- CNN model with weights
- Gender-emotion label predictions vs. actual values
- Gender-emotion labels

#### 3) Access the <a href="https://github.com/eunchanity/davids_repo/tree/master/projects/project5_speech_emotion/streamlit" target="_blank">streamlit folder</a> to test out a local Streamlit web app

- Import the model, model weights, and labels from notebook
- Deployment of the "Speech Emotion Interpreter" on Streamlit

#### 4) Access project5_speech_emotion.pdf in the <a href="https://github.com/eunchanity/davids_repo/tree/master/projects/project5_speech_emotion/reports" target="_blank">reports folder</a> to follow the presentation deck

- Presentation of model creation and model outputs
- Implications of the model's results
- Additional considerations

---
