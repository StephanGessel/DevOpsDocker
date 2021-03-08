pipeline {
    agent any
    environment {
        registry = "sgessel/my_repo"
        registryCredential = 'sgessel'
        dockerImage = ''
        }
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5' ))
    }
    stages {
        stage('Pull Code') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
                git 'https://github.com/StephanGessel/DevOpsDocker.git'
            }
        }
        stage('run rest app server ') {
            steps {
                script {
                    sh 'nohup python3.9 rest_app.py &'

                }
            }
        }

        stage('run backend testing') {
            steps {
                script {
                    sh 'python3.9 backend_testing.py'

                }
            }
        }
        stage('run clean environment ') {
            steps {
                script {
                    sh ' python3.9 clean_environment.py'

                }
            }
        }
        stage('build docker image ') {
            steps {
                script {
                    sh ' docker build -t projectdocker .'
                }
            }
        }
         stage('build and push image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    docker.withRegistry('', registryCredential) {
                    dockerImage.push()
                    }
                }
            }
        post{
        always{
            sh "docker rmi $registry:$BUILD_NUMBER"
        }
       }
      }

        stage('Set compose image version ') {
            steps {
                script {
                    sh ' echo IMAGE_TAG=${BUILD_NUMBER} > .env'
                }
            }
        }
        stage('run docker compose ') {
            steps {
                script {
                    sh ' docker-compose up -d '
                }
            }
        }
        stage('run docker backend testing') {
            steps {
                script {
                    sh ' python3.9 docker_backend_testing.py'
                }
            }
        }
         stage('run clean docker environment ') {
            steps {
                script {
                    sh 'docker-compose down'
                }
            }
        }
        stage('deploy helm with latest build') {
            steps {
                script {
                    sh 'helm upgrade --install k8s-check mychart-0.1.0.tgz --set image.tag=${BUILD_NUMBER}'
                }
            }
        }
        stage('url to file') {
            steps {
                script {
                    sh 'minikube service k8s-check-mychart --url > k8s_url.txt'
                }
            }
        }
        stage ('wait for pods to start (sleep)') {
            steps {
                sleep 30
            }
        }
        stage('k8s check') {
            steps {
                script {
                    sh 'python3.9 k8s_backend_testing.py'
                }
            }
        }
        stage('clean k8s environment') {
            steps {
                script {
                    sh 'helm delete k8s-check'
                }
            }
        }
    }
}
