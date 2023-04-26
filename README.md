# EE5346 Project
- Loop verification dataset for EE5346 project
- Three datasets
    - **qAutumn_dbSuncloud** (selected from the Oxford RobotCar): Dynamic objects, seasonal change, small viewpoint change
    - **qAutumn_dbNight** (selected from the Oxford RobotCar): Dynamic objects, Large light change, small viewpoint change
    - **Kudamm** (selected from the Kudamm dataset): Dynamic objects, Large viewpoint change

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

## Acknowledgements
- [Oxford RobotCar Dataset](https://robotcar-dataset.robots.ox.ac.uk/)
- [Kudamm Dataset from Mapillary](http://www.mapillary.com)