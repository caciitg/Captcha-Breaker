exec(open("imp_statements.py").read())
exec(open("img_class.py").read())

import timm

st.title('Image Captcha Breaker')
st.header("Employing Computer Vision & Transfer Learning to identify images")

def get_list_of_images():
    file_list = os.listdir('Images')
    return [str(filename) for filename in file_list]

image_file_chosen = st.selectbox('Select an existing image:', get_list_of_images())

path = os.path.join('Images',image_file_chosen)

st.image(path,width=100)

classes =['Bicycle', 'Bridge', 'Bus', 'Car', 'Chimney', 'Crosswalk', 'Hydrant', 'Motorcycle', 'Mountain', 'Palm', 'Traffic Light']

trans = transforms.Compose([transforms.Resize((64,64)),transforms.ToTensor(),transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
test_generator = DataLoader(ImageData(path,transform=trans),batch_size = 1,shuffle = True)

m = timm.create_model('efficientnet_b0', pretrained=True)
m.classifier = nn.Linear(in_features=1280, out_features=11, bias=True)
m.load_state_dict(torch.load('Weights/TIMM Model 4.11'))

'Classifying Image...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  bar.progress(i + 1)
  time.sleep(0.1)

for X in test_generator:
    m.eval()
    pred1 = F.softmax(m(X),dim=1)
    pred2 = (pred1.argmax(axis=1))
    st.success(classes[pred2])

time.sleep(0.5)
st.balloons()


