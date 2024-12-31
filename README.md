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

"point set B" was created in a similar way, but with random positioning errors added in the x, y, and z directions, ranging from ±0.1 to ±0.3.

This is the original surface:

<p align="center">
<img src=https://github.com/Plus-1000/Reconstruct-missing-areas-in-a-point-cloud-face/blob/main/pic/ori_face_0.jpg width="600" >
<b>
&nbsp;<br>
<p align="center">
<img src=https://github.com/Plus-1000/Reconstruct-missing-areas-in-a-point-cloud-face/blob/main/pic/fine_error.jpg width="600" >
<b>
&nbsp;<br>




 
## Point interpolation along pt_cloud face normal
Suppose we have a point near pt_cloud, this method tries to project the point on the "face" of the point cloud along the face normal

## 1, How the point cloud looks like
The pt_cloud consists of points with coordinates in CSV format.
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-interpolation/blob/main/pic/p1.jpg width="600" >
<b>
&nbsp;<br>
&nbsp;<br>
 
## 2, About the points which will be projected onto pt_cloud "face"
Red color points are on the convex side, yellow points are on the concave side. 

<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-interpolation/blob/main/pic/p2.jpg width="600" >
<b>
&nbsp;<br>
&nbsp;<br>
 
## 3, About the calculation: 
* Nearest points and face normal
* Rotate the datum and the involved points, ensuring the Z+ direction remains straight and upward
* Interpolation calculation, get the distance from pt to grid
* Back to original 
&nbsp;<br>

 1), Find nearest points on pt_cloud and the point vector.
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-interpolation/blob/main/pic/p3_1.jpg width="600" >
<b>
&nbsp;<br>
&nbsp;<br>

 
 2), Transfer point and it's nearest neighbors to new datum, which's Z+ direction is straight upwards.
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-interpolation/blob/main/pic/p3_2.jpg width="600" >
<b>
&nbsp;<br>
&nbsp;<br>
 
 3), Use scipy.interpolation.griddata, to get the distance from the point to face 
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-interpolation/blob/main/pic/p3_3.jpg width="600" >
<b>
&nbsp;<br>
&nbsp;<br>
 
 4), Return to the original datum, we move the point in the opposite direction of its vector by the previously calculated distance, resulting in the interpolated point.
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-interpolation/blob/main/pic/p3_4.jpg width="600" >
<b>
&nbsp;<br>
&nbsp;<br>
 
## 4, Check the result
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-interpolation/blob/main/pic/p4.jpg width="600" >
<b>
&nbsp;<br>
&nbsp;<br>
 
## 5, Factors affecting interpolation accuracy:
* The number of points (selected to proceed with interpolation)
* The griddata parameter (‘linear’, ‘nearest’, ‘cubic’)
* Other factors (e.g., point cloud quality)
&nbsp;<br>
&nbsp;<br>

## 6, Point interpolation along fixed vector
Please check: Interp_3D_along_fix_vector.py
&nbsp;<br>
&nbsp;<br>

## 7, Find the closest point from pt_cloud
Please check: Interp_3D_closest.py
&nbsp;<br>
&nbsp;<br>



*Wang Jian, 2024 Jun 12, wjian88@gmail.com*
