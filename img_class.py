exec(open("imp_statements.py").read())

class ImageData(Dataset):
    def __init__(self,path,transform=None):
        self.path = path
        self.transform = transform
        
    def __len__(self):
        return 1
    
    def __getitem__(self,index):
        img_path = self.path
        image = (Image.open(img_path)).convert('RGB')
        if self.transform is not None:
            image = self.transform(image)
        return image

