
pipeline {
    agent any

    environment {
        STUDENT_NAME = 'Arthur'
        STUDENT_SURNAME = 'Tokarev'
        STUDENT_GROUP = 'IT2-2312'
        STUDENT_ID = 'YOUR_STUDENT_ID'

        IMAGE_NAME = 'tokarev-arthur-devops'
        CONTAINER_NAME = 'tokarev-arthur-jenkins-ci'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git rev-parse --short HEAD'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m compileall -q app/'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f "$CONTAINER_NAME" || true

                    docker run -d \
                      --name "$CONTAINER_NAME" \
                      -e STUDENT_NAME="$STUDENT_NAME" \
                      -e STUDENT_SURNAME="$STUDENT_SURNAME" \
                      -e STUDENT_GROUP="$STUDENT_GROUP" \
                      -e STUDENT_ID="$STUDENT_ID" \
                      "$IMAGE_NAME"

                    sleep 2
                    docker ps --filter "name=$CONTAINER_NAME"
                    docker logs "$CONTAINER_NAME"

                    docker inspect -f '{{.State.Running}}' "$CONTAINER_NAME" | grep -qx true
                    docker logs "$CONTAINER_NAME" | grep -q "Application is running successfully"
                '''
            }
        }
    }

    post {
        success {
            echo "Student: ${env.STUDENT_NAME} ${env.STUDENT_SURNAME}"
            echo "Group: ${env.STUDENT_GROUP}"
            echo "Student ID: ${env.STUDENT_ID}"
            echo "Finished successfully!"
        }

        failure {
            echo "Pipeline failed. Inspect the failing stage."
        }
    }
}
