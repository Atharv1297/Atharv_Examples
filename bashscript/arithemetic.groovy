pipeline {
    agent any
    stages {
        
        stage('addition') {
            steps {
                sh 'bash /var/lib/jenkins/bashscript/addition.sh ${firstnumber} ${secondnumber}'
            }  
        }
        stage('substraction') {
            steps {
                sh 'bash /var/lib/jenkins/bashscript/substraction.sh ${firstnumber} ${secondnumber}'
            }  
        }
        stage('division') {
            steps {
                sh 'bash /var/lib/jenkins/bashscript/division.sh ${firstnumber} ${secondnumber}'
            }  
        }
