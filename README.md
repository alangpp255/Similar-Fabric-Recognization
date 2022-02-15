# similar_fabric 研究說明

### 研究目標:  
訓練能用來辨識兩布料是否相似的特徵萃取模型

### 研究方法:  
利用simese network 的架構進行訓練，可以理解為將三個CNN model 串接在一起，最後再利用歐氏距離計算Triplet loss  
  
![image](https://user-images.githubusercontent.com/86472351/153794971-e409a701-dd05-4d8f-95f8-1b9e0c3a1a6a.png)
  
由上圖可看到imput 圖片分為anchor, positive 和negative，loss 計算原理如下:  
  
![image](https://user-images.githubusercontent.com/86472351/153796035-ed101d2c-4b3f-48af-b07a-59acd86e48bc.png)  
  
### 研究結果: 
85%-90%相似布料分類準確度，然而資料集量太小，目前仍有overfitting的問題，未來隨布料增加應當重新訓練
經測試後發現以keras ResNet50 的pre-trained model 作為特徵萃取基礎模型表現較AlexNet 和VGG16更好，因此未來修正若要想嘗試換model，可以避免用VGG16或AlexNet

  
    
# similar_fabric 程式說明

### 資料集連結 (包含fabric_data、說明PPT):  
https://drive.google.com/drive/folders/1TdWUdJYUOgRTYbXSxCeTnCEPWCn7JB0H?usp=sharing

### 主要程式:  
simese.ipynb: 訓練深度學習模型的主程式 (詳細操作在註解中)  
主要步驟: 讀入圖片檔並做預處理 -> 將圖片向量重新組合成triplet dataset -> 建構simese model using ResNest50 -> 訓練 -> 檢驗  

### 操作程式的必要資料夾:  
fabric_data: 立肯提供的相似布料資料，裡面的每個資料夾是按照相似布料歸類的  
model: 儲存simese 產生的特徵值萃取model，Res_model_emb_c_1.h5 為第一版上線於wevearbird的正式model  
fabric_array: 用來儲存simese.ipynb 初步處理圖檔的內容  
triplet: 用來儲存simese.ipynb 建構出的triplet dataset  
temp: 用來儲存simese.ipynb 進行data argumentation的暫存資料夾  

### 過去研究:  
old test: 儲存過去測試程式檔
  
  
# similar fabric 更新方法
1. 將新的布料類型加入fabric_data 資料集:  
資料夾按照相似布料類型歸檔(每個資料夾名稱為一類相似布料的代號) 
  
![image](https://user-images.githubusercontent.com/86472351/153983251-e412270a-1cb9-4275-bced-f755b3b5ca3c.png)  
  
![image](https://user-images.githubusercontent.com/86472351/153983698-5057908c-d1da-4690-b70e-55caa33c5f34.png)  

2. 修改 simese.ipynb 路徑:  
os_base = '存放上述所有資料夾的路徑'  
data_file = 'fabric_data'   

3. 順著跑後，會得到兩個模型結果siamese_triplet、embedding_model，並以.h5的副檔名儲存下來
上述兩模型 都用 model = load_model('xxxx.h5') 方式可重新讀入
siamese_triplet: 用來繼續之前的訓練 ， history = model.fit(x=train_x, shuffle=True, batch_size=batch,validation_split=.2, epochs=5)
embedding_model: 用來萃取特徵，以比較相似度的model (最終放在wevearbird 後端)    

4. embedding_model替換至 Weaverbird 主程式的方法


