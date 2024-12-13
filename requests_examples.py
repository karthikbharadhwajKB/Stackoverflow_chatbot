import requests
import json 

api_url = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"


def get_all_questions():
    response = requests.get(api_url)
    for i, item in enumerate(response.json()["items"]):
        print(f"Question-{i+1}: ")
        print(item["title"])
        print(item["link"])
        print("\n")

def get_questions_with_no_answers():
    response = requests.get(api_url)
    for i, item in enumerate(response.json()["items"]):
        if item["is_answered"] == False:
            print(f"Question-{i+1}: ")
            print(item["title"])
            print(item["link"])
        else:
            print("Question skipped...!")
        print("\n")


if __name__ == "__main__":
    # get_all_questions()
    get_questions_with_no_answers()
    