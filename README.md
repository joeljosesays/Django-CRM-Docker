<html>
<h1> Django CRM Docker App Documentation </h1>
<div>
<p>In this project, I developed a CRM (Customer Relationship Management) application using Django as the web framework and MySQL as the database. To enhance scalability, portability, and ease of deployment, the application was dockerized. Docker containers encapsulate the entire application along with its dependencies, ensuring consistency and eliminating potential environment-related issues. This containerized CRM app can be efficiently deployed across various environments, providing a seamless and reliable solution for managing customer interactions and data. The use of Docker contributes to a streamlined development and deployment process, making it easier to maintain and scale the CRM application.</p>
</div>
<div>  
<h2>Table of Contents</h2>
<p>1) Introduction</br>
2) Prerequisites</br>
3) Getting Started</br>
4) Docker Configuration</br>
5) Run the Django App</br>
6) Additional Notes</p>
<div>
<h3>Introduction</h3>
Welcome to the documentation for the Django CRM Docker app! This document provides a quick guide to set up and run the app in a Docker environment.
</div>
<div>
<h3>Prerequisites</h3>
<p>Before you begin, ensure you have the following installed on your system:</p>
<p>1) Docker </br>
2) Docker Compose (if using Docker Compose)</p>
</div>
<div>
<h3>Getting Started</h3>
<p>1) Clone the repository </br>
2) Review the directory structure and files. </p>
</div>
<div>
<h3>Docker Configuration</h3>
<p>1) The Docker configuration is defined in the Dockerfile and docker-compose.yml. </br>
2) The django.sh file is mentioned as the entrypoint in the Dockerfile.</p>
</div>
<div>
<h3>Run the Django App</h3>
<p>1) Build the Docker image </br>
2) Run the Docker container </br>
3) Access the Django app in your web browser at http://localhost:8000. </p>
</div>
<div>
<h3>Additional Notes</h3>
1) Make sure to customize the django.sh file according to your Django project setup. </br>
2) Check the Django documentation for more details on <a href = https://django-configurations.readthedocs.io/en/stable/> Django configurations</a>.
</div>
</html>
