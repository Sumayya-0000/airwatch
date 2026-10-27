pipeline {
    agent any

    environment {
        DOCKER_USERNAME = 'sumayyasadaf'
        IMAGE_NAME = 'sumayyasadaf/airwatch'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Sumayya-0000/airwatch.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        ```groovy
stage('Login to Docker Hub') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'DOCKER_USERNAME',
            passwordVariable: 'DOCKER_PASSWORD'
        )]) {
            bat 'echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin'
        }
    }
}
```

        stage('Push Docker Image') {
            steps {
                bat 'docker push %IMAGE_NAME%:%IMAGE_TAG%'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
                bat 'kubectl set image deployment/airwatch airwatch=%IMAGE_NAME%:%IMAGE_TAG%'
                bat 'kubectl rollout status deployment/airwatch --timeout=120s'
            }
        }
    }

    post {
        success {
            echo 'AirWatch CI/CD pipeline completed successfully!'
        }
        failure {
            echo 'AirWatch CI/CD pipeline failed. Check the console output.'
        }
    }
}