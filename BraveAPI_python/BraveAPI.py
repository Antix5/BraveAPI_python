import requests

class BraveAPI:

    def __init__(self, key, country="FR"):
        self.key = key
        self.country = country

    def web_search(self, word_to_search):
        # Endpoint for web search
        endpoint = "https://api.search.brave.com/res/v1/web/search"

        # Prepare headers with API key
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "X-Subscription-Token": self.key,
            "country": self.country
        }

        # Prepare query parameters
        params = {
            "q": word_to_search
        }

        # Make the API request
        response = requests.get(endpoint, headers=headers, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and return the JSON response
            return response.json()
        else:
            # If the request was not successful, print the error message
            print(f"Error: {response.status_code} - {response.text}")


    def get_titles(self, nb_best_results=None):
        titles = [result["title"] for result in self.last_result["web"]["results"]]
        if nb_best_results is not None:
            titles = titles[0:nb_best_results]
        return titles
