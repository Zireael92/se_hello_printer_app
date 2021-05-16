pipeline {
    agent any
    stages {
        stage('Debs') {
            steps {
	            sh 'make deps'
              }
        }
        stage('Test') {
            steps {
	            sh 'make test'
              }
        	}
        }
    }
