from bs4 import BeautifulSoup
import requests

class RouteFinder:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://maps.googleapis.com/maps/api/directions/json"

    def get_route(self, origin, destination):
        """Fetch and print the route from origin to destination."""
        try:
            params = {
                'origin': origin,
                'destination': destination,
                'key': self.api_key,
                'traffic_model': 'best_guess',
                'departure_time': 'now'
            }

            response = requests.get(self.base_url, params=params)
            data = response.json()

            if data['status'] == 'OK':
                self.display_route(data, origin, destination)
            else:
                print(f"Error: {data['status']}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def display_route(self, data, origin, destination):
        """Display each step of the route with clean instructions."""
        steps = data['routes'][0]['legs'][0]['steps']
        print(f"Route from {origin} to {destination}:")

        for i, step in enumerate(steps):
            instruction = self.clean_instruction(step['html_instructions'])
            distance = step['distance']['text']
            duration = step['duration']['text']
            print(f"Step {i + 1}: {instruction} ({distance}, {duration})")

    @staticmethod
    def clean_instruction(html_instruction):
        """Clean HTML tags from instructions."""
        soup = BeautifulSoup(html_instruction, 'html.parser')
        return soup.get_text()

if __name__ == "__main__":
    api_key = "AIzaSyBEoBG9BD0qRT4PANx6z3aJ-GpnJTGaRto"
    origin = "Bus Stand, Sathyamangalam"
    destination = "Bannari Amman Institute of Technology"

    route_finder = RouteFinder(api_key)
    route_finder.get_route(origin, destination)
