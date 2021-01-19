from typing import List

from flask import Flask, render_template, url_for, request, redirect

import sys
from flask import session
from classes import Viking, Armoury

app = Flask(__name__)
app.secret_key = 'app secret key'




@app.route('/')
@app.route('/home')
def home():
    global hotSeatPlayers
    hotSeatPlayers = [Viking(), Viking()]
    global hotSeatStatus
    hotSeatStatus = [0, 0]
    return render_template('home.html')


@app.route('/manual')
def about():
    return render_template('manual.html', h1='Instrukcja')


@app.route('/hotseat', methods=['GET', 'POST'])
def hotseat():
    if request.method == 'POST':
        form = request.form
        if form['action'] == 'fight' and hotSeatStatus == [1, 1]:
            if 'turn-counter' not in session:
                session['turn-counter'] = 0
            else:
                session['turn-counter'] = 0
            return redirect("/pvp")
    return render_template('hotseat.html', h1='Gracz kontra Gracz', status=hotSeatStatus)
@app.route('/pvp', methods=['GET', 'POST'])
def pvp():

    turn = session["turn-counter"] % 2
    viking = hotSeatPlayers[turn]
    enemyNmb = (session["turn-counter"] + 1) % 2
    enemy = hotSeatPlayers[enemyNmb]

    if request.method == 'POST':
        form = request.form
        if form['action'] == "start":
            pass
        if form['action'] == "hPotion":
            viking.usePotion("hPotions")
        elif form['action'] == "sPotion":
            viking.usePotion("sPotions")
        elif form['action'] == "light-strike":
            viking.lightAttack(enemy)
        elif form['action'] == "power-strike":
            viking.strongAttack(enemy)
        elif form['action'] == "rest":
            viking.rest()

    if viking.Hitpoints == 0:
        return redirect("/fight-over?winner=" + str(enemyNmb))
    elif enemy.Hitpoints == 0:
        return redirect("/fight-over?winner=" + str(turn))

    if session['turn-counter'] % 2 == 0:
        turn = 0
    else:
        turn = 1
    return render_template('pvp.html', h1="Tura - "+hotSeatPlayers[turn].name, players = hotSeatPlayers, turn = turn)
@app.route('/fight-over', methods=['GET', 'POST'])
def fightOver():
    winner = int(request.args.get('winner', None))
    viking = hotSeatPlayers[winner]
    return render_template('after-battle.html', h1="Zwyciężył - "+viking.name, appearance=viking.appearance, eq=viking.eq)
@app.route('/edit-player', methods=['GET', 'POST'])
def edit_player():
    player = request.args.get('player', None)
    playerNumber = int(player)-1
    if request.method == 'POST':
        form = request.form
        if form['status'] == "yes":
            hotSeatStatus[playerNumber] = 1
        elif form['status'] == "no":
            hotSeatStatus[playerNumber] = 0
    # print(playerNumber, file=sys.stderr)
    return render_template('edit-player.html', h1='Dostosuj postać', player=playerNumber + 1, status=hotSeatStatus[playerNumber])


@app.route('/name', methods=['GET', 'POST'])
def name():
    player = request.args.get('player', None)
    playerNumber = int(player) - 1
    viking = hotSeatPlayers[playerNumber]
    if request.method == 'POST':
        form = request.form
        if form['name'] != '':
            viking.setName(form['name'])
            return redirect("/edit-player?player=" + str(playerNumber + 1))
    return render_template('name.html', h1='Wybierz nazwę', player=playerNumber + 1, name=viking.name)


@app.route('/attributes', methods=['GET', 'POST'])
def attributes(basePoints=10):
    player = request.args.get('player', None)
    playerNumber = int(player) - 1
    viking = hotSeatPlayers[playerNumber]
    points = viking.firstPoints(basePoints)

    # print(points[0], file=sys.stderr)
    if request.method == 'POST':
        form = request.form
        attr = form['attr']
        action = form['action']
        if action == 'up' and points > 0:
            points -= 1
            viking.attrU(attr, 1)

        elif action == 'down' and viking.attributes[attr] > 1:
            points += 1
            viking.attrD(attr, 1)

    # print(points, file=sys.stderr)
    return render_template('attributes.html', h1='Wybierz atrybuty', points=points, player=playerNumber + 1, attributes=viking.attributes)


@app.route('/appearance', methods=['GET', 'POST'])
def appearance():
    player = request.args.get('player', None)
    playerNumber = int(player) - 1
    viking = hotSeatPlayers[playerNumber]
    if request.method == 'POST':
        form = request.form
        part = form['part']
        action = form['action']
        viking.changeApperiance(part, action)

    return render_template('appearance.html', h1='Edytuj wygląd', appearance=viking.appearance, player=playerNumber + 1)
@app.route('/items', methods=['GET','POST'])
def items():
    player = request.args.get('player', None)
    playerNumber = int(player) - 1
    viking = hotSeatPlayers[playerNumber]
    armoury = Armoury()
    items = armoury.getItems()
    if request.method == 'POST':
        form = request.form
        if form['itemType'] == 'hPotions':
            if form['action'] == 'more':
                viking.morePotion("hPotions")
            else:
                viking.lessPotion("hPotions")
        elif form['itemType'] == 'sPotions':
            if form['action'] == 'more':
                viking.morePotion("sPotions")
            else:
                viking.lessPotion("sPotions")
        else:
            item = form['number']
            itemType = form['itemType']
            if itemType == "weapon":
                if armoury.getItem(itemType, int(item)).wClass == "tHanded" and viking.eq['shield'] != 0:
                    pass
                else:
                    viking.changeItem(itemType, item)
            elif itemType == "shield":
                if armoury.getItem("weapon", viking.eq['weapon']).wClass == "tHanded":
                    pass
                else:
                    viking.changeItem(itemType, item)
            else:
                viking.changeItem(itemType, item)
    return render_template('items.html', h1='Wybierz ekwipunek', appearance=viking.appearance, eq=viking.eq, player=playerNumber + 1, items=items)
if __name__ == '__main__':
    app.run(debug=True)
