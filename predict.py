import tensorflow as tf

class Predict(object):
    def __init__(self):
        self.model = tf.keras.models.load_model('model')
    
    def predict(self, input):
        return self.model.predict_classes(input)



if __name__ == "__main__":
    classifier = Predict()

    import base64_image
    image = base64_image.eight

    from helper import Helper
    result = classifier.predict(Helper.read_img(image))

    print(result)
