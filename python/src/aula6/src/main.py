import discord
import random
from discord.ext import commands
from gtts import gTTS

# Bot's prefix
BOT_PREFIX = "/"

piadas = [
    "Qual é o doce mais azedo? - O azedo de abelha.",
    "Por que o pato não usa chapéu? - Porque ele tem penas na cabeça.",
    "O que é um pontinho amarelo na janela? - Uma jaqueta amarela!",
    "O que é um pontinho azul na grama? - Um passarinho de calça jeans!",
    "Por que o pombo não bate em ninguém? - Porque ele tem asa!",
    "Por que a vaca foi para o espaço? - Para se encontrar com o vácuo.",
    "Por que o peixe é o animal mais engraçado? - Porque ele vive fazendo gracinha.",
    "Qual o carro mais religioso? - O da Fiat, porque ele é uno.",
    "Por que o cachorro entrou na igreja? - Porque ele era um São Bernardo.",
    "O que é um pontinho vermelho na grama? - Um morango trabalhando de jardinagem.",
    "Por que o livro de matemática estava triste? - Porque ele tinha muitos problemas.",
    "Qual é o carro favorito dos padeiros? - O pão-de-forma.",
    "O que é uma bola nas mãos de um semáforo? - Um bolão vermelho.",
    "Por que a vaca foi para o espaço? - Porque ela queria ser uma muuuulher-astronauta.",
    "Por que o gato não gosta de telefonar? - Porque ele tem medo do arranhafone.",
    "Por que o pombo não consegue achar a chave de casa? - Porque ele sempre acha que está perto, mas nunca está perto o suficiente.",
    "Por que o livro de receitas estava triste? - Porque estava cheio de bolos.",
    "Qual é o sanduíche mais inteligente? - O sanduíche natural.",
    "O que é um pontinho marrom no olho do peixe? - Um peixe-marrom!",
    "Por que o livro de ciências estava nervoso? - Porque estava cheio de problemas.",
    "Por que o cachorro entrou no cinema? - Porque ele queria ver o filme cachorrada.",
    "Qual é o carro mais medroso? - O Fiote.",
    "Por que o pombo não usa relógio? - Porque ele já tem um relógio biológico.",
    "Por que a galinha foi para o espaço? - Porque ela queria botar um ovo de gravidade zero.",
    "O que é um pontinho amarelo na árvore? - Uma banana que perdeu o caminho da fruteira.",
    "Por que o livro de história estava cansado? - Porque tinha muitas páginas.",
    "Qual o doce preferido do átomo? - O pé-de-moléculas.",
    "O que é um pontinho vermelho no meio do mar? - Um caranguejo de biquíni.",
    "Por que o livro de geografia estava perdido? - Porque ele não conseguia achar o mapa.",
    "Qual é o doce mais vaidoso? - O doce de leite, porque ele é uma gostosura.",
    "Por que o cachorro entrou na igreja? - Porque ele queria rezar o pai-nosso.",
    "Qual é o carro mais bagunceiro? - O baguetão.",
    "Por que o peixe não gosta de fazer brincadeiras? - Porque ele tem medo de levar uma ensaboada.",
    "Por que o livro de química estava triste? - Porque estava cheio de reações.",
    "Por que a vaca foi para o espaço? - Porque queria se tornar uma estrela.",
    "Qual é o doce preferido do jardineiro? - O pé-de-moleque.",
    "O que é um pontinho azul na lagoa? - Um peixe no frio.",
    "Por que o livro de português estava nervoso? - Porque estava cheio de pontos finais.",
    "Por que o cachorro entrou na igreja? - Porque queria encontrar a fé cão.",
    "Qual é o carro mais ligado? - O Carro elétrico.",
    "Por que o peixe não gosta de ir à escola? - Porque lá só tem peixinhos.",
    "Por que o livro de biologia estava nervoso? - Porque tinha muita fauna e flora.",
    "Qual é o doce preferido do macaco? - O banana split.",
    "O que é um pontinho verde na lagoa? - Um jacaré de férias.",
    "Por que o livro de física estava cansado? - Porque estava cheio de fórmulas.",
    "Por que o cachorro entrou na igreja? - Porque ele queria buscar a paz de ossos.",
    "Qual é o carro mais gelado? - O geleão.",
    "Por que o pombo não usa óculos? - Porque ele já tem lente natural.",
    "Por que a vaca foi para o espaço? - Porque queria ver se o leite é realmente zero lactose.",
    "Qual é o doce mais democrático? - O doce de leite, porque ele é uma gostosura para todos.",
    "Por que o cachorro entrou na igreja? - Porque ele queria encontrar o seu cachorro-irmão.",
    "Qual é o carro mais rápido do mundo? - O caminhão da coleta de lixo, ele sempre vai em frente.",
    "Por que o peixe não gosta de cinema? - Porque ele prefere filmes em 3D, três de sua própria dimensão.",
    "Por que o livro de inglês estava cansado? - Porque tinha muitas letras.",
    "Qual é o doce mais divertido? - O doce de abóbora, porque é uma delícia engraçada.",
    "O que é um pontinho verde no gelo? - Um alface congela-do.",
    "Por que o livro de matemática não gosta de ser lido em voz alta? - Porque sempre acaba em problemas.",
    "Por que o cachorro entrou na igreja? - Porque ele queria se confessar.",
    "Qual é o carro mais curioso? - O carro de polícia, sempre investigando.",
    "Por que o peixe não gosta de tirar fotos? - Porque sempre sai mal na escama.",
    "Por que o livro de história estava com frio? - Porque tinha muitos fatos."
]

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents.all())

# Event to print bot is ready
@bot.event
async def on_ready():
    print('has connected to Discord!')

# Ping-Pong Command
@bot.command(name='gerarPiada')
async def gerarPiada(ctx):
    pick = random.choice(piadas)
    #tts = gTTS(text=pick, lang='pt')

    # Save the TTS to a file
    #tts.save('tts.mp3')

    # Send the TTS as a file
    await ctx.send(f'A gerar uma piada...\n{pick}\nBot Made By: Ricardo Almeida.',tts=True)
    #await ctx.send(file=discord.File('tts.mp3'))

# Run the bot with your token
bot.run('MTIyNTQ5NDQ5MzI0NDAzNTA5Mg.GSTV5r.6263y1I7mwNdhMjZESS8NEgTP2XdaXJ4miZ4LI')