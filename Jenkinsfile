pipeline {
    agent any

    environment {
        TESTS_CONTAINER = 'integ-tests'
    }

    options{
        disableConcurrentBuilds()
        timeout(time: 5, unit: 'MINUTES')
    }

        stage('Start service') {
            steps{
                sh('cd app/ && docker-compose up -d --scale app=5')
            }
        }

        stage('Run integration tests') {
            steps{
                sh('cd tests/ && docker build . -t integration-tests')
                sh('docker run --network=host --name ${TESTS_CONTAINER} integration-tests')
            }
        }
    
    post {
        always {
            sh('docker cp ${TESTS_CONTAINER}:/allure-results ${WORKSPACE}')
            allure ([results: [[path: 'allure-results']]])
            sh('cd app/ && docker-compose down')
            sh('docker rm ${TESTS_CONTAINER}')
            cleanWs()
        }
        failure {
            sendEmailOnFailure()
        }
    }
}
