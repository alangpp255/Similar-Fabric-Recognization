# similar_fabric

研究目標:
訓練能用來辨識兩布料是否相似的特徵萃取模型

研究方法:  
利用simese network 的架構進行訓練，可以理解為將三個CNN model 串接在一起，最後再利用歐氏距離計算Triplet loss  
![image](https://user-images.githubusercontent.com/86472351/153794682-a09ef3c7-ccac-4fa0-9666-1ba2a2390843.png)  

由上圖可看到imput 圖片分為anchor, positive 和negative




研究結果:  
經測試後發現以keras ResNet50 的pre-trained model 作為特徵萃取基礎模型表現較AlexNet 和VGG16更好，因此未來修正若要想嘗試換model，可以避免用VGG16或AlexNet


主要程式:  
simese.ipynb: 訓練深度學習模型的主程式 (詳細操作在註解中)  

操作程式的必要資料夾:  
fabric_data: 立肯提供的相似布料資料，裡面的每個資料夾是按照相似布料歸類的  
model: 儲存simese 產生的特徵值萃取model，Res_model_emb_c_1.h5 為第一版上線於wevearbird的正式model  
fabric_array: 用來儲存simese.ipynb 初步處理圖檔的內容  
triplet: 用來儲存simese.ipynb 建構出的triplet dataset  
temp: 用來儲存simese.ipynb 進行data argumentation的暫存資料夾  

過去研究:  
old test: 儲存過去測試程式檔

資料連結 (包含fabric_data、說明PPT):  
https://drive.google.com/drive/folders/1TdWUdJYUOgRTYbXSxCeTnCEPWCn7JB0H?usp=sharing
