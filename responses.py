import random
import discord 
import bot as bt

respostas = {0:'Smt',1:'Cala a boca', 2:'So fala merda', 3 : 'Te odeio' ,
             
4: 'Comi seu pai enquanto sua mãe assistia ',
 5: 'Vc e tao feio que se vc olhar no espelho ele quebra',
 6: 'É por isso que ninguem te ama ',
 7:'Até um espantalho do fandangos trabalha melhor que você',
 8:'Vce tao chata que nem minha avo fumante gosta de vc'}
intents = discord.Intents.default()
intents.message_content = True 
intents.voice_states = True
client = discord.Client(intents=intents)


def handle_responses(message) -> str:
    p_mesasge = message.lower()
   
    
    if p_mesasge == 'ola':
        return 'Eae cara'

    if p_mesasge == 'roll':
        return str(random.randint(1, 6))

    if p_mesasge == 'help':
        return "`Este bot foi criado com intensões de diversão e teste e em um futuro pode ser melhor desenvolvido`"

    if p_mesasge == 'he said':
        return "Lana rey will u serve me a lemonade\ni said yes bill i will\nit's the day of the parade"

    if p_mesasge == 'quem e mariana':
        return 'Mariana e a pessoa mais legal que eu ja conheci e que me faz sorri todos os dias amo ela d+ e faz ela faz parte da minha vida tem pouco tempo mas ela ja esta no meu coração'
    
    if p_mesasge == 'e quem é o pai dela':
        return 'O pai dela e um gostoso'
    

    
    
    
def lara_responses(message) -> str:
    p_mesasge = message.lower()


    if p_mesasge == p_mesasge:
        msg_escolhida = random.randint(0,8)
        msg_fi = respostas[msg_escolhida]
        return msg_fi
    
    
   