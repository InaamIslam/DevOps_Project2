pipeline{
        agent any
        stages { 
            stage('Setup & Installations'){
                steps{
                    sh "./scripts/setup.sh"
                }
            }
            stage('Testing'){
                steps{
                    sh "./scripts/test.sh"
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