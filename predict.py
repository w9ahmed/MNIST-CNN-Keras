import tensorflow as tf

class Predict(object):
    def __init__(self):
        self.model = tf.keras.models.load_model('model')
    
    def predict(self, input):
        return self.model.predict_classes(input)
