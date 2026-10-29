
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sumayyasadaf/airwatch'
        IMAGE_TAG  = 'latest'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out AirWatch project from GitHub'

                git branch: 'main',
                    url: 'https://github.com/Sumayya-0000/airwatch.git'
            }
        }

        stage('Install Dependencies and Run Tests') {
            steps {
                echo 'Installing dependencies and running tests'

                bat 'python --version'
                bat 'python -m pip install --upgrade pip'

                // Install dependencies if requirements.txt exists
                bat 'if exist requirements.txt python -m pip install -r requirements.txt'

                // Run pytest only if tests are present
                bat 'if exist tests (python -m pytest -v) else (echo No tests directory found; skipping pytest)'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building AirWatch Docker image'

                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        

stage('Login to Docker Hub') {
    steps {
        echo 'Logging in to Docker Hub'

        withCredentials([
            usernamePassword(
                credentialsId: 'dockerhub-creds',
                usernameVariable: 'DH_USERNAME',
                passwordVariable: 'DH_PASSWORD'
            )
        ]) {
            bat '''
                @echo off
                echo %DH_PASSWORD% | docker login -u "%DH_USERNAME%" --password-stdin
            '''
        }
    }
}



        stage('Push Docker Image') {
            steps {
                echo 'Pushing AirWatch image to Docker Hub'

                bat 'docker push %IMAGE_NAME%:%IMAGE_TAG%'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying AirWatch to Kubernetes'

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

        always {
            echo 'AirWatch pipeline execution finished.'
        }
    }
}
