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
Testé sous Python 3.7, mais normalement fonctionnel pour Python 3.5.3 <

# Déploiement
## Prérequis

1. Pour commencer, il faut installer la librairie discord à l'aide de l'utilitaire `pip`. Sous linux, il s'agit de la commande :
```shell
    ~$ python3 -m pip install -U discord.py
```

2. On crée ensuite un serveur discord. En supposant que vous ayez déjà un compte, cette opération se fait très
   facilement en appuyant sur le '+' en-dessous de la liste des serveurs se situant à gauche de l'interface

## Mise au monde du Bot

On crée le bot depuis le site officiel de Discord, à l'adresse https://discordapp.com/developers/applications/
La procédure est guidée, mais si jamais vous rencontrez un problème, n'hésitez pas à regarder du côté de la documentation
ci-contre : https://discordapp.com/developers/docs/intro

## Codage du Bot

1. On commence avec la précision de l'encodage ainsi que l'import des librairies
2. On crée ensuite une variable `token` qui recevra le dit token qui représente une longue série de chiffres à garder
   privée
3. On choisi un préfixe qui précèdera les commandes qui invoqueront notre bot, ainsi qu'une petite description
   de ce dernier
4. Pour s'assurer que le bot est actif, on crée une fonction permettant d'afficher dans le terminal \*Bot is ready\*
5. On rajoute la commande de démarrage (dernière ligne du fichier)
5. Enfin, on crée les commandes auxquelles le bot devra répondre

Les commandes auront dans la majorité des cas la même en-tête, à savoir :

    @arena_bot.command()
    async def <commande>(ctx, <param1>, <param2>, ...):

Pour le reste, chaque fonction du programme est commentée dans le but de s'en inspirer, n'hésitez pas à les lire.

## Mise en place du bot

### Initialisation des variables d'environnement
Sous linux, il existe différents *"degrés"* de variables d'environnement dont la configuration change selon les shells utilisés.
De manière très simple, il est possible d'initialiser ces variables en les ajoutant au fichier `/etc/environment` de cette manière :
```shell
# echo "arena_token="AAZEsqdqshjkrzFrDuib1345978qds31435a4ze!$Azesd"" >> /etc/environment
```
### Last step !
Une fois le bot crée et codé, rendez-vous à l'adresse https://discordapp.com/developers/applications/
Cliquez dans la section *Bot* du pannel de gauche, et créez votre bot (vous serez averti que cette action est
irreversible).

On peut donc voir que notre bot a pris vie, et qu'il s'est vu attribuer un *token*. Comme dit précédemment, il doit rester
privé !

La suite se passe dans le panel OAuth :
- on coche Bot
- on sélectionne les permissions (en l'occurrence ici send-message et role-management, ou admin si l'on ne peut pas faire autrement)
- une adresse est alors générée
- il suffit de la coller dans un nouvel onglet
- notre bot apparait alors, déconnecté

Pour le connecter, il suffit d'exécuter dans une console notre script python, et voir s'afficher le message
*Bot is ready*
