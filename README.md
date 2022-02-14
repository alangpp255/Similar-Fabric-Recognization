# similar_fabric

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
