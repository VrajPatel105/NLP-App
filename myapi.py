
import nlpcloud

class API:
    
    def __init__(self):
        # API key (replace with your actual API key)
        self.api_key = "Enter Your api" 

    def initialize_client(self, model_name, gpu=False):
        # Initialize the client dynamically based on the model name
        return nlpcloud.Client(model_name, self.api_key, gpu=gpu)
 
    def sentiment_analysis(self, text):
        # Use the specific model for sentiment analysis
        client = self.initialize_client("distilbert-base-uncased-emotion")
        response = client.sentiment(text)
        return response
    

 
    def image_analysis(self,text):

        client = self.initialize_client("stable-diffusion", gpu = True)
        response = client.image_generation(text)
        return response
    

    def headline_generator(self,text):

        client = self.initialize_client("t5-base-en-generate-headline")
        response = client.summarization(text)
        return response
