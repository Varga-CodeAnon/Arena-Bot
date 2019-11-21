#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import discord
import requests
from discord.ext import commands
import asyncio
import datetime
import time
import os
from ast import literal_eval

# ( () |) [-   /\ |\| () |\|

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ENV @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
rootme_list = literal_eval(os.environ['arena_rm_list'])
wechall_list = literal_eval(os.environ['arena_wc_list'])

codeanon_id = int(os.environ['arena_ca_id'])
ctf_chan_id = int(os.environ['arena_ctf_id'])
test_chan_id = int(os.environ['arena_test_id'])

flag_ctf_rentree = os.environ['arena_flag']
token = os.environ['arena_token']
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ #


# -------------------------------- INTRO ------------------------------------ #
description = """Arena - Bot permettant la collecte et le traitement des scores sur root-me ou wechall"""
arena_bot = commands.Bot(command_prefix='!', description=description)
# Armorçage du bot
print('---------------')
print(' *-= Arena =-* ')
print('---------------')
print('Starting Bot...')


@arena_bot.event
async def on_ready():  # quand le bot est prêt...
    game = discord.Game("se réveiller")
    await arena_bot.change_presence(status=discord.Status.idle, activity=game)
    # ...affiche le statut idle:"Se réveiller"...
    print('*Bot is ready*')  # ... et affiche dans le terminal *Bot is ready*


@arena_bot.event
async def on_raw_reaction_add(reaction):
    message_id = reaction.message_id
    if message_id == 619522439545749514: # Message de bienvenue
        server = arena_bot.get_guild(codeanon_id)  # on sélectionne le serveur CodeAnon
        role = None

        # on crée les associations emoji/role a l'aide de leur code point
        # on peut l'obtenir en tapant dans discord :
        #              \:shinto_shrine:
        if reaction.emoji.name == '🇨':
            role = discord.utils.get(server.roles, name='cybersec')
        elif reaction.emoji.name == '🇵':
            role = discord.utils.get(server.roles, name='programmation')
        elif reaction.emoji.name == '🇷':
            role = discord.utils.get(server.roles, name='réseau&web')
        elif reaction.emoji.name == '🇸':
            role = discord.utils.get(server.roles, name='système')
        elif reaction.emoji.name == '🇮':
            role = discord.utils.get(server.roles, name='ia&maths')

        if role is not None:  # si le role choisi ne fait pas parti des 5 ci-dessus
            member = discord.utils.find(lambda m: m.id == reaction.user_id, server.members)
            await member.add_roles(role)
        print("done")

    if message_id == 647057933045202945: # Message d'annonce du rôle chaman
        server = arena_bot.get_guild(codeanon_id)  # on sélectionne le serveur CodeAnon
        role = None

        if reaction.emoji.name == '🧙‍♂️':
            role = discord.utils.get(server.roles, name='Chaman')

        if role is not None:
            member = discord.utils.find(lambda m: m.id == reaction.user_id, server.members)
            await member.add_roles(role)
        print("done")


@arena_bot.event
async def on_raw_reaction_remove(reaction):
    message_id = reaction.message_id
    if message_id == 619522439545749514:
        server = arena_bot.get_guild(codeanon_id)  # on sélectionne le serveur CodeAnon
        role = None

        # on crée les associations emoji/role a l'aide de leur code point
        # on peut l'obtenir en tapant dans discord :
        #              \:poop:
        if reaction.emoji.name == '🇨':
            role = discord.utils.get(server.roles, name='cybersec')
        elif reaction.emoji.name == '🇵':
            role = discord.utils.get(server.roles, name='programmation')
        elif reaction.emoji.name == '🇷':
            role = discord.utils.get(server.roles, name='réseau&web')
        elif reaction.emoji.name == '🇸':
            role = discord.utils.get(server.roles, name='système')
        elif reaction.emoji.name == '🇮':
            role = discord.utils.get(server.roles, name='ia&maths')

        if role is not None:  # si le role est choisi fait parti des 5 ci-dessus
            member = discord.utils.find(lambda m: m.id == reaction.user_id, server.members)
            await member.remove_roles(role)
        print("done")


