from flask import Flask
import yaml


# Load answers.json into memory
with open('answers.yml', 'r') as file:
    print(yaml.safe_load(file))



# if __name__ == '__main__':
#     app.run(port=4000)