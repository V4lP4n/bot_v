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

                    sh("docker build --tag bot-v-${BRANCH_NAME} .")
                    sh("docker tag bot-v-${BRANCH_NAME} kube01:5000/bot-v-${BRANCH_NAME}")
                    sh("docker push kube01:5000/bot-v-${BRANCH_NAME}")
                }
            }
            stage('run'){
            steps{
               sh("kubectl apply -f ./manifest_${BRANCH_NAME}.yml")
               sh("kubectl rollout restart deployment/bot-v-${BRANCH_NAME}")
            }
            }
        }
    } 
 