import cv2
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def loop_verification(img_fname_1, img_fname_2, new_size=None, is_vis=False):
    # 读取两幅图像
    img1 = cv2.imread(img_fname_1)
    if new_size is not None:
        img1 = cv2.resize(img1, new_size)
    img2 = cv2.imread(img_fname_2)
    if new_size is not None:
        img2 = cv2.resize(img2, new_size)

    # 提取关键点和描述符
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # 进行特征匹配并进行几何验证
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)
    good_matches = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good_matches.append([m])

    if not is_vis:
        return len(good_matches)  # return match nums

    # if len(good_matches) > 30: # 判断是否存在闭环
    #     if is_vis:
    #         print('Found loop closure!')
    #     else:
    #         return 1
    # else:
    #     if is_vis:
    #         print('No loop closure found.')
    #     else:
    #         return 0

    # 可视化匹配结果和验证结果
    if is_vis:
        img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good_matches,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        cv2.imshow('Matches', img3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def evaluate(gt_txt):
    match_points = []
    labels = []
    fp = open(gt_txt, "r")
    for line in tqdm(fp):
        line_str = line.split(", ")
        query, reference, gt = line_str[0], line_str[1], int(line_str[2])
        match_points.append(loop_verification(query, reference, new_size=None, is_vis=False))
        labels.append(gt)
    return np.array(match_points), np.array(labels)


if __name__ == '__main__':
    # visualization
    # loop_verification("Kudamm_mini_query/image0197.jpg", "Kudamm_mini_ref/image0174.jpg", new_size=None, is_vis=True)

    # evaluate
    datasets = ["Kudamm_easy_final.txt", "Kudamm_diff_final.txt", "robotcar_qAutumn_dbNight_easy_final.txt", "robotcar_qAutumn_dbNight_diff_final.txt", "robotcar_qAutumn_dbSunCloud_easy_final.txt", "robotcar_qAutumn_dbSunCloud_diff_final.txt"]

    for dataset in datasets:
        print("-------- Processing {} ----------".format(dataset.strip(".txt")))
        match_points, labels = evaluate(dataset)
        scaled_scores = match_points / max(match_points)
        precision, recall, _ = precision_recall_curve(labels, scaled_scores)
        average_precision = average_precision_score(labels, scaled_scores)
        plt.plot(recall, precision, label="{} (AP={:.3f})".format(dataset.strip(".txt"), average_precision))
        plt.xlabel("Recall")
        plt.ylabel("Precision")
        plt.legend()
        plt.title("Precision-Recall Curves for SIFT baseline")
        plt.savefig("pr_curve_{}.png".format(dataset.strip(".txt")))
        plt.close()
    
    # plt.xlabel("Recall")
    # plt.ylabel("Precision")
    # plt.legend()
    # plt.title("Precision-Recall Curves for SIFT baseline")
    # plt.savefig("pr_curve_SIFT.png")








    
