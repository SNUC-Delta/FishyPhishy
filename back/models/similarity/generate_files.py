import pickle

from transformers import AutoFeatureExtractor, AutoModel, ViTForImageClassification, ViTImageProcessor


def generate_pickles():
    model_id = 'google/vit-base-patch16-224-in21k'
    extractor = ViTImageProcessor.from_pretrained(model_id)
    print(extractor)
    model = AutoModel.from_pretrained(model_id)
    print(model)
    print("model loaded")
    hidden_dim = model.config.hidden_size

    with open('extractor.pkl', 'wb') as f:
        pickle.dump(extractor, f)

    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

    with open('hidden_dim.pkl', 'wb') as f:
        pickle.dump(hidden_dim, f)
    print("Done!")

generate_pickles()