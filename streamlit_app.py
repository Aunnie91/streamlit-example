import streamlit as st 
import os
import sys


from helper_inference_intruder_temp import Intruder_Temp_Inference



def load_image():
 
    image_data = st.file_uploader("Upload An Image",type=['png','jpeg','jpg','webp','tif'])
    if image_data is not None:
      file_details = {"FileName":image_data.name,"FileType":image_data.type}
      st.write(file_details)
      st.image(image_data)
      with open('/content/drive/MyDrive/Intruder_Detection/Streamlit_App/Input/'+ file_details['FileName'] ,"wb") as f: 
        f.write(image_data.getbuffer())         
      st.success("Saved File")
      if st.button('Run Prediction'):
        objhelper=Intruder_Temp_Inference()
        opFilePath=objhelper.run_Inference('/content/drive/MyDrive/Intruder_Detection/Streamlit_App/Input/'+ file_details['FileName'])
        if(opFilePath=='No Inference'):
          st.write('Error Something wet wrong')
        else:
          st.image(opFilePath)
        




def main():
    st.title('Intruder Detection Proof  Of Code')
    load_image() 



if __name__ == '__main__':
    main()
