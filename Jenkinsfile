pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker compose config
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                    docker compose build web
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker compose up -d
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    sleep 10
                    docker compose ps
                '''
            }
        }
    }
}