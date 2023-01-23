pipeline {
    agent any 
    environment {
        DISABLE_AUTH = "true"
        DB_ENGINE    = "sqlite"
        GIT_URL = "https://github.com/koxitos/ImageApi"
        DIR = "${sh 'echo $RANDOM | md5sum | head -c 20; echo;'}"
    }
    stages {
        stage('Test Stage 1: setup') {
            steps {
                sh "ls -la"
                sh "pwd"
                // bash 'git clone ${env.GIT_URL}'
                // bash 'cd ImageApi'
                
                // bash 'touch .env'
                // bash 'echo DB_NAME="imageAp" > .env'
                // bash 'echo DB_USER="imageApi" > .env'
                // bash 'echo DB_PASSWORD="imageApi" > .env'

                // bash 'echo AWS_STORAGE_BUCKET_NAME = "s3-md-bucket" > .env'

                // bash 'cd dev'

                // bash 'docker-compose build'
                // bash 'docker-compose run web migrate'

                // bash 'docker-compose run web test'
            }
        }
    }
}