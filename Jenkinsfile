pipeline{
        agent any
        environment{
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
        install = 'true'
        DATABASE_URI = credentials('DATABASE_URI')
        // SECRET_KEY = credentials('SECRET_KEY')
        }
        stages{ 
            stage('Testing'){
                steps{
                    sh "./scripts/test.sh"
                }
            }
            stage('Setup & Installations'){
                steps{
                    sh "./scripts/setup.sh"
                }
            }
            stage('Build Images'){
                steps{
                    sh "./scripts/build.sh"
                }
            }
            stage('Ansible'){
                steps{
                    sh "./scripts/ansible.sh"
                }
            }
            stage('Deploying App'){
                steps{
                    sh "./scripts/deploy.sh"
                }
            }
        }  

    }
