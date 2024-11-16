import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "La historia de la Informática"
    page.bgcolor = "blue"
    page.window_width = 650
    page.window_height = 800
    
    image_width_Portada = 800
    image_height_Portada = 400
    
    img_height = 100
    img_width = 100
    border_radius = 25  # Ajusta el valor para el radio del borde

    # Audios Padres de la informática
    intro = ft.Audio(src="Intro.mp3", volume=1, balance=0)
    page.overlay.append(intro)
    
    Pascal = ft.Audio(src="Pascal.mp3", volume=1, balance=0)
    page.overlay.append(Pascal)
    
    Leibniz = ft.Audio(src="Leibniz.mp3", volume=1, balance=0)
    page.overlay.append(Leibniz)
    
    Babbage = ft.Audio(src="Babbage.mp3", volume=1, balance=0)
    page.overlay.append(Babbage)
    
    Lovelace = ft.Audio(src="Lovelace.mp3", volume=1, balance=0) 
    page.overlay.append(Lovelace)
    
    Hollerith = ft.Audio(src="Hollerith.mp3", volume=1, balance=0)
    page.overlay.append(Hollerith)
    
    Turing = ft.Audio(src="Turing.mp3", volume=1, balance=0)
    page.overlay.append(Turing)
    
    Neumann = ft.Audio(src="Neumann.mp3", volume=1, balance=0)
    page.overlay.append(Neumann)
    
    Shannon = ft.Audio(src="shannon.mp3", volume=1, balance=0)
    page.overlay.append(Shannon)
    
    Hopper = ft.Audio(src="Hopper.mp3", volume=1, balance=0)
    page.overlay.append(Hopper)
    
    McCarthy = ft.Audio(src="McCarthy.mp3", volume=1, balance=0)
    page.overlay.append(McCarthy)
    
    Berners = ft.Audio(src="Berners.mp3", volume=1, balance=0)
    page.overlay.append(Berners)
    
    Ritchie = ft.Audio(src="Ritchie.mp3", volume=1, balance=0)
    page.overlay.append(Ritchie)
    
    Thompson = ft.Audio(src="Thompson.mp3", volume=1, balance=0)
    page.overlay.append(Thompson)
    
    Gosling = ft.Audio(src="Gosling.mp3", volume=1, balance=0)
    page.overlay.append(Gosling)
    
    Jobs = ft.Audio(src="Jobs.mp3", volume=1, balance=0)
    page.overlay.append(Jobs)
    
    Wozniak= ft.Audio(src="Wozniak.mp3", volume=1, balance=0)
    page.overlay.append(Wozniak)
    
    Gates = ft.Audio(src="Gates.mp3", volume=1, balance=0)
    page.overlay.append(Gates)
    
    Zuckerberg = ft.Audio(src="Zuckerberg.mp3", volume=1, balance=0)
    page.overlay.append(Zuckerberg)
    
    Pages = ft.Audio(src="Pages.mp3", volume=1, balance=0)
    page.overlay.append(Pages)
    
    Brin = ft.Audio(src="Brin.mp3", volume=1, balance=0)
    page.overlay.append(Brin)
    
    c = ft.Audio(src="c.mp3", volume=1, balance=0)
    page.overlay.append(c)
    
    cmas = ft.Audio(src="c++.mp3",volume=1, balance=0)
    page.overlay.append(cmas)
    
    go=  ft.Audio(src="go.mp3",volume=1,balance=0)
    page.overlay.append(go)
    
    java= ft.Audio(src="java.mp3",volume=1,balance=0)
    page.overlay.append(java)
    
    javascrip=ft.Audio(src="javascrip.mp3",volume=1,balance=0)
    page.overlay.append(javascrip)
    
    kotin=ft.Audio(src="javascrip.mp3",volume=1,balance=0)
    page.overlay.append(kotin)
    
    php=ft.Audio(src="php.mp3", volume=1, balance=0)
    page.overlay.append(php)
    
    python=ft.Audio(src="python.mp3", volume=1, balance=0)
    page.overlay.append(python)
    
    r=ft.Audio(src="r.mp3", volume=1,balance=0)
    page.overlay.append(r)
    
    facebook=ft.Audio(src="facebook.mp3", volume=1,balance=0)
    page.overlay.append(facebook)
    
    instagram=ft.Audio(src="instagram.mp3",volume=1,balance=0)
    page.overlay.append(instagram)
    
    twiter=ft.Audio(src="twiter.mp3",volume=1,balance=0)
    page.overlay.append(twiter)
    
    tiktok=ft.Audio(src="tiktok.mp3",volume=1,balance=0)
    page.overlay.append(tiktok)
    
    linkedin=ft.Audio(src="linkedin.mp3",volume=1,balance=0)
    page.overlay.append(linkedin)
    
    snapchat=ft.Audio(src="snapchat.mp3",volume=1,balance=0)
    page.overlay.append(snapchat)
    
    youtube=ft.Audio(src="youtube.mp3",volume=1,balance=0)
    page.overlay.append(youtube)
    
    piterest=ft.Audio(src="piterest.mp3",volume=1,balance=0)
    page.overlay.append(piterest)
    
    whatsapp=ft.Audio(src="whatsapp.mp3",volume=1,balance=0)
    page.overlay.append(whatsapp)
    
    teletrabajo=ft.Audio(src="teletrabajo.mp3",volume=1,balance=0)
    page.overlay.append(teletrabajo)
    
    ciberseguridad=ft.Audio(src="ciberseguridad.mp3",volume=1,balance=0)
    page.overlay.append(ciberseguridad)
    
    nube=ft.Audio(src="nube.mp3",volume=1,balance=0)
    page.overlay.append(nube)
    
    educacion=ft.Audio(src="educacion.mp3",volume=1,balance=0)
    page.overlay.append(educacion)
    
    telemedicina=ft.Audio(src="telemedicina.mp3",volume=1,balance=0)
    page.overlay.append(telemedicina)
    
    comercio=ft.Audio(src="comercio.mp3",volume=1,balance=0)
    page.overlay.append(comercio)
    
    redes=ft.Audio(src="redes.mp3",volume=1,balance=0)
    page.overlay.append(redes)
    
    trabajoremoto=ft.Audio(src="trabajoremoto.mp3",volume=1,balance=0)
    page.overlay.append(trabajoremoto)
    
    rastreo=ft.Audio(src="rastreo.mp3",volume=1,balance=0)
    page.overlay.append(rastreo)
    
    ia2=ft.Audio(src="ia2.mp3",volume=1,balance=0)
    page.overlay.append(ia2)

    cuantica=ft.Audio(src="cuantica.mp3",volume=1,balance=0)
    page.overlay.append(cuantica)

    blockchain=ft.Audio(src="blockchain.mp3",volume=1,balance=0)
    page.overlay.append(blockchain)

    g=ft.Audio(src="5g.mp3",volume=1,balance=0)
    page.overlay.append(g)

    vr=ft.Audio(src="vr.mp3",volume=1,balance=0)
    page.overlay.append(vr)

    internet=ft.Audio(src="internet.mp3",volume=1,balance=0)
    page.overlay.append(internet)

    impresion=ft.Audio(src="impresion.mp3",volume=1,balance=0)
    page.overlay.append(impresion)

    robots=ft.Audio(src="robots.mp3",volume=1,balance=0)
    page.overlay.append(robots)

    energia=ft.Audio(src="energia.mp3",volume=1,balance=0)
    page.overlay.append(energia)

    def StopAll():
        intro.pause()
        Pascal.pause()
        Leibniz.pause()
        Babbage.pause()
        Lovelace.pause()
        Hollerith.pause()
        Turing.pause()
        Neumann.pause()
        Shannon.pause()
        Hopper.pause()
        McCarthy.pause()
        Berners.pause()
        Ritchie.pause()
        Thompson.pause()
        Gosling.pause()
        Jobs.pause()
        Wozniak.pause()
        Gates.pause()
        Zuckerberg.pause()
        Pages.pause()
        Brin.pause()
        c.pause()
        cmas.pause()
        go.pause()
        java.pause()
        javascrip.pause()
        kotin.pause()
        php.pause()
        python.pause()
        r.pause()
        facebook.pause()
        instagram.pause()
        twiter.pause()
        tiktok.pause()
        linkedin.pause()
        snapchat.pause()
        youtube.pause()
        piterest.pause()
        whatsapp.pause()
        teletrabajo.pause()
        ciberseguridad.pause()
        nube.pause()
        educacion.pause()
        telemedicina.pause()
        comercio.pause()
        redes.pause()
        trabajoremoto.pause()
        rastreo.pause()
        ia2.pause()
        cuantica.pause()
        blockchain.pause()
        g.pause()
        vr.pause()
        internet.pause()
        impresion.pause()
        robots.pause()
        energia.pause()
    
    def play_intro(e):
        StopAll()
        intro.play()
        
    def play_pascal(e):
        StopAll()
        Pascal.play()
        
    def play_leibniz(e):
        StopAll()
        Leibniz.play()
        
    def play_babbage(e):
        StopAll()
        Babbage.play()
        
    def play_lovelace(e):    
        StopAll()
        Lovelace.play()
        
    def play_hollerith(e):
        StopAll()
        Hollerith.play()
        
    def play_turing(e):
        StopAll()
        Turing.play()
    
    def play_neumann(e):
        StopAll()
        Neumann.play()
        
    def play_shannon(e):
        StopAll()
        Shannon.play()
    
    def play_hopper(e):
        StopAll()
        Hopper.play()
    
    def play_mccarthy(e):
        StopAll()
        McCarthy.play()
    
    def play_berners(e):
        StopAll()
        Berners.play()
    
    def play_ritchie(e):
        StopAll()
        Ritchie.play()
        
    def play_thompson(e):
        StopAll()
        Thompson.play()
        
    def play_gosling(e):
        StopAll()
        Gosling.play()
        
    def play_jobs(e):
        StopAll()
        Jobs.play()
        
    def play_wozniak(e):
        StopAll()
        Wozniak.play()
        
    def play_gates(e):
        StopAll()
        Gates.play()
    
    def play_zuckerberg(e):
        StopAll()
        Zuckerberg.play()
    
    def play_pages(e):
        StopAll()
        Pages.play()
    
    def play_brin(e):
        StopAll()
        Brin.play()

    def play_c(e):
        StopAll()
        c.play()
    
    def play_cmas(e):
        StopAll()
        cmas.play()
    
    def play_go(e):
        StopAll()
        go.play()
    
    def play_java(e):
        StopAll
        java.play()
    
    def play_javascrip(e):
        StopAll()
        javascrip.play()
    
    def play_kotin(e):
        StopAll()
        kotin.play()
    
    def play_php(e):
        StopAll()
        php.play()
    
    def play_python(e):
        StopAll()
        python.play()
    
    def play_r(e):
        StopAll()
        r.play()
        
    def play_facebook(e):
        StopAll()
        facebook.play()
    
    def play_instagram(e):
        StopAll()
        instagram.play()
    
    def play_twiter(e):
        StopAll()
        twiter.play()
    
    def play_tiktok(e):
        StopAll()
        tiktok.play()
    
    def play_linkedin(e):
        StopAll()
        linkedin.play()
    
    def play_snapchat(e):
        StopAll()
        snapchat.play()
    
    def play_youtube(e):
        StopAll()
        youtube.play()
    
    def play_piterest(e):
        StopAll()
        piterest.play()
    
    def play_whatsapp(e):
        StopAll()
        whatsapp.play()
    
    def play_teletrabajo(e):
        StopAll()
        teletrabajo.play()
    
    def play_ciberseguridad(e):
        StopAll()
        ciberseguridad.play()
    
    def play_nube(e):
        StopAll()
        nube.play()
    
    def play_educacion(e):
        StopAll()
        educacion.play()
    
    def play_telemedicina(e):
        StopAll()
        telemedicina.play()
    
    def play_comercio(e):
        StopAll()
        comercio.play()
    
    def play_redes(e):
        StopAll()
        redes.play()
    
    def play_trabajoremoto(e):
        StopAll()
        trabajoremoto.play()
    
    def play_rastreo(e):
        StopAll()
        rastreo.play()
    
    def play_ia2(e):
        StopAll()
        ia2.play()

    def play_cuantica(e):
        StopAll()
        cuantica.play()

    def play_blockchain(e):
        StopAll()
        blockchain.play()

    def play_g(e):
        StopAll()
        g.play()

    def play_vr(e):
        StopAll()
        vr.play()

    def play_internet(e):
        StopAll()
        internet.play()

    def play_impresion(e):
        StopAll()
        impresion.play()

    def play_robots(e):
        StopAll()
        robots.play()

    def play_energia(e):
        StopAll()
        energia.play()
    
    
    # Botones Padres de la informática con imágenes y etiquetas semánticas
    btn1 = ElevatedButton(content=ft.Image(src="Pascal.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Blaise Pascal"), on_click=play_pascal)
    btn2 = ElevatedButton(content=ft.Image(src="Leibniz.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Gottfried Wilhelm Leibniz"), on_click=play_leibniz)
    btn3 = ElevatedButton(content=ft.Image(src="babbage.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Charles Babbage"), on_click=play_babbage)
    btn4 = ElevatedButton(content=ft.Image(src="Lovelace.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ada Lovelace"), on_click=play_lovelace)
    btn5 = ElevatedButton(content=ft.Image(src="Hollerith.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Herman Hollerith"), on_click=play_hollerith)
    btn6 = ElevatedButton(content=ft.Image(src="Turing.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Alan Turing"), on_click=play_turing)
    btn7 = ElevatedButton(content=ft.Image(src="Neumann.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John von Neumann"), on_click=play_neumann)
    btn8 = ElevatedButton(content=ft.Image(src="shannon.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Claude Shannon"), on_click=play_shannon)
    btn9 = ElevatedButton(content=ft.Image(src="Hopper.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Grace Hopper"), on_click=play_hopper)
    btn10 = ElevatedButton(content=ft.Image(src="McCarthy.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John McCarthy"), on_click=play_mccarthy)
    btn11 = ElevatedButton(content=ft.Image(src="Berners.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Tim Berners-Lee"), on_click=play_berners)
    btn12 = ElevatedButton(content=ft.Image(src="Ritchie.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Dennis Ritchie"), on_click=play_ritchie)
    btn13 = ElevatedButton(content=ft.Image(src="Thompson.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ken Thompson"), on_click=play_thompson)
    btn14= ElevatedButton(content=ft.Image(src="Gosling.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="James Gosling"), on_click=play_gosling)
    btn15 = ElevatedButton(content=ft.Image(src="Jobs.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Jobs"), on_click=play_jobs)
    btn16 = ElevatedButton(content=ft.Image(src="Wozniak.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Wozniak"), on_click=play_wozniak)
    btn17 = ElevatedButton(content=ft.Image(src="Gates.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Bill Gates"), on_click=play_gates)
    btn18 = ElevatedButton(content=ft.Image(src="Zuckerberg.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Mark Zuckerberg"), on_click=play_zuckerberg)
    btn19 = ElevatedButton(content=ft.Image(src="Pages.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Larry Page"), on_click=play_pages)
    btn20 = ElevatedButton(content=ft.Image(src="Brin.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Sergey Brin"), on_click=play_brin)
    
    btn21= ElevatedButton(content=ft.Image(src="c.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="c"), on_click=play_c)
    btn22= ElevatedButton(content=ft.Image(src="c2.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="c+"), on_click=play_cmas)
    btn23= ElevatedButton(content=ft.Image(src="go.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="go"), on_click=play_go)
    btn24= ElevatedButton(content=ft.Image(src="java.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="java"), on_click=play_java)
    btn25= ElevatedButton(content=ft.Image(src="javascrip.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="javascrip"), on_click=play_javascrip)
    btn26= ElevatedButton(content=ft.Image(src="kotin.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="kotlin"), on_click=play_kotin)
    btn27= ElevatedButton(content=ft.Image(src="php.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="php"), on_click=play_php)
    btn28= ElevatedButton(content=ft.Image(src="python.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="python"), on_click=play_python)
    btn29= ElevatedButton(content=ft.Image(src="r.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="r"), on_click=play_r)
    
    btn33= ElevatedButton(content=ft.Image(src="facebook.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="facebook"),on_click=play_facebook)
    btn34= ElevatedButton(content=ft.Image(src="instagram.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="instagram"), on_click=play_instagram)
    btn35= ElevatedButton(content=ft.Image(src="twiter.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="twitter"), on_click=play_twiter)
    btn36= ElevatedButton(content=ft.Image(src="tiktok.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="tiktok"), on_click=play_tiktok)
    btn37= ElevatedButton(content=ft.Image(src="linkedin.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="linkedin"), on_click=play_linkedin)
    btn38= ElevatedButton(content=ft.Image(src="snapchat.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="snapchat"), on_click=play_snapchat)
    btn39= ElevatedButton(content=ft.Image(src="youtube.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="yotube"), on_click=play_youtube)
    btn40= ElevatedButton(content=ft.Image(src="pinterest.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="pinterest"), on_click=play_piterest)
    btn41= ElevatedButton(content=ft.Image(src="whatsapp.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="whatsapp"), on_click=play_whatsapp)
    
    btn45= ElevatedButton(content=ft.Image(src="teletrabajo.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="teletrabajo"), on_click=play_teletrabajo)
    btn46= ElevatedButton(content=ft.Image(src="ciberseguridad.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="ciberseguridad"), on_click=play_ciberseguridad)
    btn47= ElevatedButton(content=ft.Image(src="nube.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="nube"), on_click=play_nube)
    btn48= ElevatedButton(content=ft.Image(src="educacion.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="educacion"), on_click=play_educacion)
    btn49= ElevatedButton(content=ft.Image(src="telemedicina.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="telemedicina"), on_click=play_telemedicina)
    btn50= ElevatedButton(content=ft.Image(src="comercio.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="ciber comercio"), on_click=play_comercio)
    btn51= ElevatedButton(content=ft.Image(src="redes.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="redes"), on_click=play_redes)
    btn52= ElevatedButton(content=ft.Image(src="ia.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="ia"), on_click=play_ia2)
    btn53= ElevatedButton(content=ft.Image(src="trabajo.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="trabajo"), on_click=play_trabajoremoto)
    
    btn57= ElevatedButton(content=ft.Image(src="ia2.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="ia"), on_click=play_ia2)
    btn58= ElevatedButton(content=ft.Image(src="cuantica.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="computadoras cuanticas"), on_click=play_cuantica)
    btn59= ElevatedButton(content=ft.Image(src="bloakchain.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="blockchain"), on_click=play_blockchain)
    btn60= ElevatedButton(content=ft.Image(src="g.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="5G"), on_click=play_g)
    btn61= ElevatedButton(content=ft.Image(src="vr.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="VR"), on_click=play_vr)
    btn62= ElevatedButton(content=ft.Image(src="internet.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="internet de las cosas"), on_click=play_internet)
    btn63= ElevatedButton(content=ft.Image(src="impresion.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="impresion 3d"), on_click=play_impresion)
    btn64= ElevatedButton(content=ft.Image(src="robots.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="robots"), on_click=play_robots)
    btn65= ElevatedButton(content=ft.Image(src="energia.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="energia limpia"), on_click=play_energia)
    # Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        
        # Vista de portada
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("La historia de la Informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Los padres de la informática',
                                        on_click=lambda _: [StopAll(), page.go('/padres')]
                                    ),
                                    ElevatedButton(
                                        'la evolucion de de los lenguajes de programacion',
                                        on_click=lambda _: [StopAll(), page.go('/lenguajes')]
                                    ),
                                    ElevatedButton(
                                        'las redes sociales',
                                        on_click=lambda _: [StopAll(), page.go('/redes')]
                                    ),
                                    ElevatedButton(
                                        'la informatica durante la pandemia de covid-19',
                                        on_click=lambda _: [StopAll(), page.go('/pandemia')]
                                    ),
                                    ElevatedButton(
                                        'las nuevas tecnologias',
                                        on_click=lambda _: [StopAll(), page.go('/tecnologias')]
                                    ),
                                    ft.Image(
                                        src="Portada.png",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Escucha el intro",
                                        on_click=play_intro
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Vista de los padres de la informática
        elif page.route == '/padres':
            page.views.append(
                View(
                    "/padres",
                    controls=[
                        AppBar(
                            title=ft.Text("Los padres de la informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3,btn4
                                        ]
                                    ),
                                    ft.Row(
                                      alignment="center",
                                      controls=[
                                        btn5, btn6, btn7,btn8
                                      ]  
                                    ),
                                    ft.Row(
                                       alignment="center",
                                        controls=[
                                          btn9, btn10, btn11,btn12
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn13,btn14,btn15,btn16
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn17,btn18,btn19,btn20
                                        ] 
                                    ),
                                     ElevatedButton(
                                        'La evolución de los lenguajes de programación',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de la evolución de los lenguajes de programación
        elif page.route == '/lenguajes':
            page.views.append(
                View(
                    "/lenguajes",
                    controls=[
                        AppBar(
                            title=ft.Text("La evolución de los lenguajes de programación"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn21, btn22, btn23,
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn25,btn26,btn27,
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn29,btn24,btn28
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
            #vista de redes sociales
        elif page.route == '/redes':
            page.views.append(
                View(
                    "/redes",
                    controls=[
                        AppBar(
                            title=ft.Text("Las redes sociales"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn33, btn34, btn35,
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn37, btn38, btn39,
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn41,btn36,btn40
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
            #vista de la informatica en pandemia
        elif page.route == '/pandemia':
            page.views.append(
                View(
                    "/pandemia",
                    controls=[
                        AppBar(
                            title=ft.Text("la informatica durante la pandemia"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn45,btn46,btn47,
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn49, btn50, btn51,
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn53,btn52,btn48
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
            #visita de nuevas tecnologias
        elif page.route == '/tecnologias':
            page.views.append(
                View(
                    "/tecnologias",
                    controls=[
                        AppBar(
                            title=ft.Text("La evolución de los lenguajes de programación"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn58, btn59,btn60
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn61, btn62,btn64
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn65, btn63,btn57
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
#ft.app(target=main,view=ft.WEB_BROWSER, assets_dir="assets")
