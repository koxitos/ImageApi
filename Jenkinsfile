pipeline {
    agent any 
    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
        GIT_URL = 'https://github.com/koxitos/ImageApi'
        DIR = "${sh 'echo $RANDOM | md5sum | head -c 20; echo;'}"
    }
    stages {
        stage('Test Stage 1: setup') {
            steps {
                sh 'mkdir ${DIR} && cd ${DIR}'
                sh 'git clone ${GIT_URL}'
                sh 'cd ImageApi'
                
                sh 'touch .env'
                sh 'echo DB_NAME="imageAp" > .env'
                sh 'echo DB_USER="imageApi" > .env'
                sh 'echo DB_PASSWORD="imageApi" > .env'

                sh 'echo AWS_STORAGE_BUCKET_NAME = "s3-md-bucket" > .env'

                sh 'cd dev'

                sh 'docker-compose build'
                sh 'docker-compose run web migrate'

                sh 'docker-compose run web test'
            }
        }
    }
}