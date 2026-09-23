pipeline {
    agent any

    stages {

        stage('Vault Test') {
            steps {
                withVault(
                    configuration: [
                        vaultUrl: 'https://vault.axror.tech',
                        vaultCredentialId: 'vault-approle-jenkins'
                    ],
                    vaultSecrets: [
                        [
                            path: 'axrortech/data/axrortech',
                            secretValues: [
                                [
                                    envVar: 'TEST_MESSAGE',
                                    vaultKey: 'TEST_MESSAGE'
                                ]
                            ]
                        ]
                    ]
                ) {
                    sh '''
                        test -n "$TEST_MESSAGE"
                        echo "Vault secret successfully loaded!"
                    '''
                }
            }
        }

    }
}