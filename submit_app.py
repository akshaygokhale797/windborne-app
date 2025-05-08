import requests

url = "https://windbornesystems.com/career_applications.json"

data = {
    "career_application": {
        "name": "Akshay Gokhale",
        "email": "akshaygokhale2001@gmail.com",
        "role": "Atlas Software Intern",
        "notes": (
            "Linux & Python Infrastructure & Data Science and ML"
            "I feel like I bring an open-mindedness and willingness to change/grow my skills/habits, which makes me easy to work with!"
        ),
        "submission_url": "https://your-project-link.com",
        "portfolio_url": "https://github.com/akshaygokhale797",
        "resume_url": "https://docs.google.com/document/d/1jSW2D16-yg8CxLw4QKS9ezOcAYDPZlqqiqA60kV2cAY/edit?tab=t.0"
    }
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.text)
