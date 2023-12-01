pipeline {
    agent any
   

    stages {
        stage('Initialize'){
            steps{
                sh '''
                sudo apt-get update
                sudo apt-get install python3
                sudo apt-get install python3-pip
                    echo "PATH = ${PATH}"
                    python3 --version
                '''

            }
        }
        stage('SonarQube'){
            steps{
                println "Inside SonarQube"
            }
        }
        stage('Build') {
            steps {
                println "Inside build package..."   
                         
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
