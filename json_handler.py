
import json



class JsonDataBase:
    def __init__(self):
        pass

    
    def store_user_data(self, user_data):
        return self.write_data(user_data,"./tel_bot/data.json")



    def write_data(self, new_data, filename='./tel_bot/data.json'):
        with open(filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)

            user_id = new_data["uid"]
            # check if aleady exist
            if str(user_id) in file_data["user_data"].__str__():
                return 0
            # Join new_data with file_data inside emp_details
            file_data["user_data"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
            return 1

