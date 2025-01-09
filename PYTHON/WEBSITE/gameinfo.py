from flask import Blueprint, render_template

gameinfo = Blueprint('gameinfo', __name__)
image = str
game_title = []
game_info = []
game_release = str
page_title = str



@gameinfo.route('/botw')
def botw():
    return render_template(
            "GAME_INFO/gameinfo.html", image = "IMG/botw.png", 
            game_info = ["The Legend of Zelda: Breath of the Wild is an award winning acion-adventure game published in 2017 by Nintendo.", 
            "Experience a post-apocalyptic world set at the end of the Zelda timeline, playing as an amnesiac Link as he sets", 
            "out to save Princess Zelda and stop Calamity Ganon from corrupting the world."],

            game_release = "March 3rd 2017", 
            game_title = ["The Legend of Zelda:", "Breath of the Wild"],
            page_title = "Breath of the Wild"
            )



@gameinfo.route('/celeste')
def celeste():
    return render_template(
            "GAME_INFO/gameinfo.html", image = "IMG/celeste.png", 
            game_info = ["Celeste is an award winning 2D pixel-platformer published in 2018 by indie-studio Maddy Makes Games. ", 
            "Control Madeline, a young women set out to climb Celeste Mountain to overcome her", 
            "anxiety and depression. Jump, climb and dash your way through challenging platforming gameplay."],

            game_release = "October 8th 2024", 
            game_title = ["Celeste", ""],
            page_title = "Celeste"
            )



@gameinfo.route('/dbsz')
def dbsz():
    return render_template(
            "GAME_INFO/gameinfo.html", image = "IMG/dbsz.png", 
            game_info = ["DRAGON BALL: Sparking! ZERO is a 2024 arena fighter developed by", 
            "Spike Chunsoft and published by Bandai Namco. <br><br> Master sophisticated", 
            "combat systems as one of 182 characters from the Dragon Ball series, written by Akira Toriyama (R.I.P)."],

            game_release = "October 8th 2024", 
            game_title = ["DRAGON BALL:", "Sparking! ZERO"],
            page_title = "DBSZ"
            )



@gameinfo.route('/deadcells')
def deadcells():
    return render_template(
            "GAME_INFO/gameinfo.html", image = "IMG/deadcells.png", 
            game_info = ["Dead Cells is an award winning rouge-like-metroidvania game developed by Motion Twin ", 
            "Play as an amorphous creature named the 'Prisoner' and fight your way through procedurally", 
            "generated rooms, mastering various unique weapons in order to slay the King of a diseasd island."],

            game_release = "May 10th 2017", 
            game_title = ["Dead Cells", ""],
            page_title = "Dead Cells"
            )



@gameinfo.route('/eldinring')
def eldinring():
    return render_template(
            "GAME_INFO/gameinfo.html", image = "IMG/eldinring.png", 
            game_info = ["Eldin Ring is a 2022 Game of the Year souls-like action-roleplaying game developed by FromSoftware", 
            "Experience punishing gameplay while fighting rage-endusing bosses and finding hidden dungeons in a", 
            "content-filled fantasy open-world."],

            game_release = "February 25th 2022", 
            game_title = ["Eldin Ring", ""],
            page_title = "Eldin Ring"
            )



@gameinfo.route('/got')
def got():
    return render_template(
            "GAME_INFO/gameinfo.html", image = "IMG/got.png", 
            game_info = ["Ghost of Tsushima is an action-adventure game set in 11th Century Japan ", 
            "during the first Mongol Invasian, developed by Sony Interactive Entertainment", 
            "Explore the vast open-world of Tsushima, filled with beautiful scenery, secrets and enemy camps, all made within the style of 11th Century Japan"],

            game_release = "July 17th 2020", 
            game_title = ["Ghost of Tsushima", ""],
            page_title = "Ghost of Tsushima"
            )



@gameinfo.route('/hollowknight')
def hollowknight():
    return render_template(
            "GAME_INFO/gameinfo.html", image = "IMG/hollowknight.png", 
            game_info = ["Hollow Knight is an indie metroidvania platformer developed by Aussie indie-studio Team Cherry", 
            "Explore the insect world of Hallownest, a fallen kingdom plagued by a mysterious supernatural infection,", 
            "turning it and it's inhabitants hostile. Discover dark secrets and fight challenging bosses in this award-winning metroidvania"],

            game_release = "Februrary 24th 2017", 
            game_title = ["Hollow Knight", ""],
            page_title = "Hollow Knight"
            )



@gameinfo.route('/minecraft')
def mineacraft():
    return render_template(
            "GAME_INFO/gameinfo.html", image = "IMG/minecraft.png", 
            game_info = ["Minecraft is a procedurally generated voxel-sandbox developed by Mojang Studios", 
            "Mine, craft and build in an infinitely-sized world, doing whatever your mind pleases, whether that be", 
            "building a house, mining for diamonds or defeating the Ender Dragon."],

            game_release = "November 18th 2011", 
            game_title = ["Minecraft", ""],
            page_title = "Minecraft"
            )



@gameinfo.route('/pkmn-bw')
def pokemon_bw():
    return render_template(
            "GAME_INFO/gameinfo.html", image = "IMG/bw.png", 
            game_info = ["Pokémon Black and White are role-playing adventure games developed by Game Freak and published by The Pokémon Company and Nintendo", 
            "Explore the Unova Region in the 5th generation of Pokémon Games as a young Pokémon ", 
            "Trainer. Train, battle and capture various Pokémon to complete your ultimate goal of becoming a Pokémon Champion"],

            game_release = "September 18th 2010", 
            game_title = ["Pokémon", "Black and White"],
            page_title = "Pokémon Black and White"
            )



@gameinfo.route('/sa2')
def sa2():
    return render_template(
            "GAME_INFO/gameinfo.html", image = "IMG/sa2.png", 
            game_info = ["Sonic Adventure 2 is an action platformer published by SEGA", 
            "ollow Sonic, Shadow and friends as you play through various levels, uncovering the mysteries of Shadow's origin", 
            "and prevent the destruction of the World."],

            game_release = "June 18th 2001", 
            game_title = ["Sonic Adventure 2", ""],
            page_title = "Sonic Adventure 2"
            )