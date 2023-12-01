pipeline {
    agent any
   

    stages {
        stage('Initialize'){
            steps{
                sh '''
                apt-get update
                apt-get install python3
                apt-get install python3-pip
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