# ------------------------------ DEFINITIONS -------------------------------- #
async def logs(ctx, nom):
    """Permet de conserver un log des commandes utilisées"""
    server = arena_bot.get_guild(codeanon_id)  # on sélectionne le serveur CodeAnon
    user = ctx.message.author  # on sélectionne l'utilisateur de discord
    member = server.get_member(user.id)  # on l'associe à un utilisateur du serveur
    channel = arena_bot.get_channel(621785230675673098)  # on sélectionne le chan logs
    await channel.send(str(member) + " a utilisé la commande " + str(nom))  # et on envoie le tout


def user_rootme(pseudo):
    """Verifie qu'un utilisateur est bien dans la bdd de root-me"""
    url_rootme = 'https://www.root-me.org/' + pseudo + '?lang=fr'
    page_rootme = requests.get(url_rootme)
    return page_rootme.status_code == 200
    # renvoie vrai ou faux en fonction de l'existence du pseudo


def user_wechall(pseudo):
    """Verifie qu'un utilisateur est bien dans la bdd de wechall"""
    url_wechall = 'http://www.wechall.net/profile/' + pseudo
    page_wechall = requests.get(url_wechall)
    text = page_wechall.text  # on receptionne le code source de la page, et on la piege dans une variable
    return text.find(pseudo + "`s Profile") != -1
    # renvoie vrai ou faux en fonction de l'existence du pseudo


def score_rootme(pseudo):
    """Retourne le score du challenger <pseudo>"""
    # Note : La vérification de la présence de l'user
    # dans la bdd root-me est faite avant l'appel de la fonction, pas dans sa définition
    url = 'https://www.root-me.org/' + pseudo + '?lang=fr'
    page = requests.get(url)
    text = page.text  # on receptionne le code source de la page, et on la piege dans une variable
    indice_points = text.find("squelettes/img/valid.svg?1566650916") + 105  # C'est à cette position qu'est placé le score du challenger
    score = ''
                 
    while text[indice_points] != '<':  # on parcourt le score
        score += text[indice_points]
        indice_points += 1
    if score == '':
        score = '0'   

    return score


def score_wechall(pseudo):
    """Retourne le score du challenger <pseudo>"""
    # Note : La vérification de la présence de l'user
    # dans la bdd wechall est faite avant l'appel de la fonction, pas dans sa définition
    url = 'http://www.wechall.net/profile/' + pseudo
    page = requests.get(url)
    text = page.text  # on receptionne le code source de la page, et on la piege dans une variable
    indice_points = text.find("totalscore") + 14  # C'est à cette position qu'est placé le score du challenger
    score = ''
    while text[indice_points] != '.':  # on parcourt le score
        score += text[indice_points]
        indice_points += 1

    return score


def tableau():
    """Retourne un liste de tuples python contenant la liste des joueurs ainsi que leurs scores"""
    table = []
    for pseudo in rootme_list:
        table.append((int(score_rootme(pseudo)), pseudo))
        time.sleep(0.5)  # permet aux requtes de ne pas etre bloques par root-me
    table.sort()
    table.reverse()
    return table  # notre liste de tuple est maintenant classée par score décroissant


async def classement_hebdo():
    """Classement hebdomadaire des challengers"""
    print("OK")
    channel = arena_bot.get_channel(ctf_chan_id)  # on sélectionne le chan root-me
    # channel = arena_bot.get_channel(test_chan_id)    # todo: à décommenter pour les tests

    liste = tableau()  # on récupère le classement
    reponse = '*Et voilà le classement de la semaine ! :flag_black:\nBravo à **' \
              + liste[0][1] + '** qui est en première position !' + '\n```ruby'
    # le ruby est simplement là pour une coloration syntaxique des scores
    for challenger in liste:
        if challenger[1] == "hug0-351012":
            reponse += "\n- " + "hug0" + " : " + str(challenger[0]) + " pts"
            continue
        reponse += "\n- " + challenger[1] + " : " + str(challenger[0]) + " pts"
    await channel.send(reponse + '```' + "\nÀ vendredi prochain ! :flag_black:*")  # et on envoie le tout
#    await start_timer()  # on relance pour le vendredi prochain


