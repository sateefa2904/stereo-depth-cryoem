% make_synthetic_volume.m
% Generates a synthetic 3D volume and saves stereo slices

% Create a 3D synthetic volume
[x, y, z] = meshgrid(1:256, 1:256, 1:60);
volume = sin(0.1*x + 0.1*y + 0.3*z);

% Normalize volume manually to [0, 1]
min_val = min(volume(:));
max_val = max(volume(:));
volume_norm = (volume - min_val) / (max_val - min_val);

% Extract two slices to mimic stereo view
left_slice = uint8(255 * volume_norm(:,:,30));  % Left eye
right_slice = uint8(255 * volume_norm(:,:,32)); % Right eye

% Save slices as images
imwrite(left_slice, 'left.png');
imwrite(right_slice, 'right.png');

disp('Stereo images saved as left.png and right.png');
