<h1 align="center">A LiDAR Point Cloud Data Access and Visualization Package</h1>
<div align="center">
<a href="https://github.com/Hen0k/lidar_point_cloud"><img src="https://img.shields.io/github/forks/Hen0k/lidar_point_cloud" alt="Forks Badge"/></a>
<a "https://github.com/Hen0k/lidar_point_cloud/pulls"><img src="https://img.shields.io/github/issues-pr/Hen0k/lidar_point_cloud" alt="Pull Requests Badge"/></a>
<a href="https://github.com/Hen0k/lidar_point_cloud/issues"><img src="https://img.shields.io/github/issues/Hen0k/lidar_point_cloud" alt="Issues Badge"/></a>
<a href="https://github.com/Hen0k/lidar_point_cloud/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Hen0k/lidar_point_cloud?color=2b9348"></a>
<a href="https://github.com/Hen0k/lidar_point_cloud/blob/main/LICENCE"><img src="https://img.shields.io/github/license/Hen0k/lidar_point_cloud?color=2b9348" alt="License Badge"/></a>
</div>
</br>

## Problem Description

This is a tool that would allow AgriTech to easily and realiably fetch LiDAR point cloud data from a public AWS repository.

How much maize a field produces is very spatially variable. Even if the same farming practices, seeds and fertilizer are applied exactly the same by machinery over a field, there can be a very large harvest at one corner and a low harvest at another corner.  We would like to be able to better understand which parts of the farm are likely to produce more or less maize, so that if we try a new fertilizer on part of this farm, we have more confidence that any differences in the maize harvest 9are due mostly to the new fertilizer changes, and not just random effects due to other environmental factors.  

Water is very important for crop growth and health.  We can better predict maize harvest if we better understand how water flows through a field, and which parts are likely to be flooded or too dry. One important ingredient to understanding water flow in a field is by measuring the elevation of the field at many points. The USGS recently released high resolution elevation data as a lidar point cloud called USGS 3DEP in a public dataset on Amazon. This dataset is essential to build models of water flow and predict plant health and maize harvest.

## Installation Instructions
1. Clone the repo
   ```bash
   git clone https://github.com/Hen0k/lidar_point_cloud.git
   or
   git clone git@github.com:Hen0k/lidar_point_cloud.git
   ```
2. run the following
   ```bash
   cd lidar_point_cloud
   pip install .
   ```