# ------------------------------- MINUTEUR ---------------------------------- #
def dans_1mn():
    """Renvoie la prochaine minute"""
    now = datetime.datetime.now()
    date = now + datetime.timedelta(minutes=1)
    return datetime.datetime(date.year, date.month, date.day, date.hour, date.minute)


def vendredi_pro_18h():
    """Calcule la date du prochain vendredi:18h à compter de l'exécution"""
    now = datetime.datetime.now()
    day = now.weekday()  # attribue un indice aux jour de la semaine (lundi = 0)
    next_vendredi = (4-day) % 7  # nombre de jour restant avant vendredi
    if day == 4 and now.time() > datetime.time(18, 00):
        next_vendredi = 7  # après 18h, il faudra attendre une semaine
    date_next_vendredi = now + datetime.timedelta(days=next_vendredi)

    return datetime.datetime(date_next_vendredi.year, date_next_vendredi.month, date_next_vendredi.day, 18, 00)


async def wait_for(date):
    """Attends jusqu'à la date spécifiée"""
    now = datetime.datetime.now()
    remaining = (date - now).total_seconds()  # désigne le temps restant en secondes
    while remaining > 86400:
        await asyncio.sleep(86400)  # on empêche la fonction asyncio.sleep de dormir plus de 24h (raisons techniques)
    await asyncio.sleep(remaining)


async def run_at(date, coroutine):
    """Exécute une co-routine à la date spécifiée"""
    await wait_for(date)  # on attend la date spécifiée
    return await coroutine  # et on renvoie la coroutine pour son exécution


async def start_timer():
    """Paramètre une minuterie pour l'exécution différée/répétée d'une tache"""
    loop = arena_bot.loop  # on se greffe sur la boucle d'execution du bot
    rappel = vendredi_pro_18h()
    print(rappel)
    # rappel = dans_1mn()  # todo: à décommenter pour les tests
    loop.create_task(run_at(rappel, classement_hebdo()))
    # On cree une tache qui va executer la coroutine classement_hebdo() au travers de la coroutine run_at()
    # Ainsi, on ne bloque pas le thread principal


# ------------------------------- COMMANDES --------------------------------- #
@arena_bot.command()
async def ping(ctx):
    """Ping le bot"""
    await ctx.send(f"*Pong, vitesse de {round(arena_bot.latency * 1000)}ms*")


@arena_bot.command()
async def addUser(ctx, pseudo):
    """Ajoute le challenger <pseudo> à la liste des challengers"""
    if user_rootme(pseudo):
        if pseudo not in rootme_list:
            rootme_list.append(pseudo)
            await ctx.send("*Nouveau challenger root-me inscrit : " + pseudo + ". Bonne chance ! :flag_black:*")
        else:
            await ctx.send("*Ce challenger est déjà inscrit ici. Son score root-me est de "
                           + score_rootme(pseudo) + " points.*")

    if user_wechall(pseudo):
        if pseudo not in wechall_list:
            wechall_list.append(pseudo)
            await ctx.send("*Nouveau challenger WeChall inscrit : " + pseudo + ". Bonne chance ! :flag_black:*")
        else:
            await ctx.send("*Ce challenger est déjà inscrit ici. Son score WeChall est de "
                           + score_rootme(pseudo) + " points.*")

    if not user_rootme(pseudo) and not user_wechall(pseudo):
        await ctx.send("*L'utilisateur ne semble pas exister dans la "
                       "base de données root-me, ni dans celle de WeChall.*")

    await logs(ctx, "addUser")


@arena_bot.command()
async def delUser(ctx, pseudo):
    """Supprime le challenger <pseudo> de la liste des challengers"""

    if pseudo in rootme_list:
        rootme_list.remove(pseudo)
        await ctx.send("*Le challenger " + pseudo + " a quitté la compétition root-me.*")

    if pseudo in wechall_list:
        wechall_list.remove(pseudo)
        await ctx.send("*Le challenger " + pseudo + " a quitté la compétition WeChall.*")
    else:
        await ctx.send("*Ce challenger n'était pas inscrit.*")
    await logs(ctx, "delUser")


