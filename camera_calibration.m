clear;
close all;
clc;

load("cameraParams.mat");

R_gri_cam = cameraParams.RotationMatrices(:, :, 1);
p_cam_gri = cameraParams.TranslationVectors(1, :)';

p_gri_cam = -R_gri_cam*p_cam_gri;
T_gri_cam = [R_gri_cam p_gri_cam; 0 0 0 1];

R_rob_gri = [0 -1 0; -1 0 0; 0 0 -1];
p_rob_gri = [755.175; -27.961; 22.778];
T_rob_gri = [R_rob_gri p_rob_gri; 0 0 0 1];

T_rob_cam = T_rob_gri*T_gri_cam