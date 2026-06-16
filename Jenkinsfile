pipeline{
    agent any

      stages{
        stage('Github'){
            steps{
                git branch:'main',
                url:'https://github.com/Sai-Adimulam/Deploy-Docker-Application-using-Rollback-Deployment'
            }
        }
        stage('Build Docker image'){
            steps{
                sh 'docker build -t app-3:v1 .'
            }
        }
        stage('AWS Authenticate Ecr'){
            steps{
                sh 'aws ecr get-login-password --region ap-south-2 |docker login --username AWS --password-stdin 908708651361.dkr.ecr.ap-south-2.amazonaws.com'
            }
        }
        stage('Tag Image to ECR'){
            steps{
                sh 'docker tag app-3:v1 908708651361.dkr.ecr.ap-south-2.amazonaws.com/app-3:v1 '
            }
        }
        stage('Psuh Image to ECR'){
            steps{
                sh 'docker push 908708651361.dkr.ecr.ap-south-2.amazonaws.com/app-3:v1'
            }
        }
        stage('Deploy ECS'){
            steps{
                sh '''
                aws ecs update-service \
                --cluster app-3-cluster \
                --service app-3-task-service-yrwvctle \
                --force-new-deployment 
                '''
            }
        }
      }
}
