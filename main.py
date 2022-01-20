from graphics import *
import random

def main():
    win = GraphWin("Runner", 1000, 500, autoflush=False)
    #verifica teclas
    key = win.checkKey()
    podeAcontecerSoUmaVez=1
    namorada=1
    carregar=0
    comecarJogo=0
    carregando_cont=0
    altura=0
    podeJogar=0
    jogoPausado=0
    jogoPausado_cont=0
    carregarArquivos=1
    playerVivo=0
    cachorroCriado=0
    cachorroCriado2=0
    carroPode=0
    skateCriado=0
    layoutCriado=0
    lixoCriado=0
    distanciaCriada=0
    podeSangue=0
    sangue_cont=0
    sangueDesenhado=0
    playerMorto_cont=0
    playerVida=3
    podeTrocarVida=10
    playerDesbug=0
    texto1Pode=1
    escola=0
    posicao=0
    cenarioLocal=0
    posicaoPlayer=0
    posicaoPlayerEsq=0
    #Segunda Parte
    inverterPlayer_cont=0
    inverterPlayer=0
    playerInvertido=0
    recomecar=0
    skate_pos=0
    skate_posDir=0
    paralax = Image(Point(1000, 250), "paralax.png")
    paralax.draw(win)
    cenario = Image(Point(15000, 250), "cenario.png")
    cenario.draw(win)

    menuInicial=Image(Point(500,250), "runner.png")
    menuInicial.draw(win)
    menuInicialOff=0

    player = Image(Point(100, 360), "player.png")
    player.draw(win)

    comecar = Image(Point(500, 250), "começar.png")
    comecar.draw(win)
    comecar_cont=0
    comecarOff = 0


    while key != "Escape":
        key = win.checkKey()


        if playerVivo==1:
            update(42)
        else:
            update(30)

        if comecarOff==0 and podeJogar==0:
            if comecar_cont<30:
                comecar_cont+=1

            if comecar_cont==15:
                comecar.undraw()

            if comecar_cont==30:
                comecar = Image(Point(500, 250), "começar.png")
                comecar.draw(win)
                comecar_cont = 0

        # SEGUNDA PARTE
        if key=="Return" and inverterPlayer==1 and escola==1:
            recomecar = 1


        if cenarioLocal <= 20000 and playerInvertido==1 and namorada==1:
            podeJogar = 0
            texto4 = Text(Point(500, 200), "Você chegou na casa da sua namorada! Pressione ENTER")
            texto4.setSize(20)
            texto4.setFill(color="Red")
            texto4.draw(win)
            recomecar=2
            namorada=0

        if key=="Return" and recomecar==2:
            texto4.undraw()
            podeJogar=1
            recomecar=0


        if recomecar==1:
            escola = 0
            podeJogar=1
            playerVida = 3
            podeTrocarVida = 2
            cenarioMovimento = 1
            paralax.undraw()
            paralax = Image(Point(0, 250), "paralaxNoite.png")
            cenario.undraw()
            paralax.draw(win)
            cenario = Image(Point(-11500, 250), "cenario.png")
            cenario.draw(win)

            layout.undraw()
            layout = Image(Point(500, 250), "layout3.png")
            layout.draw(win)

            texto2.undraw()
            texto3.undraw()

            lixo_cont = 0
            player.undraw()
            playerInvertido = 1
            player_cont = 0
            recomecar=0


        # LAYOUT
        if playerVida == 2 and podeTrocarVida == 2:
            layout.undraw()
            layout = Image(Point(500, 250), "layout2.png")
            layout.draw(win)
            podeTrocarVida = 1

        if playerVida == 1 and podeTrocarVida == 1:
            layout.undraw()
            layout = Image(Point(500, 250), "layout1.png")
            layout.draw(win)
            podeTrocarVida = 0

        if podeSangue == 1:
            sangue_cont += 1
            if sangueDesenhado == 0:
                sangue = Image(Point(500, 250), "sangue.png")
                sangue.draw(win)
                sangueDesenhado = 1

            if sangue_cont == 5:
                sangue.undraw()
                sangueDesenhado = 0
                sangue_cont = 0
                podeSangue = 0

        # SISTEMA DE MORTE
        if playerVida == 0:
            if podeTrocarVida == 0:
                # LAYOUT MORTO
                layout.undraw()
                layout = Image(Point(500, 250), "morto.png")
                layout.draw(win)
                voceMorreu = Text(Point(500, 250), "VOCÊ MORREU!")
                voceMorreu.setSize(20)
                voceMorreu.setFill(color="Red")
                voceMorreu.draw(win)
                podeTrocarVida=2
            # PLAYER MORTO
            if playerMorto_cont < 10 and playerDesbug<=1:
                player.undraw()
                playerCentro = player.getAnchor()
                if playerInvertido==0:
                    player = Image(playerCentro, "playerMorto.png")
                if playerInvertido==1:
                    player = Image(playerCentro, "playerMortoInvertido.png")
                player.draw(win)
                playerMorto_cont = playerMorto_cont + 1

            if playerMorto_cont >= 10 and playerDesbug<=1:
                playerMorto_cont = 0
                playerDesbug+=1

            playerVivo = 0
            posicaoPlayer = 5000
            posicaoPlayerEsq = 5000
            skate_cont += 1

        #SISTEMA DE RESTART
        if (playerVivo == 0 and key=="Return") or (key=="r" and carregarArquivos==0) or (carregarArquivos==1 and key=="Return"):
            if menuInicialOff==0 and comecarOff==0:
                menuInicial.undraw()
                menuInicialOff=1
                comecar.undraw()
                comecarOff==1
                comecar_cont=31

            podeJogar=0
            carregando = Image(Point(500, 250), "carregando.png")
            carregando.draw(win)
            carregar=1

        if carregar==1:
            if playerVivo==0:
                update(30)
            carregando_cont+=1
            if carregando_cont>10:
                comecarJogo = 1

        if comecarJogo==1:
            # JOGO QUE VAI SER REINICIADO

            jogoPausado = 0
            jogoPausado_cont = 0
            podeJogar = 1


            if lixoCriado==1:
                lixo.undraw()

            # CARRO
            if carroPode==1:
                carro.undraw()
            carro = Image(Point(1500, 587), "carro.png")
            carro.draw(win)
            carroPode = 1
            carro_cont = 0

            # CENARIO
            paralax.undraw()
            cenario.undraw()
            paralax = Image(Point(1000, 250), "paralax.png")
            cenario = Image(Point(15000, 250), "cenario.png")
            cenarioLocal = 0
            paralax.draw(win)
            cenario.draw(win)

            cenarioMovimento = 1

            # ANIMAÇÃO CACHORRO
            if cachorroCriado==1:
                imagem.undraw()
            cachorro = 0            #contador do cachorro
            imagem = Image(Point(400 + 3000, 380), "cachorro1.png")
            centro = imagem.getAnchor()
            localCachorro = 0
            imagem.draw(win)
            cachorroPosEsq = 350 + 3000
            cachorroPosDir = 450 + 3000
            cachorroCriado=1

            # ANIMAÇÃO CACHORRO 2
            if cachorroCriado2==1:
                cachorro2.undraw()
            cachorro_cont2 = 0            #contador do cachorro
            cachorro2 = Image(Point(400 - 2500, 350), "cachorroinvertido1.png")
            cachorro2Centro = cachorro2.getAnchor()
            localCachorro2 = 0
            cachorro2.draw(win)
            cachorroPosEsq2 = 370 - 2500
            cachorroPosDir2 = 440 - 2500
            cachorroCriado2=1

            # SKATE
            if skateCriado==1:
                skate.undraw()
            skate = Image(Point(500 + 1000, 370), "skate.png")
            skateCentro = skate.getAnchor()
            skate.draw(win)
            skate_cont = 0
            skateMove = 1
            skate_pos = 465 + 1000
            skate_posDir = 550 + 1000
            desenharSkatistaMorto = 1
            skateCriado = 1

            # PLAYER
            playerInvertido=0
            playerDesbug=0
            playerMorto_cont=0
            podeTrocarVida = 2
            playerVida = 3
            playerVivo = 1
            delay_para_pular = 0
            limitadorDeAltura_cont = 0
            limitadorDeAltura = 0
            altura = 0
            player_cont = 0

            player.undraw()
            player = Image(Point(200, 390), "sprite1.png")
            playerCentro = player.getAnchor()
            player.draw(win)
            posicao = 0
            posicaoPlayer = 264
            posicaoPlayerEsq = 133

            # layout
            if layoutCriado==1:
                layout.undraw()
            layout = Image(Point(500, 250), "layout3.png")
            layout.draw(win)
            layoutCriado=1

            # LIXO
            lixo = Image(Point(100+600, 385), "lixo.png")
            lixoPosicaoEsq = 98 + 600
            lixoPosicaoDir = 123 + 600

            lixo.draw(win)
            lixo_cont = 0
            lixoMove = 1
            lixoCriado=1

            #Para evitar bug
            carregando.undraw()
            carregando_cont=0
            carregar=0          #looping para aparecer tela de carregamento
            carregarArquivos=0
            comecarJogo=0


        #SISTEMA DE PAUSE
        if (jogoPausado == 1 or jogoPausado==0) and jogoPausado_cont<20:
            jogoPausado_cont += 1

        if key == "p" or key=="P":
            if jogoPausado == 1:
                if jogoPausado_cont>10:
                    podeJogar = 1
                    jogoPausado=0
                    jogoPausado_cont = 0

            if jogoPausado == 0:
                if jogoPausado_cont>10:
                    podeJogar=0
                    jogoPausado=1
                    jogoPausado_cont=0


        #VARIAVEL PARA PODER PAUSAR
        if podeJogar==1:
            #CÓDIGOS ABAIXO PARA FUNCIONAR A VARIÁVEL DE PAUSE

            # SISTEMA DE COLISÃO
            # COLISAO ENTRE PLAYER E LIXO
            if ((posicaoPlayerEsq <= lixoPosicaoEsq and lixoPosicaoEsq <= posicaoPlayer) or (
                    posicaoPlayerEsq <= lixoPosicaoDir and lixoPosicaoDir <= posicaoPlayer)) and posicao == 1 and altura < 10:
                playerVida = playerVida - 1
                lixoMove = 0
                podeSangue = 1
                lixoPosicaoDir = 100000
                lixoPosicaoEsq = 100000


                # COLISAO ENTRE PLAYER E CACHORRO
            if ((posicaoPlayerEsq <= cachorroPosEsq and cachorroPosEsq <= posicaoPlayer) or (
                    posicaoPlayerEsq <= cachorroPosDir and cachorroPosDir <= posicaoPlayer)) and posicao == 0 and altura < 10:
                playerVida = playerVida - 1
                podeSangue = 1
                cachorroPosDir = 100000
                cachorroPosEsq = 100000


                # COLISAO ENTRE PLAYER E CACHORRO 2
            if ((posicaoPlayerEsq <= cachorroPosEsq2 and cachorroPosEsq2 <= posicaoPlayer) or (
                    posicaoPlayerEsq <= cachorroPosDir2 and cachorroPosDir2 <= posicaoPlayer)) and posicao == 1 and altura < 10:
                playerVida = playerVida - 1
                podeSangue = 1
                cachorroPosDir2 = 100000
                cachorroPosEsq2 = 100000



            # SISTEMA DE COLISÃO ENTRE JOGADOR E SKATISTA
            if ((posicaoPlayerEsq <= skate_pos and skate_pos <= posicaoPlayer) or (
                    posicaoPlayerEsq <= skate_posDir and skate_posDir <= posicaoPlayer)) and posicao == 0:
                playerVida = playerVida - 1
                skateMove = 0
                podeSangue = 1
                skate_pos = 100000
                skate_posDir = 100000

            # lixo
            if lixoMove == 1 and playerVivo == 1:
                if playerInvertido==0:
                    lixo.move(-13, 0)
                    lixoPosicaoDir = lixoPosicaoDir - 13
                    lixoPosicaoEsq = lixoPosicaoEsq - 13
                if playerInvertido==1:
                    lixo.move(13,0)
                    lixoPosicaoDir = lixoPosicaoDir + 13
                    lixoPosicaoEsq = lixoPosicaoEsq + 13

                lixo_cont += 1

                if lixo_cont > 400:
                    lixo.undraw()
                    if playerInvertido==0:
                        lixo = Image(Point(100+1000, 385), "lixo.png")
                        lixoPosicaoEsq = 98 + 1000
                        lixoPosicaoDir = 123 + 1000
                    if playerInvertido==1:
                        lixo = Image(Point(100-1500, 385), "lixo.png")
                        lixoPosicaoEsq = 98 - 1500
                        lixoPosicaoDir = 123 - 1500
                    lixo.draw(win)
                    lixo_cont = 0


            if lixoMove == 0:
                lixo.undraw()
                if playerVivo == 1:
                    if playerInvertido==0:
                        lixo.move(-13, 0)
                    if playerInvertido==1:
                        lixo.move(13, 0)
                lixoCentro = lixo.getAnchor()
                lixo = Image(lixoCentro, "lixoCaido.png")
                lixo.draw(win)
                lixo_cont += 1

                if lixo_cont > 150:
                    lixoMove = 1

            # ANIMAÇÃO CACHORRO 2
            if localCachorro2 > 300:
                cachorro2.undraw()
                cachorro2 = Image(Point(400 - 1000, 350), "cachorroinvertido1.png")
                cachorro2Centro = cachorro2.getAnchor()
                localCachorro2 = 0
                cachorro_cont2 = 0
                cachorroPosEsq2 = 370 - 1000
                cachorroPosDir2 = 440 - 1000

            else:
                if cachorro_cont2 < 3:
                    cachorro2.move(17, 0)
                    cachorro2Centro = cachorro2.getAnchor()
                    cachorro2.undraw()
                    cachorro2 = Image(cachorro2Centro, "cachorroinvertido2.png")
                    cachorro2.draw(win)
                    cachorro_cont2 += 1
                    localCachorro2 += 1
                    cachorroPosDir2 = cachorroPosDir2 + 17
                    cachorroPosEsq2 = cachorroPosEsq2 + 17

                if cachorro_cont2 >= 3 and cachorro_cont2 < 6:
                    cachorro2.move(17, 0)
                    cachorro2Centro = cachorro2.getAnchor()
                    cachorro2.undraw()
                    cachorro2 = Image(cachorro2Centro, "cachorroinvertido3.png")
                    cachorro2.draw(win)
                    cachorro_cont2 += 1
                    localCachorro2 += 1
                    cachorroPosDir2 = cachorroPosDir2 + 17
                    cachorroPosEsq2 = cachorroPosEsq2 + 17

                if cachorro_cont2 == 6:
                    cachorro_cont2 = 0


        #ANIMAÇÃO DO JOGADOR----------
            #SISTEMA DE PULO
            if delay_para_pular>0:
                limitadorDeAltura = 1

            if limitadorDeAltura == 1:
                delay_para_pular+=1

            if delay_para_pular>20:
                limitadorDeAltura=0
                delay_para_pular=0

            if altura>0:
                player.move(0, 10)
                playerCentro = player.getAnchor()
                player.undraw()
                if playerInvertido==0:
                    player = Image(playerCentro , "pulando.png")
                if playerInvertido==1:
                    player = Image(playerCentro, "pulandoInvertido.png")
                player.draw(win)
                altura -= 10

            elif limitadorDeAltura==0 and key == "space" and playerVivo==1 and cenarioLocal>150 and cenarioLocal<26350:
                player.move(0, -150)
                playerCentro = player.getAnchor()
                player.undraw()
                if playerInvertido==0:
                    player = Image(playerCentro , "pulando.png")
                if playerInvertido==1:
                    player = Image(playerCentro, "pulandoInvertido.png")

                player.draw(win)
                altura += 150
                delay_para_pular += 1

            #VAI PRA DIREITA
            elif (key == "Right" or key == "d" or key == "D") and posicaoPlayer<1000:
                if playerVivo==1:
                    if player_cont < 3:
                        player.move(4, 0)
                        playerCentro = player.getAnchor()
                        player.undraw()
                        if playerInvertido == 0:
                            player = Image(playerCentro, "sprite1.png")
                        if playerInvertido == 1:
                            player = Image(playerCentro, "sprite1invertido.png")
                        player.draw(win)
                        posicaoPlayerEsq = posicaoPlayerEsq + 4
                        posicaoPlayer = posicaoPlayer + 4
                        cenarioLocal = cenarioLocal + 4
                        player_cont+=1


                    if player_cont >= 3 and player_cont < 6:
                        player.move(4, 0)
                        playerCentro = player.getAnchor()
                        player.undraw()
                        if playerInvertido == 0:
                            player = Image(playerCentro, "sprite2.png")
                        if playerInvertido == 1:
                            player = Image(playerCentro, "sprite2invertido.png")
                        player.draw(win)
                        posicaoPlayerEsq = posicaoPlayerEsq + 4
                        posicaoPlayer = posicaoPlayer + 4
                        cenarioLocal = cenarioLocal + 4
                        player_cont += 1


                    if player_cont >= 6 and player_cont < 9:
                        player.move(4, 0)
                        playerCentro = player.getAnchor()
                        player.undraw()
                        if playerInvertido == 0:
                            player = Image(playerCentro, "sprite3.png")
                        if playerInvertido == 1:
                            player = Image(playerCentro, "sprite3invertido.png")

                        player.draw(win)
                        posicaoPlayerEsq = posicaoPlayerEsq + 4
                        posicaoPlayer = posicaoPlayer + 4
                        cenarioLocal = cenarioLocal + 4
                        player_cont += 1


                    if player_cont >= 9 and player_cont < 12:
                        player.move(4, 0)
                        playerCentro = player.getAnchor()
                        player.undraw()
                        if playerInvertido==0:
                            player = Image(playerCentro , "sprite4.png")
                        if playerInvertido==1:
                            player = Image(playerCentro, "sprite4invertido.png")
                        player.draw(win)
                        posicaoPlayerEsq = posicaoPlayerEsq + 4
                        posicaoPlayer = posicaoPlayer + 4
                        cenarioLocal = cenarioLocal + 4
                        player_cont += 1

                    if player_cont == 12:
                        player_cont = 0

            elif (key == "Left" or key == "a" or key == "A") and posicaoPlayerEsq>0:
                if playerVivo == 1:
                    if player_cont < 3:
                        player.move(-4, 0)
                        playerCentro = player.getAnchor()
                        player.undraw()
                        if playerInvertido == 0:
                            player = Image(playerCentro, "sprite1.png")
                        if playerInvertido == 1:
                            player = Image(playerCentro, "sprite1invertido.png")
                        player.draw(win)
                        posicaoPlayer = posicaoPlayer - 4
                        posicaoPlayerEsq = posicaoPlayerEsq - 4
                        cenarioLocal = cenarioLocal - 4
                        player_cont += 1

                    if player_cont >= 3 and player_cont < 6:
                        player.move(-4, 0)
                        playerCentro = player.getAnchor()
                        player.undraw()
                        if playerInvertido == 0:
                            player = Image(playerCentro, "sprite2.png")
                        if playerInvertido == 1:
                            player = Image(playerCentro, "sprite2invertido.png")
                        player.draw(win)
                        posicaoPlayer = posicaoPlayer - 4
                        posicaoPlayerEsq = posicaoPlayerEsq - 4
                        cenarioLocal = cenarioLocal - 4
                        player_cont += 1


                    if player_cont >= 6 and player_cont < 9:
                        player.move(-4, 0)
                        playerCentro = player.getAnchor()
                        player.undraw()
                        if playerInvertido == 0:
                            player = Image(playerCentro, "sprite3.png")
                        if playerInvertido == 1:
                            player = Image(playerCentro, "sprite3invertido.png")
                        player.draw(win)
                        posicaoPlayer = posicaoPlayer - 4
                        posicaoPlayerEsq = posicaoPlayerEsq - 4
                        cenarioLocal = cenarioLocal - 4
                        player_cont += 1

                    if player_cont >= 9 and player_cont < 12:
                        player.move(-4, 0)
                        playerCentro = player.getAnchor()
                        player.undraw()
                        if playerInvertido == 0:
                            player = Image(playerCentro, "sprite4.png")
                        if playerInvertido == 1:
                            player = Image(playerCentro, "sprite4invertido.png")
                        player.draw(win)
                        posicaoPlayer = posicaoPlayer - 4
                        posicaoPlayerEsq = posicaoPlayerEsq - 4
                        cenarioLocal=cenarioLocal - 4
                        player_cont += 1

                    if player_cont == 12:
                        player_cont = 0

            elif (key == "w" or key == "W" or key == "Up") and posicao==0 and playerVivo==1:
                player.move(-15,-30)
                posicao+=1
                posicaoPlayer=posicaoPlayer-15
                posicaoPlayerEsq=posicaoPlayerEsq-15

            elif (key == "s" or key == "S" or key == "Down") and posicao==1 and playerVivo ==1:
                player.move(15,30)
                posicao-=1
                posicaoPlayer=posicaoPlayer+15
                posicaoPlayerEsq=posicaoPlayerEsq+15

            else:
                if playerVivo==1:
                    if player_cont < 3:
                        playerCentro = player.getAnchor()
                        player.undraw()
                        if playerInvertido == 0:
                            player = Image(playerCentro, "sprite1.png")
                        if playerInvertido == 1:
                            player = Image(playerCentro, "sprite1invertido.png")
                        player.draw(win)
                        player_cont+=1

                    if player_cont >= 3 and player_cont < 6:
                        playerCentro = player.getAnchor()
                        player.undraw()
                        if playerInvertido == 0:
                            player = Image(playerCentro, "sprite2.png")
                        if playerInvertido == 1:
                            player = Image(playerCentro, "sprite2invertido.png")
                        player.draw(win)
                        player_cont += 1

                    if player_cont >= 6 and player_cont < 9:
                        playerCentro = player.getAnchor()
                        player.undraw()
                        if playerInvertido == 0:
                            player = Image(playerCentro, "sprite3.png")
                        if playerInvertido == 1:
                            player = Image(playerCentro, "sprite3invertido.png")
                        player.draw(win)
                        player_cont += 1

                    if player_cont >= 9 and player_cont < 12:
                        playerCentro = player.getAnchor()
                        player.undraw()
                        if playerInvertido == 0:
                            player = Image(playerCentro, "sprite4.png")
                        if playerInvertido == 1:
                            player = Image(playerCentro, "sprite4invertido.png")
                        player.draw(win)
                        player_cont += 1

                    if player_cont == 12:
                        player_cont = 0

            #cenario
            if cenarioMovimento==1 and playerVivo==1 and playerInvertido==0 and cenarioLocal<=26500:
                cenario.move(-13,0)
                paralax.move(-0.4,0)
                cenarioLocal=cenarioLocal+13

            if cenarioMovimento==1 and playerVivo==1 and playerInvertido==1 and cenarioLocal>100:
                cenario.move(13, 0)
                paralax.move(0.4, 0)
                cenarioLocal = cenarioLocal - 13

            if cenarioLocal>=26500 and playerInvertido==0:
                podeJogar=0
                cenarioMovimento=0
                player.undraw()
                player = Image(playerCentro, "player.png")
                player.draw(win)
                texto2 = Text(Point(500, 160), "Você chegou na escola!")
                texto2.setSize(25)
                texto2.setFill(color="Red")
                texto2.draw(win)

                texto3 = Text(Point(500, 190), "Vá para a casa da sua namorada! Pressione Enter")
                texto3.setSize(25)
                texto3.setFill(color="Red")
                texto3.draw(win)
                escola=1
                inverterPlayer=1


            if cenarioLocal<150 and playerInvertido==1:
                podeJogar=0
                cenarioMovimento=0
                player.undraw()
                player = Image(playerCentro, "player.png")
                player.draw(win)
                texto2 = Text(Point(500, 160), "Parabens! Você chegou em casa, fim de jogo. Pressione R ou ESC.")
                texto2.setSize(25)
                texto2.setFill(color="Red")
                texto2.draw(win)


            if texto1Pode==1:
                if cenarioLocal>100 and playerInvertido==0 and cenarioLocal<110:
                    texto1 = Text(Point(500, 160), "Chegue na escola")
                    texto1.setSize(25)
                    texto1.setFill(color="Red")
                    texto1.draw(win)
                if cenarioLocal>300:
                    texto1.undraw()
                    texto1Pode=0

            #skate
            if skateMove==1:
                if skate_cont>=0:
                    skate.undraw()
                    skate.move(-32,0)
                    skateCentro = skate.getAnchor()
                    skate = Image(skateCentro, "skate.png")
                    skate.draw(win)
                    skate_pos=skate_pos-32
                    skate_posDir = skate_posDir-32
                    skate_cont += 1

                if skate_cont>100:
                    skate.undraw()
                    skate = Image(Point(500+1000, 370), "skate.png")
                    skate.draw(win)
                    skate_cont=0
                    skate_pos = 465 + 1000
                    skate_posDir = 550 + 1000

            if skateMove==0:
                if skate_cont>=0:
                    skate.undraw()
                    if playerVivo==1:
                        if playerInvertido == 0:
                            skate.move(-13, 0)
                        if playerInvertido == 1:
                            skate.move(13, 0)

                    if playerVivo==0:
                        if desenharSkatistaMorto==1:
                            skate2Centro=skate.getAnchor()
                            skate2 = Image(skate2Centro, "skatecaido.png")
                            skate2.draw(win)
                            desenharSkatistaMorto=0
                    skateCentro = skate.getAnchor()
                    skate = Image(skateCentro, "skatecaido.png")
                    skate.draw(win)
                    skate_cont += 1
                if skate_cont>200:
                    skateMove=1


            #ANIMAÇÃO DO CACHORRO
            #se o cachorro tiver longe, spawna ele de novo
            if localCachorro >250:
                imagem.undraw()
                imagem = Image(Point(400+1000, 380), "cachorro1.png")
                centro = imagem.getAnchor()
                localCachorro=0
                cachorro = 0
                cachorroPosEsq = 350 + 1000
                cachorroPosDir = 450 + 1000

            else:
                if cachorro<3:
                    imagem.move(-20,0)
                    centro = imagem.getAnchor()
                    imagem.undraw()
                    imagem = Image(centro, "cachorro2.png")
                    imagem.draw(win)
                    cachorro += 1
                    localCachorro+=1
                    cachorroPosDir=cachorroPosDir-20
                    cachorroPosEsq=cachorroPosEsq-20


                if cachorro>=3 and cachorro <6:
                    imagem.move(-20, 0)
                    centro = imagem.getAnchor()
                    imagem.undraw()
                    imagem = Image(centro, "cachorro3.png")
                    imagem.draw(win)
                    cachorro += 1
                    localCachorro += 1
                    cachorroPosDir=cachorroPosDir-20
                    cachorroPosEsq=cachorroPosEsq-20

                if cachorro==6:
                    cachorro=0

            #Animação do carro
            if carroPode==1:
                carro.move(-50,0)
                carro_cont += 1
                if carro_cont>400:
                    carro.undraw()
                    carro = Image(Point(1500, 587), "carro.png")
                    carro.draw(win)
                    carro_cont=0


    win.close()

main()