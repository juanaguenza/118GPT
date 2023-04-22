# When deploy on your local machine, please use ‘pip install openai‘ to install OpenAI library
import openai
import getpass
import os
import json
import time
from glob import glob

# Insert your OPENAI API Key here
# Do not publish or reveal Your API KEY
# Find your API Key at: https://platform.openai.com/account/api-keys

# getting my api key
api_key_file = open("my_apikey.txt", "r")

openai.api_key = api_key_file.readline()

api_key_file.close()

chat_messages = [{
    "role": "system",
    "content": "You were a mathematics calculator. All you have now are a bunch of answers and some may contain explanations."
}, { 
    "role": "system", 
    "content": "You are going to get rid of the explanations from the text and only respond with the answer."
}, {
    "role": "system",
    "content": "If there is only an answer, repeat that answer in .tex format."
}, { 
    "role": "system", 
    "content": "If the input is only numbers in tex format, repeat the numbers in .tex format"
}, { 
    "role": "system", 
    "content": "You are going to output it in .tex format"
}, {
    "role": "system",
    "content": "If the content is a numerical value followed by words, the answer is the numerical value, get rid of the words."
}, {
    "role": "system",
    "content": "If the content are words followed by a numerical value, the answer is the numerical value, get rid of the words."
}, {
    "role": "system",
    "content": "For example, content of 36 words. results in you responding with \\boxed{36}. Apply this to all other variations."
}, {
    "role": "system",
    "content": "If it is a fraction keep it formatted as a latex fraction."
}, { 
    "role": "system", 
    "content": "Please ensure that your answer is in .tex format. it should be \\boxed{answer}"
}, { 
    "role": "system", 
    "content": "If no numerical value exists, respond with the text answer instead in the format of \\boxed{\text{answer}}"
},{
    "role": "system",
    "content": "If the content is no solution, respond with \\boxed{no solution}."
}, {
    "role": "system",
    "content": "When user is asking to exit/quit the chat, let them know they may enter 'exit' to exit the program"
}]

current_model = "gpt-3.5-turbo"

def create_result():
    try:
        print(chat_messages)
        response = openai.ChatCompletion.create(model=current_model,messages=chat_messages)

        # way of tracking total tokens used recently
        print("Total tokens used: ")
        print(response['usage']['total_tokens'])


        response_msg = response['choices'][0]['message']['content']
        # comment this to decide whether or not to track old messages
            # needs a bit more work with the api to track tokens
        # chat_messages.append(response_msg)
        # new_response_msg = response_msg['content'].strip("{\"solution\": ")
        # new_response_msg = new_response_msg.strip("\"}")
        return response_msg
    except openai.error.AuthenticationError:
        print(
        "system: Something went wrong when authenticating with server (AuthenticationError)"
        )
        print(
        "system: Your API key or token might be invalid, expired, or revoked")
        print(
        "system: Check or find your OpenAI API key at: https://platform.openai.com/account/api-keys"
        )
        return "error getting an answer"
    except openai.error.RateLimitError:
        print("system: You have hit your assigned rate limit. (RateLimitError)")
        print(
        "system: If your are not a pay as you go user, add your payment mehtods at: https://platform.openai.com/account/billing/overview"
        )
        print(
        "system: Or manage your usage rate at: https://platform.openai.com/account/billing/limits"
        )
        return "error getting an answer"
    except openai.error.Timeout:
        print("system: Your Request timed out. (Timeout)")
        print(
        "system: Please retry after a brief wait. Check OpenAI system status at: https://status.openai.com/?slack_message_token=default_success"
        )
        print("Enter \'exit\' to exit program.\n")
        return "error getting an answer"
    except openai.error.ServiceUnavailableError:
        print(
        "system: OpenAI service is currently unavaliable (ServiceUnavailableError)"
        )
        print(
        "system: Please retry after a brief wait. Check OpenAI system status at: https://status.openai.com/?slack_message_token=default_success"
        )
        print("Enter \'exit\' to exit program.\n")
        return "error getting an answer"
    except openai.error.InvalidRequestError:
        print(
        "system: Your request was malformed or missing some required parameters, such as a token or an input. (InvalidRequestError)"
        )
        print(
        "system: Chect OpenAi documentation at: https://platform.openai.com/docs/api-reference/"
        )
        print("Enter \'exit\' to exit program.\n")
        return "error getting an answer"
    except openai.error.APIConnectionError:
        print(
        "system: Something went wrong while connecting to OpenAI's API. (APIConnectionError)"
        )
        print(
        "system: If you are running on replit. Check replit's system status at: https://status.replit.com"
        )
        print(
        "system: On your own deployment, check your network settings, proxy configuration, SSL certificates, or firewall rules."
        )
        print("Enter \'exit\' to exit program.\n")
        return "error getting an answer"
    except Exception as e:
        print(
        "system: Something went wrong when parsing your message or communicating to server"
        )
        print("error_message: \n" + e.__str__())
        print("Enter \'exit\' to exit program.\n")
        return "error getting an answer"


path_to_folders = 'C:/Users/me/Desktop/All Code Resides Here/School/CMPM118/test/' # replace with your own filepath
# folder = input("What folder would you like to run? (algebra) (counting_and_probability) (intermediate_algebra) (number_theory) (prealgebra) or (precalculus)\n")

list_of_folders = ["algebra", "counting_and_probability", "geometry", "intermediate_algebra", "number_theory", "prealgebra", "precalculus"]

for folder in list_of_folders:
    counter = 0

    path_to_json = path_to_folders + folder + '/easy_answers/*.json'

    try:
        os.mkdir(path_to_json.replace("*.json", "") + "answers_formatted")
    except OSError as error:
        print(error)
        pass

    counter = 0
    for f_name in sorted(glob(path_to_json)):
        f = open(f_name)

        data = json.load(f)

        print("filepath we are working with is:")
        print(f_name)

        # get the name of the file here
        file_num = f_name[len(path_to_json) - 6:]
        file_num = file_num.strip(".json")

        # get the problem from each file
        message = {"role" : "system", "content" : data['solution']}
        chat_messages.append(message)

        res = create_result()

        # delete the problem (don't keep track of old answers)
        chat_messages.pop()

        # now make it into the answers folder
        answers_file = path_to_json.replace("*.json", "") + "answers_formatted/" + file_num + "_formatted.json"

        data_new = data
        data_new['solution'] = res

        with open(answers_file, "w") as outfile:
            outfile.write(json.dumps(data_new, indent = 4))

        print("Completed: " + data_new['solution'])
        counter += 1
        print(str(counter) + " iterations")

        # trying to prevent reaching a RPM or TPM limit (might need to be longer, or might even be redundant and slowing down for no reason)
        time.sleep(10)

print("We finished")