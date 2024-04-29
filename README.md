# Anthropometric Evaluation of Generated Face Images
This project is practical part of Jakub Mikyšek's Bachelor's Thesis at BUT FIT.

The main goal of this application is to provide an __anthropometric analysis__ between real and generated images of the human face.

[Deepface](https://github.com/serengil/deepface) and [MediaPipe](https://github.com/google/mediapipe) libraries are used for face recognition.

## How to Run the Program

To execute the program, enter the following command in your terminal:

```
python3 analyze_face_landmarks.py -r REAL-DATA -g GENERATED-DATA [-p] [-l]
```

For more information about program options run:

```
python3 analyze_face_landmarks.py -h
```

### Helpers

Some script are used to give support for text part of the thesis or for the program as well. There are located in directory `src/helpers`.