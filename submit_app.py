import requests

url = "https://windbornesystems.com/career_applications.json"

data = {
    "career_application": {
        "name": "Akshay Gokhale",
        "email": "youremail@example.com",
        "role": "Atlas Software Intern",
        "notes": (
            "Most skilled in full-stack development and data wrangling. "
            "I'm a collaborative builder who enjoys debugging messy systems and refining them into simple interfaces. "
            "I chose OpenWeather's API because it's live and dynamic, just like Windborne’s — combining the two felt like a natural fit for real-time exploration."
        ),
        "submission_url": "https://your-project-link.com",
        "portfolio_url": "https://github.com/akshaygokhale797",
        "resume_url": "https://docs.google.com/document/d/1jSW2D16-yg8CxLw4QKS9ezOcAYDPZlqqiqA60kV2cAY/edit?tab=t.0"
    }
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.text)
