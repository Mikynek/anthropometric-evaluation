# Anthropometric Evaluation of Generated Face Images
This project is practical part of Jakub Mikyšek's Bachelor's Thesis at BUT FIT.

The main goal of this application is to provide an __anthropometric analysis__ between real and generated images of the human face.

[Deepface](https://github.com/serengil/deepface) and [MediaPipe](https://github.com/google/mediapipe) libraries are used for face recognition.

## How to Run the Program

To execute the program, enter the following command in your terminal:

```
python3 src/analyze_face_landmarks.py -r REAL-DATA -g GENERATED-DATA [-p] [-l]
```

For more information about program options run:

```
python3 src/analyze_face_landmarks.py -h
```

To run program properly install needed dependencies from requirements.txt using:

```
cd src
pip install -r requirements.txt
```

StyleGAN3 notebook for generating images has own pip install already in first code block. It is primarily optimized for use with [Google Colab](https://colab.research.google.com/drive/1wdxcXZlfuppqG6gbN94YjNPHmGbDGHQ0?usp=sharing) for seamless execution.

## Dataset

The dataset used in this thesis includes real and generated images. The real images are a subset of the [CelebAMask-HQ Dataset](https://mmlab.ie.cuhk.edu.hk/projects/CelebA/CelebAMask_HQ.html) and are located in the `real-data` folder. The generated images were created by GAN model [StyleGAN3](https://github.com/NVlabs/stylegan3) and are located in the `gen-data` folder. Each folder contains 250 images, forming 250 pairs in total.


### Helpers

Various scripts are used to support the thesis and the program. They are located in the `src/helpers` directory.