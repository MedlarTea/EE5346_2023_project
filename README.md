# EE5346 Project
- Loop verification dataset for EE5346 project
- Three datasets
    - **qAutumn_dbSuncloud** (selected from the Oxford RobotCar): Dynamic objects, seasonal change, small viewpoint change
    - **qAutumn_dbNight** (selected from the Oxford RobotCar): Dynamic objects, large light change, small viewpoint change
    - **Kudamm** (selected from the Kudamm dataset): Dynamic objects, large viewpoint change

## Get and know the dataset
- `unzip` all datasets to the current repository
- `.txt` file stores the ground truth information where
```bash
# For example, in the first line of "robotcar_qAutumn_dbNight_diff_final.txt"
Autumn_mini_query/1418133788799845.jpg, Night_mini_ref/1418756794975225.jpg, 1
# "query image file name", "reference image file name", "label" (1 for true loop verification, 0 for false one)
```

- Every dataset contains an `easy` part and a `difficult` part, which is judged by the simple verification baseline in the `verification_test.py`.

## Simple running
```bash
python verification_test.py
```

## Final testing
Our final testing datasets are selected from Oxford RobotCar, including two mini datasets:
- **qAutumn_dbSuncloud_val** (1600 pairs): Dynamic objects, seasonal change and large viewpoint change (distance of two places is larger than 15 meter)
- **qAutumn_dbNight_val** (1600 pairs): Dynamic objects, large seasonal change and small viewpoint change (distance of two places is smaller than 5 meter)

Dataset download (can only be downloaded via SUSTech network):
```bash
# original files including images, pointclouds, vo and gps
Autumn_val.zip
Night_val.zip
Suncloud_val.zip

# selected images
Autumn_mini_val_query.zip
Night_mini_val_ref.zip
Suncloud_mini_val_ref.zip

# toolkit for projecting the pointcloud to the image
robotcar-dataset-sdk-3.0 
```
If you prefer to utilize sequence or depth information, please download the original files to accomplish your ideas; Otherwise, you can download the selected images only. **Notice that, all images have been undistored.**

Selected image pairs are stored in `robotcar_qAutumn_dbNight_val_final.txt`, `robotcar_qAutumn_dbSunCloud_val_final.txt`. Please ensure your codes can read these two files and corresponding images, then infer the final results. The results should be named as `robotcar_qAutumn_dbNight_val_result.txt`, `robotcar_qAutumn_dbNight_val_result.txt` and look like (1 for true and 0 for false):
```
1
0
1
```
For students who utilize sequence or depth information, please write a `README.md` to explain how to run your codes. We hope you can make the best effort to ease TA's job :) that we can easily download your processed data and run your codes.


## Acknowledgements
- [Oxford RobotCar Dataset](https://robotcar-dataset.robots.ox.ac.uk/)
```
@article{RobotCarDatasetIJRR,
  Author = {Will Maddern and Geoff Pascoe and Chris Linegar and Paul Newman},
  Title = {{1 Year, 1000km: The Oxford RobotCar Dataset}},
  Journal = {The International Journal of Robotics Research (IJRR)},
  Volume = {36},
  Number = {1},
  Pages = {3-15},
  Year = {2017},
  doi = {10.1177/0278364916679498},
  URL = {http://dx.doi.org/10.1177/0278364916679498},
  eprint = {http://ijr.sagepub.com/content/early/2016/11/28/0278364916679498.full.pdf+html},
  Pdf = {http://robotcar-dataset.robots.ox.ac.uk/images/robotcar_ijrr.pdf}}
```
- [Kudamm Dataset from Mapillary](https://www.mapillary.com/dataset/places)
```
@article{sunderhauf2015place,
  title={Place recognition with convnet landmarks: Viewpoint-robust, condition-robust, training-free},
  author={S{\"u}nderhauf, Niko and Shirazi, Sareh and Jacobson, Adam and Dayoub, Feras and Pepperell, Edward and Upcroft, Ben and Milford, Michael},
  journal={Robotics: Science and Systems XI},
  pages={1--10},
  year={2015},
  publisher={Robotics: Science and Systems Conference}
}
```