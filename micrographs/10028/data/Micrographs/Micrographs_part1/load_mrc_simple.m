function vol = load_mrc_simple(filename)
    % Open MRC file
    fid = fopen(filename, 'r');
    if fid == -1
        error('Cannot open file: %s', filename);
    end

    % Read header values (assumes little-endian, 4-byte int32s)
    nx = fread(fid, 1, 'int32');
    ny = fread(fid, 1, 'int32');
    nz = fread(fid, 1, 'int32');

    % Skip the rest of the 1024-byte header
    fseek(fid, 1024, 'bof');

    % Read volume data
    vol = fread(fid, nx * ny * nz, 'float32');

    % Close the file
    fclose(fid);

    % Reshape and permute volume
    vol = reshape(vol, [nx, ny, nz]);
    vol = permute(vol, [2, 1, 3]);
end
left = uint8(tomogram(:,:,44));
right = uint8(tomogram(:,:,46));
imwrite(left, 'left.png');
imwrite(right, 'right.png');
