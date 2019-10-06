# Arena-Bot

Un bot Discord écrit en Python conçu pour gérer notre serveur et collecter les résultats de nos membres sur des sites tels que Root-Me ou WeChall.

```
+-----------------------------------------------------------------------------------------------------------------+
|      ___           ___           ___           ___           ___           ___           ___           ___      |
|     /\  \         /\  \         /\  \         /\  \         /\  \         /\__\         /\  \         /\__\     |
|    /::\  \       /::\  \       /::\  \       /::\  \       /::\  \       /::|  |       /::\  \       /::|  |    |
|   /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \     /:|:|  |      /:/\:\  \     /:|:|  |    |
|  /:/  \:\  \   /:/  \:\  \   /:/  \:\__\   /::\~\:\  \   /::\~\:\  \   /:/|:|  |__   /:/  \:\  \   /:/|:|  |__  |
| /:/__/ \:\__\ /:/__/ \:\__\ /:/__/ \:|__| /:/\:\ \:\__\ /:/\:\ \:\__\ /:/ |:| /\__\ /:/__/ \:\__\ /:/ |:| /\__| |
| \:\  \  \/__/ \:\  \ /:/  / \:\  \ /:/  / \:\~\:\ \/__/ \/__\:\/:/  / \/__|:|/:/  / \:\  \ /:/  / \/__|:|/:/  / |
|  \:\  \        \:\  /:/  /   \:\  /:/  /   \:\ \:\__\        \::/  /      |:/:/  /   \:\  /:/  /      |:/:/  /  |
|   \:\  \        \:\/:/  /     \:\/:/  /     \:\ \/__/        /:/  /       |::/  /     \:\/:/  /       |::/  /   |
|    \:\__\        \::/  /       \::/__/       \:\__\         /:/  /        /:/  /       \::/  /        /:/  /    |
|     \/__/         \/__/         ~~            \/__/         \/__/         \/__/         \/__/         \/__/     |
|                                                                                                                 |
|                                                                                                                 |
|                                         * est fier de vous présenter *                                          |
|                                                                                                                 |
|                                          ____,____, ____,_,  _, ____,                                           |
|                                         (-/_|(-|__)(-|_,(-|\ | (-/_|                                            |
|                                         _/  |,_|  \,_|__,_| \|,_/  |,                                           |
|                                        (     (     (    (     (                                                 |
|                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------+
```

# Pour les utilisateurs

L'installation de ce bot est entièrement à la charge des utilisateurs, nous ne proposons pas ce bot en tant que service. Si vous souhaitez intégrer ce bot à votre serveur discord, il faut donc en faire le déploiement manuellement.

Il existe de nombreuses manière de déployer un bot discord. L'une des plus simple (et gratuite) et de passer par le service [HEROKU APP](). Ce dernier permet par exemple d'héberger des applications python, parfait pour nous puisque ce bot en est justement une ;) !

## Les bonnes adresses pour apprendre à déployer un bot :

+ **Avec heroku** : [vidéo d'aide](https://www.youtube.com/watch?v=BPvg9bndP1U)
+ Nous proposons aussi un [tuto](TUTO.md) pour déployer un bot depuis zéro sur sa propre machine.

## Résumé des commandes offertes par le bot Arena

```
Arena - Bot permettant la collecte et le traitement des scores sur root-me ou wechall

​No Category:
  addUser     Ajoute le challenger <pseudo> à la liste des challengers
  close       Fait jouer le bot à "Local fermé" 
  delUser     Supprime le challenger <pseudo> de la liste des challengers
  flag        Récompense une CTF réussie
  help        Shows this message
  open        Fait jouer le bot à "Local ouvert !" 
  ping        Ping le bot
  publication Publie le classement hebdomadaire des challengers
  rang        Affiche le classement actuel des challengers
  scoreUser   Affiche le score du challenger <pseudo>

Type !help command for more info on a command.
You can also type !help category for more info on a category.
```


# Pour les développeurs

Cette section s'adresse aux développeurs souhaitant contribuer au développement du bot.

## Instructions

Des instructions sur le procédé de création d'un bot discord sont disponibles [ici](TUTO.md). N'hésitez pas à les lires si c'est la première fois que vous codez un bot discord.

## Installation des outils

### Python3

Contribuer au développement de ce bot nécessite l'installation de python3 (*testé en 3.7*). On peut installer python3 depuis [ce lien](https://www.python.org/downloads/)

### Dépendances

Pour que le bot soit fonctionnel, nous utilisons un package appellé [discord.py](https://discordpy.readthedocs.io/en/latest/). Il permet de faire la connexion entre le bot et les services de discord.

Pour installer cette dépendance et commencer à contribuer au développement, vous pouvez saisir les commandes suivantes :

**[1] Clonage des sources**
```shell
$ git clone git@github.com:codeanonorg/Arena-Bot.git
```

**[2] Installation des dépendances**
```shell
$ pip3 install -r requirements.txt
```

**⚠︎** : *cette commande nécessite d'avoir une installation complète de python3*