@arena_bot.command()
async def scoreUser(ctx, pseudo):
    """Affiche le score du challenger <pseudo>"""
    if pseudo in rootme_list and pseudo in wechall_list:
        # ce filtre permet de n'effectuer la commande de vérification qu'une seule fois
        # autrement dit, au lieu de vérifier dans chaque fonction la présence d'un challenger dans la bdd root-me,
        # cette vérification est sulement faite lors de l'admission dans le fichier 'rootme_list'
        await ctx.send("*" + pseudo + " : " + score_rootme(pseudo) + " pts sur root-me, et "
                       + score_wechall(pseudo) + " pts sur WeChall.*")

    elif pseudo in rootme_list:
        await ctx.send("*" + pseudo + " : " + score_rootme(pseudo) + " pts sur root-me.*")

    elif pseudo in wechall_list:
        await ctx.send("*" + pseudo + " : " + score_wechall(pseudo) + " pts sur WeChall.*")

    else:
        await ctx.send("*Ce challenger n'est pas inscrit.*")
    await logs(ctx, "scoreUser")


@arena_bot.command()
async def rang(ctx):
    """Affiche le classement actuel des challengers"""
    liste = tableau()
    reponse = ""

    for challenger in liste:

        if challenger[1] == "hug0-351012":
            reponse += "\n- " + "hug0" + " : " + str(challenger[0]) + " pts"
            continue

        reponse += "\n- " + challenger[1] + " : " + str(challenger[0]) + " pts"
    await ctx.send('```ruby' + reponse + '```')  # idem, le ruby est simplement là pour une coloration stylée


@arena_bot.command()
async def publication(ctx, now=None):
    """Publie le classement hebdomadaire des challengers"""
    await logs(ctx, "publication")
#    await start_timer()  # on demmare un compteur
    if now is not None:
        await classement_hebdo()


@arena_bot.command()
async def flag(ctx, drapeau):
    """Récompense une CTF réussie"""
    if drapeau == flag_ctf_rentree:
        server = arena_bot.get_guild(codeanon_id)  # on sélectionne le serveur CodeAnon
        user = ctx.message.author  # on sélectionne l'utilisateur de discord
        member = server.get_member(user.id)  # on l'associe à un utilisateur du serveur
        role = discord.utils.get(server.roles, id=615790340854644747)
        # on sélectionne le rôle du serveur à attribuer avec son id
        await logs(ctx, drapeau)
        await member.add_roles(role)  # on attribue le rôle

        member_name = str(member)
        await ctx.author.send("*Bravo " + member_name[:-5] + " ! Vous avez désormais le rôle **" + str(role.name)
                              + "** en guise de trophée, regardez votre profil :flag_black:*")


@arena_bot.command()
async def open(ctx):
    """Fait jouer le bot à "Local ouvert !" """
    game = discord.Game("Local ouvert !")
    await logs(ctx, "open")
    await arena_bot.change_presence(status=discord.Status.online, activity=game)


@arena_bot.command()
async def close(ctx):
    """Fait jouer le bot à "Local fermé" """
    game = discord.Game("Local fermé")
    await logs(ctx, "close")
    await arena_bot.change_presence(status=discord.Status.dnd, activity=game)


# @arena_bot.command()
# async def bienvenue(ctx):
#     await ctx.send("""
#     Ce discord possède 5 thématiques principales qui sont :
#         - La Cybersécurité
#         - La Programmation
#         - Réseau & Web
#         - Système
#         - IA & Maths
#
# Pour vous abonner à une section, n'hésitez pas à réagir à ce message avec \
# la lettre correspondante !""")

@arena_bot.command()
async def chaman(ctx):
    await ctx.send("""
    Un nouveau rôle a été ajouté, celui de **Chaman**.
    Un *chaman* est *"un sage, un thérapeute, un conseiller"* de l'informatique.
    Si vous souhaitez aider les membres du serveur sur des questions relatives à \
    leurs cursus scolaire et que vous avez la fibre d'un tuteur, alors \
    attribuez-vous ce rôle en sur 'icone'

    Il permettra aux membres ayant besoin d'aide au niveau de leurs cours \
    d'invoquer les @Chaman dans le chan #licence, ou de les identifier plus \
    facilement pour leur envoyer un message privé.""")

# ================================== MAIN =================================== #
arena_bot.run(token)  # on pouvait difficilement faire plus court

