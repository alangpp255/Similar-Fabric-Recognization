from feature_sim import get_feature_vector, calculate_similarity
from sklearn.metrics import confusion_matrix,precision_score,recall_score   #counting confusion matrix
import matplotlib.pyplot as plt
import os
import time
import cv2

#set main direction
os_base='C:/Users/Alan/Desktop/Bilab/Weaver/similarity_test/'

#cut down for similarity
cut = 0.8

top_true=[] #to counting confusion matrix
top_pred=[] #to counting confusion matrix

#store original image to visualize 
images =[]
#Store all features by file name or id
feature_dict={}



#read the all image and get feature by VGG16
#time_start = time.time()
for i in os.listdir(os_base+'test_image'):
    img_list = os.listdir(os_base+'test_image/'+i)
    for t in range(len(img_list)):
        img = cv2.imread(os_base+'test_image/'+i+'/'+img_list[t])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #images.append(img)
        feature_dict[img_list[t][:-4]]=get_feature_vector(img)
     
  
# time_end = time.time()
# time_c= time_end - time_start
# print('time cost', time_c, 's')
# print(len(feature_name))



#calcuate similarity
sim_dict = {}
for i in feature_dict.keys():
    #time_start = time.time()
    sim=[]
    for t in feature_dict.keys():
        if i != t:
            result = calculate_similarity(feature_dict[i],feature_dict[t])
            if result >= cut:
                sim.append((t,result))
    sim= sorted(sim, key = lambda s: s[1],reverse = True)
    sim_dict[i] = sim
print(sim_dict)
    
    
    
    # # time_end = time.time()
    # # time_c= time_end - time_start
    # # print('time cost', time_c, 's')
    
    # #排序
    # top = []
    # for t in range(len(sim)):
    #     if max(sim) >= cut:
    #         top_pred.append(1)
    #         if (feature_name[sim.index(max(sim))].split('_'))[0] == (t_feature_name[i].split('_'))[0]:
    #             top_true.append(1)
    #         else:
    #             top_true.append(0)
    #         top.append(sim.index(max(sim)))
    #         rating.append(max(sim))
    #     else:
    #         top_pred.append(0)
    #         if (feature_name[sim.index(max(sim))].split('_'))[0] == (t_feature_name[i].split('_'))[0]:
    #             top_true.append(1)
    #         else:
    #             top_true.append(0)
    #     sim[sim.index(max(sim))]=0

