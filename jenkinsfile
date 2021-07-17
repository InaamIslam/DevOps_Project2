pipeline{
        agent any
        stages{
            stage('Testing'){
                steps{
                    sh "./scripts/test.sh"
                }
            }
            stage('Building Images'){
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