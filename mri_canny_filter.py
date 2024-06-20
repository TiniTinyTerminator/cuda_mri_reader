import nibabel as nib
import numpy as np
from skimage import feature, filters
import argparse

def apply_3d_canny(input_filepath, output_filepath, sigma=1.0, gaussian_sigma=1.0, threshold=0.0):
    # Load the NIfTI image
    img = nib.load(input_filepath)
    data = img.get_fdata()
    
    # Apply threshold to remove data below the threshold
    data[data < threshold] = 0
    
    # Apply Gaussian filter to remove noise
    data_smoothed = filters.gaussian(data, sigma=gaussian_sigma)
    
    # Initialize an empty array to store the combined edges
    combined_edges = np.zeros_like(data_smoothed)
    
    # Apply Canny edge detection for each axis
    # Axis 0 (Sagittal)
    for i in range(data_smoothed.shape[0]):
        combined_edges[i, :, :] = np.maximum(combined_edges[i, :, :], feature.canny(data_smoothed[i, :, :], sigma=sigma))
    
    # Axis 1 (Coronal)
    for i in range(data_smoothed.shape[1]):
        combined_edges[:, i, :] = np.maximum(combined_edges[:, i, :], feature.canny(data_smoothed[:, i, :], sigma=sigma))
    
    # Axis 2 (Axial)
    for i in range(data_smoothed.shape[2]):
        combined_edges[:, :, i] = np.maximum(combined_edges[:, :, i], feature.canny(data_smoothed[:, :, i], sigma=sigma))
    
    # Save the result as a new NIfTI image
    edge_img = nib.Nifti1Image(combined_edges.astype(np.float32), img.affine)
    nib.save(edge_img, output_filepath)
    print(f"3D Canny edge detection applied and saved to {output_filepath}")
    
    return edge_img

def main():
    parser = argparse.ArgumentParser(description="Apply 3D Canny edge detection to a NIfTI image with Gaussian smoothing, thresholding, and combining edges from all axes.")
    parser.add_argument('input_filepath', type=str, help="Path to the input NIfTI file.")
    parser.add_argument('output_filepath', type=str, help="Path to save the output NIfTI file.")
    parser.add_argument('--sigma', type=float, default=1.0, help="Sigma value for Canny edge detection (default: 1.0).")
    parser.add_argument('--gaussian_sigma', type=float, default=1.0, help="Sigma value for Gaussian filter (default: 1.0).")
    parser.add_argument('--threshold', type=float, default=0.0, help="Threshold value to remove data below this value (default: 0.0).")
    parser.add_argument('--view', action='store_true', help="Open the OrthoSlicer3D viewer to visualize the result.")

    args = parser.parse_args()
    edge_img = apply_3d_canny(args.input_filepath, args.output_filepath, args.sigma, args.gaussian_sigma, args.threshold)
    
    if args.view:
        nib.viewers.OrthoSlicer3D(edge_img.get_fdata()).show()

if __name__ == "__main__":
    main()
