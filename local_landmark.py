import numpy as np

class LocalLandmark:

    def __init__(self, x, y, z, d=0, visibility=None):
        self.x = x
        self.y = y
        self.z = z
        self.d = d
        self.visibility = visibility

    @classmethod
    def from_mediapipe_pose_landmark(cls, mp_landmark):
        return cls(x=mp_landmark.x, y=mp_landmark.y, z=mp_landmark.z, visibility=mp_landmark.visibility)
    
    @classmethod
    def from_mediapipe_hand_landmark(cls, mp_landmark):
        return cls(mp_landmark.x, mp_landmark.y, mp_landmark.z)
    
    @classmethod
    def from_np_array(cls, np_array):
        visibility = np_array[4] if len(np_array) == 5 else None
        return cls(x=np_array[0], y=np_array[1], z=np_array[2], d=np_array[3], visibility=visibility)
    
    def get_np_array(self):
        landmark_array = [self.x, self.y, self.z, self.d] 
        if self.visibility is not None:
            landmark_array.append(self.visibility)
        return np.array(landmark_array)
    
    def is_empty(self):
        return self.x == 0 and self.y == 0 and self.z == 0 and self.d == 0
    
    def set_depth(self, d):
        self.d = d
