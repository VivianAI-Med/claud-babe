import pickle

# After training your model
pickle.dump(model, open('appendicitis_model.pkl', 'wb'))

# If you have a label encoder for categorical variables
pickle.dump(label_encoder, open('label_encoder.pkl', 'wb'))
