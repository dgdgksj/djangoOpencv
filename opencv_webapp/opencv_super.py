from django.conf import settings
import numpy as np
import cv2


def opencv_super(path):
    img = cv2.imread(path, 1)




    if (type(img) is np.ndarray):
        row,col,cha=img.shape
        converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        num_superpixels = 100  # desired number of superpixels
        print(row,col)
        print(row*col)
        #num_superpixels = row*col
        num_iterations = 4  # number of pixel level iterations. The higher, the better quality
        prior = 2  # for shape smoothing term. must be [0, 5]
        num_levels = 4
        num_histogram_bins = 5  # number of histogram bins
        height, width, channels = converted_img.shape
        seeds = cv2.ximgproc.createSuperpixelSEEDS(width, height, channels, num_superpixels, num_levels, prior,
                                                   num_histogram_bins)
        seeds.iterate(converted_img, num_iterations)
        num_of_superpixels_result = seeds.getNumberOfSuperpixels()
        #print('Final number of superpixels: %d' % num_of_superpixels_result)
        labels = seeds.getLabels()  # height x width matrix. Each component indicates the superpixel index of the corresponding pixel position
        mask = seeds.getLabelContourMask(False)
        #cv2.imshow('MaskWindow', mask)
        # cv2.waitKey(0)
        color_img = np.zeros((height, width, 3), np.uint8)
        color_img[:] = (0, 0, 255)
        mask_inv = cv2.bitwise_not(mask)
        result_bg = cv2.bitwise_and(img, img, mask=mask_inv)
        result_fg = cv2.bitwise_and(color_img, color_img, mask=mask)
        result = cv2.add(result_bg, result_fg)
        #cv2.imshow('ColorCodedWindow', mask)

        cv2.destroyAllWindows()
        result = cv2.resize(result, dsize=(800, 680), interpolation=cv2.INTER_AREA)
        cv2.imwrite(path, result)

    else:
        print('someting error')
        print(path)