import pickle

from transformers import AutoFeatureExtractor, AutoModel

def generate_pickles():
    model_id = 'google/vit-base-patch16-224-in21k'
    extractor = AutoFeatureExtractor.from_pretrained(model_id)
    model = AutoModel.from_pretrained(model_id)
    hidden_dim = model.config.hidden_size

    with open('extractor.pkl', 'wb') as f:
        pickle.dump(extractor, f)

    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

    with open('hidden_dim.pkl', 'wb') as f:
        pickle.dump(hidden_dim, f)
    print("Done!")