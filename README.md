# Captcha-Breaker
<img src="https://developers.google.com/recaptcha/images/newCaptchaAnchor.gif" width="500" height="110" />

This project uses Deeplearning techiniques to break Google reCAPTCHA v2 by classifying the most popular image categories

## Description
We use a pretrained [Efficient Net B0](https://github.com/lukemelas/EfficientNet-PyTorch) model to classify 11 categories of Google reCAPTCHA v2-  
**`'Bicycle', 'Bridge', 'Bus', 'Car', 'Chimney', 'Crosswalk', 'Hydrant', 'Motorcycle', 'Mountain', 'Palm', 'Traffic Light'`**  
We finetune the pretrained model using manually scrapped images (about 1000 per class) using transfer learning

<img src = "https://www.researchgate.net/publication/339462624/figure/fig1/AS:862263699316737@1582591094412/The-architecture-of-EfficientNet-b0.ppm" />

## Usage
1. Create a Virtual Environment
```bash
conda create -n captcha
```
2. Activate the virtual environment
```bash
conda activate captcha
```
3. Using command line navigate to the project directory
4. Install the required packages
```bash
pip install -r requirements.txt
```
5. Add your custom image to [Images](https://github.com/caciitg/Captcha-Breaker/tree/main/Images) folder
6. Run the following command
```bash
streamlit run ImageCaptcha.py
```
7. Program will run in your local browser

## Demo
![demo](https://github.com/rishondz/Captcha-Breaker/blob/main/demo.gif)

## Team
* [Amey Rambatla](https://github.com/Ameybot)
* [Aayush Sharma](https://github.com/aayush9753)
* [Rishon Dsouza](https://github.com/rishondz)
