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
                //sh "ls -la"
                //sh "pwd"
                
                sh "touch ImageApi/.env"
                sh "echo DB_NAME='imageAp' > ImageApi/.env"
                sh "echo DB_USER='imageApi' > ImageApi/.env"
                sh "echo DB_PASSWORD='imageApi' > ImageApi/.env"
                sh "echo AWS_STORAGE_BUCKET_NAME = 's3-md-bucket' > ImageApi/.env"

                sh "cd dev"

                sh "docker-compose build"
                sh "docker-compose run web migrate"

                sh "docker-compose run web test"
            }
        }
    }
}