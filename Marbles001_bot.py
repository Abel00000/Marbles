#importem la llibreria que utilitzarem anomenada telegram
import logging
import telegram
import random

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler,dispatcher, handler,updater, MessageHandler, Filters

TOKEN = "2023962833:AAFkARwaeKjdDgvb19Gp6Wq3tl8fLsD2d2g" 
updater = Updater(TOKEN)

#Declaro les caniques de l'usuari
puntos_Usuario = 10
puntos_Maquina = 10


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__) 

# Explica en que consisteix el joc i dona inici al joc.
def start(update: Update, context): 
    puntos_Usuario = 10
    puntos_Maquina = 10
    update.message.reply_text(
            "Aquest bot et permet jugar a Marbles, es un joc que tracta sobre aconseguir les bales del teu oponent. Cadascú té 10 bales al començament de la partida i haurà d'acabar quan un dels dos aconsegueixi tenir 20 bales. \nSi vols PAR introdueix /par. Si vols IMPAR introdueix /impar."
            )
    

#Aquest comandament serveix per donar suport al usuari i que sàpiga com interactuar amb el bot.
def help_command(update: Update, context):
    update.message.reply_text(
        "Entra /start per poder començar a jugar. \nEntra /par si vols ecollir un número PAR. \nEntra /impar si vols escollir un número IMPAR."
    )

#Donar un número IMPAR
def impar(update: Update, context):
    bot = context.bot
    text = update.message.text

    contador = 0
    global puntos_Usuario
    global puntos_Maquina 
    apostar_Maquina = 0
    apostar_Usuario = 0

    # Random del bot
    apostar_Maquina = random.randint(1,puntos_Maquina)


    # Comptador de les caniques que té l'usuari.
    update.message.reply_text(
        "Caniques del Jugador: "
        )
    update.message.reply_text(
        puntos_Usuario
        )

    # Si l'usuari escull l'opció /IMPAR farà el següent.
    
    if apostar_Maquina % 2 == 1:
                    update.message.reply_text(
                    "Es IMPAR."
                    )
                    update.message.reply_text(
                    "El bot ha apostat:"
                    )
                    update.message.reply_text(
                    apostar_Maquina
                    )
                    puntos_Maquina = puntos_Maquina - apostar_Maquina
                    puntos_Usuario = puntos_Usuario + apostar_Maquina

    if apostar_Maquina % 2 == 0:
                    update.message.reply_text(
                    "ERA PAR!!!"
                    )
                    update.message.reply_text(
                    "El bot ha apostat:"
                    )
                    update.message.reply_text(
                    apostar_Maquina
                    )
                    puntos_Maquina = puntos_Maquina + apostar_Maquina
                    puntos_Usuario = puntos_Usuario - apostar_Maquina

    update.message.reply_text(
        "Caniques que té ara el Jugador: "
        )
    update.message.reply_text(
        puntos_Usuario
        )

    if puntos_Usuario > 0 and puntos_Usuario <20:
            update.message.reply_text(
            "Introdueix /par o /impar per seguir jugant:"
            )

    # Si el bot té menys d'1 canica ha perdut.
    if puntos_Maquina < 1: 
            update.message.reply_text(
            "Has Guanyat!!!"
            )
            

        # Si l'usuari té menys d'1 canica ha perdut.
    if puntos_Usuario < 1:
            update.message.reply_text(
            "Has Perdut!!!"
            )


def par(update: Update, context):
    bot = context.bot
    text = update.message.text

    contador = 0
    global puntos_Usuario
    global puntos_Maquina 
    apostar_Maquina = 0
    apostar_Usuario = 0

    # Random del bot
    apostar_Maquina = random.randint(1,puntos_Maquina)


    # Comptador de les caniques que té l'usuari.
    update.message.reply_text(
        "Caniques del Jugador: "
        )
    update.message.reply_text(
        puntos_Usuario
        )


    if apostar_Maquina % 2 == 0:
                    update.message.reply_text(
                    "ES PAR!!!"
                    )
                    update.message.reply_text(
                    "El bot ha apostat:"
                    )
                    update.message.reply_text(
                    apostar_Maquina
                    )
                    puntos_Maquina = puntos_Maquina - apostar_Maquina
                    puntos_Usuario = puntos_Usuario + apostar_Maquina

    if apostar_Maquina % 2 == 1:
                    update.message.reply_text(
                    "ERA IMPAR!!!"
                    )
                    update.message.reply_text(
                    "El bot ha apostat:"
                    )
                    update.message.reply_text(
                    apostar_Maquina
                    )
                    puntos_Maquina = puntos_Maquina + apostar_Maquina
                    puntos_Usuario = puntos_Usuario - apostar_Maquina

    #Caniques que li van quedant al usuari en cada torn
    update.message.reply_text(
        "Caniques que té ara el jugador: "
        )
    update.message.reply_text(
        puntos_Usuario
        )

    if puntos_Usuario > 0 and puntos_Usuario <20:
            update.message.reply_text(
            "Introdueix /par o /impar per seguir jugant:"
            )

    # Si el bot té menys d'1 canica ha perdut.
    if puntos_Maquina < 1: 
            update.message.reply_text(
            "Has Guanyat!!!"
            )
            

        # Si l'usuari té menys d'1 canica ha perdut.
    if puntos_Usuario < 1:
            update.message.reply_text(
            "Has Perdut!!!"
            )

#Amb el metòde main farem correr al bot
def main():
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(CommandHandler('impar', impar))
    dispatcher.add_handler(CommandHandler('par', par))

    #Fem que s'inicï el bot
    updater.start_polling()

    updater.idle()


main()

