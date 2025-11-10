pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies & Run Tests') {
            steps {
                sh '''
                  python3 -m venv venv
                  . venv/bin/activate
                  pip install --upgrade pip
                  pip install -r requirements.txt
                  python -m pytest -q
                '''
            }
        }

       stage('SonarQube Analysis') {
            steps {
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_LOGIN')]) {
                    script {
                        def scannerHome = tool 'sonar-scanner'
                        withSonarQubeEnv('sonarqube-server') {
                            sh """
                              ${scannerHome}/bin/sonar-scanner \
                                -Dproject.settings=sonar-project.properties \
                                -Dsonar.login=${SONAR_LOGIN}
                            """
                        }
                    }
                }
            }
        }
    }
}
