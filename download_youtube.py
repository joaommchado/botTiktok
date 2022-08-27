#bibliotecas que serão utilizadas no video
from ast import main
from distutils.command.upload import upload
from pytube import YouTube
from pytube import Playlist
from pytube import Channel
import random
import os
from moviepy.editor import VideoClip, VideoFileClip

#Lista dos canais que fazem corte
canais = {}
#Cortes do Flow
canais[0] = "https://www.youtube.com/c/CortesdoFlow"
#Cortes Podcast
canais[1] = "https://www.youtube.com/c/CortesPodcast"
#Cortes do Inteligencia
canais[2] = "https://www.youtube.com/c/CortesdoIntelig%C3%AAncia"
#Cortes mais que 8 minutos
canais[3] = "https://www.youtube.com/c/CortesMaisque8MinutosOFICIAL"
#Cortes do Venus
canais[4] = "https://www.youtube.com/channel/UCOL_QmVnNQ5bKeS4zgqV81g"
#Master cortes Podcast
canais[5] = "https://www.youtube.com/c/TimesCortesPodcast/videos"
#PodPah Melhores Cortes
canais[6] = "https://www.youtube.com/c/PodpahMelhoresMomentosyt/videos"
#Cortes do PodCast
canais[7] = "https://www.youtube.com/c/podcatscortes"
# Ticaracacast Cortes
canais[8] = "https://www.youtube.com/c/TicaracaticastCortes"
#Canal do MHM
canais[9] = "https://www.youtube.com/c/CortesdoMHM"
#Cortes do Edward
canais[10] = "https://www.youtube.com/c/CortesdoEdward/videos"
#PodCortes
canais[11] = "https://www.youtube.com/c/PodCortes1/videos"
#Cortes do Podihhcast
canais[12] = "https://www.youtube.com/channel/UCZc2umMjCiT_zA3pVh-XtCQ"
#Cortes & Cortes
canais[13] = "https://www.youtube.com/channel/UCcPfI4LZ9_j5GVFunR6U_kA"

def gerar_video():
    #número aleatório que sera usado para escolher o canal
    aleatorio = random.randint(0,13)
    #escolhe um canal para consumirmos o conteudo
    c = Channel(canais[aleatorio])
    #print("Canal :", canais[aleatorio], "\n")

    #lista os 20 primeiros videos do canal
    aleatorio = random.randint(0,19)

    #seleciona aleatoriamente qual video devera ser baixado
    video = YouTube(c.video_urls[aleatorio])

    #video.streams.filter(file_extension='mp4')
    #Seleciona a Stream correta para fazer o downlaod do video
    stream = video.streams.get_by_itag(18)

    #faz o download do video e grava o local dele
    local = stream.download()
    video = VideoFileClip(local)

    i = 0

    if(video.duration > 1500):
        gerar_video()
    else:
        todasPartes = []
        while video.duration > 60:
            videoAux = video.subclip(0, 60)
            video = video.subclip(t_start=60, t_end= video.duration)
            titulo = 'C:/Users/joao_/OneDrive/Desktop/postar_tik_tok' + '/parte' + str(i) + '.mp4'
            videoAux.write_videofile(titulo)
            todasPartes.append(titulo)
            i = i + 1
    i = i + 1
    titulo = 'C:/Users/joao_/OneDrive/Desktop/postar_tik_tok' + '/parte' + str(i) + '.mp4'
    todasPartes.append(titulo)
    video.write_videofile(titulo)
    os.remove(local)
    return todasPartes
