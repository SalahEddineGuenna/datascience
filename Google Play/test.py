

class CustomETL:
    
    def __init__(self, filepath):
        self.filepath = filepath
        

example= CustomETL('test_data.csv')

print(example.filepath)