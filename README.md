# Captcha-Breaker
![captcha](https://developers.google.com/recaptcha/images/newCaptchaAnchor.gif)

This project uses Deeplearning techiniques to break Google reCAPTCHA v2 by classifying the most popular image categories

## Demo
![demo](https://github.com/rishondz/Captcha-Breaker/blob/main/demo.gif)

## Description
We use a [Efficient Net B0](https://github.com/lukemelas/EfficientNet-PyTorch) model architecture to classify 11 categories of Google reCAPTCHA v2-  
**`'Bicycle', 'Bridge', 'Bus', 'Car', 'Chimney', 'Crosswalk', 'Hydrant', 'Motorcycle', 'Mountain', 'Palm', 'Traffic Light'`**


## Usage
1. Create a Virtual Environment
```bash
conda create -n captcha
```

2. Activate the virtual environment
```bash
conda activate captcha
```

2. Install the required packages
```bash
pip install -r requirements.txt
```

3. Using command line navigate to the project directory

4. Run the following command
```bash
streamlit run ImageCaptcha.py
```
5. Program will run in your local browser

## Team
* [Amey Rambatla](https://github.com/Ameybot)
* [Aayush Sharma](https://github.com/aayush9753)
* [Rishon Dsouza](https://github.com/rishondz)
