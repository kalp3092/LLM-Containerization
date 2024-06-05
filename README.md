# LLM Model Finetuning and Deployment

This project involves finetuning the LLAMA2 model using ollama interface, tweaking its parameters, and providing a GUI to interact with the model via a Streamlit web application. The project also includes DevOps tasks such as containerizing the model using Docker, pushing the Docker image to Docker Hub, creating Kubernetes deployments and services, and finally deploying and accessing the application.

## Project Structure

1. **Model Finetuning**: The LLAMA2 model is finetuned and its parameters are tweaked for optimal performance.

2. **Streamlit Web Application**: A Streamlit web application is developed to provide a GUI for interacting with the finetuned model.

3. **Dockerization**: The application is containerized using Docker. The `Dockerfile` in the project root can be used to build a Docker image of the application.

4. **Kubernetes Deployment**: The Docker image is deployed to a Kubernetes cluster using a deployment configuration. A service is also created to expose the application.

### Building the Docker Image Locally

To build the Docker image locally, use the `docker build` command. Replace `your-image-name` with the name you want to give to your Docker image.

```bash
docker build -t your-image-name .
```

### Running the Docker Image Locally

```bash
docker run -p 8501:8501 your-image-
```

### Building and Pushing the Docker Image to Docker Hub

To build the Docker image and push it to Docker Hub, use the docker build command followed by the docker push command. Replace yourusername with your Docker Hub username and your-image-name with the name you want to give to your Docker image.

```bash
docker build -t yourusername/your-image-name .
docker push yourusername/your-image-name
```

## Deploying to Kubernetes

### To deploy the application to Kubernetes, apply the deployment and service configurations:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## Accessing the Application

The application can be accessed in two ways:

1. Directly via Docker: If you're running the Docker container directly, you can access the application at http://localhost:8501.

2. Via Kubernetes NodePort Service: If you've deployed the application to Kubernetes and exposed it via a NodePort service, you can access the application at http://localhost:30080.
