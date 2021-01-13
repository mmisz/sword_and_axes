from flask import Flask, render_template, url_for, request, redirect
import classes

import sys

app = Flask(__name__)

global hotSeatPlayers
hotSeatPlayers = [classes.Viking(), classes.Viking()]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/manual')
def about():
    return render_template('manual.html', h1='Instrukcja')


@app.route('/hotseat', methods=['GET', 'POST'])
def hotseat():
    return render_template('hotseat.html', h1='Gracz kontra Gracz')


@app.route('/edit-player', methods=['GET', 'POST'])
def edit_player():
    player = request.args.get('player', None)
    playerNumber = int(player)
    # print(playerNumber, file=sys.stderr)
    return render_template('edit-player.html', h1='Dostosuj postać', player=playerNumber)


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
    if request.method == 'POST':
        form = request.form
    return render_template('items.html', h1='Wybierz ekwipunek', appearance=viking.appearance, eq=viking.eq, player=playerNumber + 1, items=classes.Armoury)
if __name__ == '__main__':
    app.run(debug=True)