# Use polynomial fitting to reconstruct missing areas in a point cloud face, with ChatGPT coding assistance.

## About "polynomial fitting"
Please refer to this link for how to build a formula from points:

<br>
https://www.scilab.org/surface-fitting


Or we can observe how the  surface fitting works with an app:
<br> 
https://www.originlab.com/fileExchange/details.aspx?fid=282

Any face can be described by the polynomial formula:

<p align="center">
<img src=https://github.com/Plus-1000/Reconstruct-missing-areas-in-a-point-cloud-face/blob/main/pic/formula.jpg width="600" >
<b>
&nbsp;<br>
&nbsp;<br>
The typical applications of polynomial techniques include: 
* Noise Reduction: Fit a polynomial to noisy data and use it as a smoothed representation.
  
* Interpolation: Estimate values at unknown points within the domain of the data.
  
* Surface Approximation: Model complex surfaces like terrain, curved structures, or fluid flow.

* Feature Extraction: Analyze curvature or other geometric properties of the surface.

In this test, we aim to retrieve the missing points from the point cloud face stored in a CSV file.

## 1) About the test: 
We designed a 3D face and generated a "point set A" from it, with some points in the central area intentionally missing.

"point set B" was created similarly, but with random positioning errors added in the x, y, and z directions, ranging from ±0.1 to ±0.3.

This is the original surface:

<p align="center">
<img src=https://github.com/Plus-1000/Reconstruct-missing-areas-in-a-point-cloud-face/blob/main/pic/ori_face_0.jpg width="600" >
<b>
&nbsp;<br>
  
Points set A, point set B (noise added), and target point set after fitting.
<p align="center">
<img src=https://github.com/Plus-1000/Reconstruct-missing-areas-in-a-point-cloud-face/blob/main/pic/fine_error.jpg width="600" >
<b>
&nbsp;<br>


## 2) How ChatGPT can help in coding: 
The advice from ZD.net for the advantages and disadvantages of coding with ChatGPT : 
<br>
https://www.zdnet.com/article/how-to-use-chatgpt-to-write-code-what-it-does-well-and-what-it-doesnt/

Now we try to ask ChatGPT: "*Apply a polynomial algorithm to generate a 3D face from the current pt_cloud which is provided in a CSV format.*"

Then we can receive the reply on the PC screen: 

<span style="color: grey;"> 
To apply a polynomial algorithm to generate a 3D face from a point cloud provided in a CSV format, we can follow these steps:


1. Load the Point Cloud: 
    * Read the CSV file containing the point cloud data. Ensure the file has x, y, and z coordinates for each point.
2. Fit a Polynomial Surface:

   *  Use polynomial fitting to approximate the surface. For 3D point clouds, we typically fit a 2D polynomial to model 
z=f(x,y).

   *  Choose the degree of the polynomial based on the complexity of the surface.

1. Generate the Surface:
   * Use the fitted polynomial coefficients to create a smooth surface grid over the range of the 
x and y coordinates.
1. Export the Result:

   * Save the generated 3D surface points (x, y, z) into a new CSV file.

<p align="center">
<img src=https://github.com/Plus-1000/Reconstruct-missing-areas-in-a-point-cloud-face/blob/main/pic/GPT%20codes%202.jpg width="600" >
<b>
&nbsp;<br>


You can test or modify the code as needed; the file Polynomial_fit.py contains the complete implementation.

## 3) Check result
3.1) Fitting original points cloud (point set A), 9-degree fitting takes 17 seconds. 

<p align="center">
<img src=https://github.com/Plus-1000/Reconstruct-missing-areas-in-a-point-cloud-face/blob/main/pic/ori_9%20degree%20fitting.JPG width="600" >
<b>
&nbsp;<br>


Export new pts to SIEMENS NX CADCAM interface, check the distance from missing pts to original face: 
<p align="center">
<img src=https://github.com/Plus-1000/Reconstruct-missing-areas-in-a-point-cloud-face/blob/main/pic/ori_dist.JPG width="600" >
<b>
&nbsp;<br>


3.2) Fitting points cloud with noisy (point set A), 9-degree fitting also. 
<p align="center">
<img src=https://github.com/Plus-1000/Reconstruct-missing-areas-in-a-point-cloud-face/blob/main/pic/noisy_9%20degree%20fitting.JPG width="600" >
<b>
&nbsp;<br>


The distance from the missing pt to the ori face is 0.122 mm.
<p align="center">
<img src=https://github.com/Plus-1000/Reconstruct-missing-areas-in-a-point-cloud-face/blob/main/pic/noisy_dist.jpg width="600" >
<b>
&nbsp;<br>

</span>

Polynomial fitting has its limitations; it is not practical for a normal PC to handling complex or non-continuous surfaces, and high-degree fitting calculations may take a long time.

*Wang Jian, 2024 Dec 27, wjian88@gmail.com*

</span>







