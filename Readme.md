# SERVER DE JEU

###Requests type:
    signin:
        "header": {
            "type": "signin"
        }, "body": {
            "username": Username,
        }

    signout:
        "header": {
            "type": "signout",
            "token": self.token,
        }, "body": {
        }
    inQueue: 
        "header": {
                "type": "inQueue",
                "token": self.token,
            },
            "body": {
                "username": Username,
            }
Il manque beaucoup de routes, notemment les routes concernant
les parties.

### Network
 Le network est incomplet et n'est pas encore fonctionnel.
    

## Problèmes rencontrés:
Nous avons eu beaucoup de mal avec les délais car nous avions 
fait un mauvais choix concernant la technologies utilisées. Nous avons donc tout recommencé
il y a 2 semaines ce qui ne nous a pas permis de réaliser le projet dans son intégralité.