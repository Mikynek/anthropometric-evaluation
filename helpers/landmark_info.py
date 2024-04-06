from dataclasses import dataclass
from typing import List

# Medical anthropometric landmarks as MediaPipe landmarks indexes

G = 9
TR = 10
GN = 152

# Face oval
ZY_L = 127
ZY_R = 356
GO_L = 58
GO_R = 288

# Left eye
EX_L = 33
EN_L = 133

# Right eye
EX_R = 263
EN_R = 362

# Nose
SN = 2
N = 8
AL_L = 49
AL_R = 279

# Mouth
CH_L = 61
CH_R = 308
LS = 0
STO_LS = 13
LI = 17
STO_LI = 14

@dataclass
class LandmarkMeasurements:
    start: int
    end: int
    name: str

FACE_PROPORTIONS: List[LandmarkMeasurements] = [
    LandmarkMeasurements(ZY_L, ZY_R, "face_width"),
    LandmarkMeasurements(GO_L, GO_R, "jaw_width"),
    LandmarkMeasurements(SN, GN, "lower_face_height"),
    LandmarkMeasurements(TR, GN, "face_height"),
    LandmarkMeasurements(N, GN, "morph_face_height"),
    LandmarkMeasurements(N, STO_LS, "upper_face_height"),
    LandmarkMeasurements(STO_LI, GN, "lower_third_face_height"),
    LandmarkMeasurements(EN_L, GN, "special_face_height_left"),
    LandmarkMeasurements(EN_R, GN, "special_face_height_right"),
    LandmarkMeasurements(G, SN, "special_upper_face_height"),
    LandmarkMeasurements(EX_L, EX_R, "outer_eye_width"),
    LandmarkMeasurements(EN_L, EN_R, "inner_eye_width"),
    LandmarkMeasurements(EX_L, EN_L, "left_eye_width"),
    LandmarkMeasurements(EX_R, EN_R, "right_eye_width"),
    LandmarkMeasurements(AL_L, AL_R, "nose_width"),
    LandmarkMeasurements(N, SN, "nose_height"),
    LandmarkMeasurements(CH_L, CH_R, "mouth_width"),
    LandmarkMeasurements(LS, STO_LS, "upper_lip_height"),
    LandmarkMeasurements(STO_LI, LI,"lower_lip_height"),
]

@dataclass
class MaxDifference:
    value: float
    count: int
