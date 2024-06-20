# 3D Canny Edge Detection with Gaussian Smoothing and Thresholding

This Python script applies 3D Canny edge detection to a NIfTI image with optional Gaussian smoothing, thresholding, and the ability to combine edges from all axes. It also supports auto-completion for command-line arguments.

## Requirements

- Python 3
- `nibabel`
- `scikit-image`
- `argparse`
- `argcomplete`

You can install the required packages using pip:

```sh
pip install nibabel scikit-image argparse argcomplete
```

## Usage

### Command-Line Arguments

- `input_filepath`: Path to the input NIfTI file.
- `output_filepath`: Path to save the output NIfTI file.
- `--sigma`: Sigma value for Canny edge detection (default: 1.0).
- `--gaussian_sigma`: Sigma value for Gaussian filter (default: 1.0).
- `--threshold`: Threshold value to remove data below this value (default: 0.0).
- `--view`: Open the OrthoSlicer3D viewer to visualize the result.

### Example Command

```sh
python mri_canny_filter.py path/to/your/input_image.nii.gz path/to/your/output_image.nii.gz --sigma 2.0 --gaussian_sigma 1.5 --threshold 0.1 --view
```

### Enabling Auto-Completion

To enable tab completion for the script's arguments, follow these steps:

1. Install `argcomplete` if you haven't already:

    ```sh
    pip install argcomplete
    ```

2. Add the following line to your `.bashrc` or `.bash_profile`:

    ```sh
    eval "$(register-python-argcomplete mri_canny_filter.py)"
    ```

    Replace `script_name.py` with the actual name of your script.

3. Source your shell configuration file to apply the changes:

    ```sh
    source ~/.bashrc
    # or
    source ~/.bash_profile
    ```

Alternatively, you can enable `argcomplete` for the current shell session with:

```sh
activate-global-python-argcomplete --dest=- | source /dev/stdin
```

### Script Explanation

1. **Thresholding:** The script applies a threshold to the input data, setting all values below the threshold to zero.
2. **Gaussian Smoothing:** A Gaussian filter is applied to smooth the data and reduce noise.
3. **Canny Edge Detection:** Canny edge detection is performed along each axis (sagittal, coronal, axial) of the 3D image.
4. **Combining Edges:** The edges detected along each axis are combined using `np.maximum` to form a single edge-detected volume.
5. **Saving the Result:** The combined edges are saved as a new NIfTI image.
6. **OrthoSlicer3D Viewer:** If the `--view` flag is set, the OrthoSlicer3D viewer is opened to visualize the result.
