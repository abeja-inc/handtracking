#!/usr/bin/env python
# coding: utf-8



from utils import detector_utils as detector_utils
import cv2
import tensorflow as tf
import datetime


detection_graph, sess = detector_utils.load_inference_graph()



import time
video = cv2.VideoCapture('shelf_ceil.MOV')

# 形式はMP4Vを指定/ out
fps    = video.get(cv2.CAP_PROP_FPS)
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
ts = int(time.time())
result = f"out2/test2_output_{ts}.m4v"
out = cv2.VideoWriter(result, int(fourcc), fps, (width, height))
totalFrames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))


# In[34]:


from tqdm import tqdm

num_hands_detect = 100
score_thresh = 0.3

for i in tqdm(range(totalFrames)):
    ret, image_np = video.read()
    if not ret:
        break
    image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
    boxes, scores = detector_utils.detect_objects(image_np,
                                                          detection_graph, sess)
    for box, score in zip(boxes, scores):
        if score > score_thresh:
            print(i, box, score)

    im_height, im_width, _ = image_np.shape
    detector_utils.draw_box_on_image(num_hands_detect, score_thresh,
                                             scores, boxes, im_width, im_height,
                                             image_np)
    out.write(image_np)
out.release()


# In[ ]:
