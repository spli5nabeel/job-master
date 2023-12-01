pipeline {
    agent any
    tools{
        PythonInstallation python
    }

    stages {
        stage('Initialize'){
            steps{
                sh '''
                    echo "PATH = ${PATH}"
                    python --version
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
