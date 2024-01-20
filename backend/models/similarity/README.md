# Theory here
- Loading the ViT (vision transformer) base model
- load the images with PIL
- use torchvision transforms to resize the images to 224, 224 (dimensions accepted by ViT)
- converting the images to tensors
- normalizing the tensors to improve performance
- using unsqueeze method to convert the images to the proper dimensions and making them computable on gpu
- getting embeddings of both images, while torch.no_grad() to prevent calculating gradients as we arent training
- reshaping the embeddings, and calculating cosine similarity

Google colab: https://colab.research.google.com/drive/1LijTUCRp4qGSOK-m5nHf_vGuHwGPiABl?usp=sharing