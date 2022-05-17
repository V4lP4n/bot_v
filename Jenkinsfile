    pipeline {
        agent any
         environment{
                        TOKEN = credentials("${BRANCH_NAME}_bot_v")
                    }
        stages{
            stage('env preparation'){
                      steps{
                   sh("cat settings.ini | sed 's/InsertYourTokenHere/${TOKEN}/g' > tmp")
                   sh("mv tmp settings.ini")
                }
            }
            stage('build'){
                steps{

                    sh("docker build --tag bot-${BRANCH_NAME}-v .")
                    sh("docker tag bot-${BRANCH_NAME}-v kube01:5000/bot-${BRANCH_NAME}-v")
                    sh("docker push kube01:5000/bot-${BRANCH_NAME}-v")
                }
            }
            stage('run'){
            steps{
               sh("kubectl apply -f ./manifest_${BRANCH_NAME}.yml")
               sh("kubectl rollout restart deployment/bot-app-${BRANCH_NAME}")
            }
            }
        }
    } 
 