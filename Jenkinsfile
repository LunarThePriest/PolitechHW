pipeline{
  agent any
  stages{
    stage('Uptime normal'){
      steps{
        echo '==========uptime normal=========='
        sh 'uptime'
      }
    }
    stage('Uptime from script'){
      steps{
        echo '==========uptime from script=========='
        sh './script.sh'
      }
    }
  } 
}
