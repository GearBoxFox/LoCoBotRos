import numpy as np
import math
from typing import List

class Kinematics:
    """
    Handles the calculation of kinematics for the 5-dof kinematic arm
    """

    def __init__(self, phi_resolution: float = 1.0):
        # Define Devanit-Hartenberg parameters for the locobot arm
        # arm length segments in centimeters
        self.a_1: float = 4.0
        self.a_2: float = 2.54
        self.a_3: float = 20.32
        self.a_4: float = 0#12.7
        self.a_5: float = 20.32
        self.a_6: float = 1.0
        self.a_7: float = 1.0

        self.dh_parameters = [
            {'alpha': 0, 'r': 0, 'd': 0}, # base frame 
            {'alpha': -math.pi / 2, 'r': 0, 'd': self.a_1 + self.a_2}, # shoulder joint
            {'alpha': 0, 'r': self.a_3, 'd': self.a_4}, # elbow joint
            {'alpha': 0, 'r': self.a_5, 'd': 0},
        ]

    def generate_transform_matrix(self, theta: float, joint_index: int) -> np.ndarray:
        """
        Generates a 4x4 transformation matrix from joint frame n-1 to n.
        """

        if joint_index >= len(self.dh_parameters):
            raise ValueError(f"Joint index {joint_index} out of range")
        
        dh = self.dh_parameters[joint_index]

        cos_theta = np.cos(theta)
        sin_theta = np.sin(theta)
        cos_alpha = np.cos(dh['alpha'])
        sin_alpha = np.sin(dh['alpha'])

        #print(f"CosTheta: {cos_theta}\nSinTheta: {sin_theta}\nCosAlpha: {cos_alpha}\nSinAlpha: {sin_alpha}")

        return np.array([
            [cos_theta, -sin_theta * cos_alpha, sin_theta * sin_alpha, dh['r'] * cos_theta],
            [sin_theta, cos_theta * cos_alpha, -cos_theta * sin_alpha, dh['r'] * sin_theta],
            [0, sin_alpha, cos_alpha, dh['d']],
            [0, 0, 0, 1]
        ])
    
    def forward_kinematics(self, joint_angles: List[float]) -> List[np.ndarray]:
        if len(joint_angles) != 5:
            raise ValueError(f"joint_angles must contain exactly 5 elements.\n join_angles is of size {len(joint_angles)}")
        
        # extract joint angles
        theta1, theta2, theta3, theta4, theta5 = joint_angles
        #print(f"Theta 1: {theta1}")

        t1_2 = self.generate_transform_matrix(theta1, 1)
        t2_3 = self.generate_transform_matrix(theta2 - (math.pi / 2), 2)
        t3_4 = self.generate_transform_matrix(theta3 + (math.pi / 2), 3)

        return [t1_2, t2_3, t3_4]
    
