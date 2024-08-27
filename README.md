# Django Application with Docker

This is a Django application that has been containerized using Docker. The project includes a Dockerfile to build a Docker image and run the Django application in a container.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/) (if you plan to use Docker Compose)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Uzumaki1209/my-django-app
   cd your-repo-name

Build the Docker image:

Run the following command in the root directory of your project where the Dockerfile is located:

docker build -t django-app .

Running the Application

Run the Docker Container:

To start the Django application in a Docker container, run:

docker run -p 8000:8000 django-app

Access the Application:

Open your web browser and go to http://localhost:8000 to view the Django application.

Development

If you want to contribute to this project or run it locally without Docker, follow these steps:

Create a virtual environment:

python -m venv venv
Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS and Linux:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the Django development server:

python manage.py runserver

Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any changes you'd like to make.