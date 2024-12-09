"""
Module: a Flask application that serves as the
interface for our gambling application, using
flask-login to initialize user data storage
"""

# import necessary pkgs
from flask import Flask, render_template, request, redirect, url_for, jsonify
import flask_login
from flask_login import login_user, logout_user, login_required
from craps_func import linebet, buybet
from blackjack import Hand, Deck, Card
import blackjack as bj
import db

# instantiate flask app, create key
app = Flask(__name__)
app.secret_key = "letsgogambling"

# setup flask login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# simulate database of users, placeholder until pymongo connection
db.register_user("abc", "xyz")
users = db.get_users()
# users = {}
# users["abc"] = {"password": "xyz"}

users_balance = {'abc': 500,
                 'zyx': 900}

# create User object
class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return
    
    user = User()
    user.id = username
    return user

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    if username not in users:
        return
    
    user = User()
    user.id = username
    return user
    
@app.route("/")
def redirect_home():
    return redirect(url_for('show_login'))

@app.route("/login_screen", methods = ["GET","POST"])
def show_login():

    error_msg = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # error handling for missing/incorrect values
        if username in users and password == users[username]['password']:
            user = User()
            user.id = username
            flask_login.login_user(user)
            return redirect(url_for('user_home', username=username))        
        else:
            error_msg = "Invalid credentials, please try again."

    return render_template('login.html', error_msg=error_msg)

@app.route('/<username>', methods = ["POST", "GET"])
@flask_login.login_required
def user_home(username):
    # if username in users_balance:
    #     user_balance = users_balance[username]['balance']
    #     return render_template('user_home.html', username=username, balance = user_balance)
    user_balance = db.get_bal(username)
    return render_template('user_home.html', username=username, balance = user_balance)
    
@app.route("/<username>/craps", methods = ["POST", "GET"])
@flask_login.login_required
def craps_home(username):
    balance = request.form['balance']
    return render_template("craps_home.html", username=username, balance=balance)


@app.route("/<username>/craps/playline", methods=["POST"])
@flask_login.login_required
def playline(username):
    win = True if request.form["bettype"] == 'p' else False
    bet = float(request.form["betamount"])
    balance = float(request.form["balance"])
    rolls, result = linebet(win)
    #return_text= "Here are the rolls:\n"
    return_text = ""
    for r in rolls:
        return_text+=r + "@"
    
    win = False
    if result == 'w':
        return_text += "You win!"
        balance += bet
        win = True
    elif result == 'l':
        return_text+= "You lost!"
        balance-=bet 
    else:
        return_text += "It was a tie!"

    db.update_bal(username, balance, win, "craps")

    # update database maybe use requests?
    # or maybe make a different .py that will make a request

    return render_template("craps_results.html", username=username, balance=balance, textResult=return_text)


@app.route("/<username>/craps/playbuy", methods=["POST"])
@flask_login.login_required
def playbuy(username):
    win = True if request.form["bettype"] == 'b' else False
    bet = float(request.form["betamount"])
    place = int(request.form["buynum"])
    balance = float(request.form["balance"])
    rolls, result, odds = buybet(win, place)
    return_text= ""
    win = False
    for r in rolls:
        return_text+=r + "@"
    if result == 'w':
        return_text += "You win!"
        balance += bet * odds
        win = True
    elif result == 'l':
        return_text+= "You lost!"
        balance-=bet 

    db.update_bal(username, balance, win, "craps")
    
    return render_template("craps_results.html", username=username, balance=balance, textResult=return_text)


@app.route('/logout', methods = ["GET", "POST"])
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return redirect(url_for('show_login'))

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401

@app.route("/<username>/blackjack", methods = ["POST"])
def bj_home(username):
    balance = request.form['balance']
    return render_template("bj_home.html", username=username, balance=balance)

deck = Deck()
dealer = Hand()
player = Hand()


@app.route("/<username>/blackjack/play", methods = ["POST"])
def bj_play(username):
    global deck
    global player
    global dealer
    prev = request.form["prev"]
    balance = float(request.form["balance"])
    bet = float(request.form["betamount"])
    turn = int(request.form["turn"]) + 1
    if len(prev) == 1:
        # start game
        deck = Deck()
        dealer = Hand()
        player = Hand()

        player.add_card(deck.deal_one())
        player.add_card(deck.deal_one())

        dealer.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())
        prev = bj.show_some(player, dealer)
    else:
        dec = request.form["dec"]
        if dec == 'h':
            prev += "@" + bj.take_hit(deck, player)
            if player.value > 21:
                #player went bust
                balance -=bet
                prev += "@You went bust!"
                db.update_bal(username, balance, False, "blackjack")
                return render_template("bj_result.html", username=username, prev=prev, balance=balance)
        else:
            prev += "@Player Stands. Dealers Turn:"
            prev += "@" + bj.show_all(player, dealer)
            while dealer.value <= 17:
                prev += "@Dealer hits."
                prev += "@" + bj.take_hit(deck, dealer)

            if dealer.value > 21:
                prev += "@" +  bj.dealer_busts()
                balance+=bet
                db.update_bal(username, balance, True, "blackjack")
            elif dealer.value > player.value:
                prev += "@" + bj.dealer_wins()
                balance-=bet
                db.update_bal(username, balance, False, "blackjack")
            elif dealer.value < player.value:
                prev += "@" + bj.player_wins()
                balance+=bet
                db.update_bal(username, balance, True, "blackjack")
            else:
                prev += "@" + bj.push()
            
            return render_template("bj_result.html", username=username, prev=prev, balance=balance)

    return render_template("bj_play.html", username=username, prev=prev, balance=balance, bet=bet, turn=turn)

@app.route("/register", methods=["GET", "POST"])
def register():
    """handles account creation interface and functionality"""
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")

        # validation logic
        if username in users:
            error = "Error: Username already exists, try another!"
        elif not username or not password:
            error = "Error: Username or password left blank."
        elif password != password_confirm:
            error = "Error: Passwords do not match."
        else:
            # Add new user to "database"
            users[username] = {"password": password}
            db.register_user(username, password)
            return redirect(url_for("show_login"))

    return render_template("register.html", error=error)


if __name__ == "__main__":
    app.run(debug=True, host="134.122.3.54", port=5000)
