# heatmap


`heatmap.py` calculates a histogram-like representation using circles with different radii and intensities. It iterates over each row in the DataFrame, creates a copy of the mask, and draws circles with varying radii and intensities at the specified ('x', 'y') coordinates. 

This approach creates a weighted accumulation of circular regions, allowing for intensity variations based on the radius. The resulting mask_total represents a distribution of points that have an impact on the histogram, with varying intensity levels.


`naive_heatmap.py` creates a binary mask where each point is represented as a filled circle of a fixed radius and intensity. The resulting mask represents the presence or absence of points at specific coordinates. Inspired by the Stack Overflow post titled "Superimpose heatmap on a base image - OpenCV Python." Available at: https://stackoverflow.com/questions/46020894/superimpose-heatmap-on-a-base-image-opencv-python.