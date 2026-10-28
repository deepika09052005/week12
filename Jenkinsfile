pipeline {
    agent any

    stages {
        stage('Test') {
    steps {
        bat '"C:\\Users\\kassl\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
        bat 'start /B "" "C:\\Users\\kassl\\AppData\\Local\\Python\\bin\\python.exe" app.py'
        bat 'ping 127.0.0.1 -n 5 > nul'
        bat '"C:\\Users\\kassl\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -v tests/test_registration.py'
    }
}

        stage('Build') {
            steps {
                bat 'docker build -t deepika09052005/week12:latest .'
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                    bat 'docker push deepika09052005/week12:latest'
                }
            }
        }

        stage('Deploy') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
}