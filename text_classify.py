import numpy as np

code_to_category = {0: 'Travel',
                    1: 'Social Networking and Messaging',
                    2: 'News',
                    3: 'Streaming Services',
                    4: 'Sports',
                    5: 'Photography',
                    6: 'Law and Government',
                    7: 'Health and Fitness',
                    8: 'Games',
                    9: 'E-Commerce',
                    10: 'Food',
                    11: 'Education',
                    12: 'Computers and Technology',
                    13: 'Business/Corporate'}

class TextClassifier:
    
    def __init__(self, loaded_model):
        self.loaded_model = loaded_model
        
        
    def get_two_largest_indices(self, arr):
        sorted_indices = np.flip(arr.argsort())
        largest_index = sorted_indices[0]
        second_largest_index = sorted_indices[1]
        
        return largest_index, second_largest_index


    def assign_tag(self, text, loaded_model):
        category=[]
        probabilities = loaded_model.predict_proba(text)[0]
        largest_index_1,largest_index_2 = self.get_two_largest_indices(probabilities)
        
        category=[]
        if probabilities[largest_index_1]>=0.30:
            category.append(code_to_category[largest_index_1])
        else:
            return category
        
        if probabilities[largest_index_2]>= max(0.20, probabilities[largest_index_1]/2):
            category.append(code_to_category[largest_index_2])
            
        return category