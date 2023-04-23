import cv2

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

    if len(good_matches) > 30: # 判断是否存在闭环
        if is_vis:
            print('Found loop closure!')
        else:
            return 1
    else:
        if is_vis:
            print('No loop closure found.')
        else:
            return 0

    # 可视化匹配结果和验证结果
    if is_vis:
        img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good_matches,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        cv2.imshow('Matches', img3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    loop_verification("Kudamm_mini_query/image0197.jpg", "Kudamm_mini_ref/image0174.jpg", new_size=None, is_vis=True)




    
