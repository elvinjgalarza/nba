#allows the application to start
from flask import Flask
#sends nba data from py file to html file 
from flask import render_template

import nba_py

#to make date objects
from datetime import datetime

#app is used to run/initiate the server
app = Flask(__name__)

#backslash represents the main front page
@app.route("/") 
#function for the directing homepage
def index():
	#call the function below
	games = get_games()
	return render_template("index.html",
					title = "Daily Scores")


	"""taking advantage of the library and the 
	Scoreboard class written by the the dev
	of the API... only nba_py.Scoreboard because
	it's in THEIR  __init__.py ...

	Get lists of games for the day .
	
	Args:
		date: datetime object of the day that we want games.

	Returns:
		games: An array of dictionaries of the games that were
			   played today.
	"""
	Args date
def get_games(date):

	scoreboard = nba_py.Scoreboard()
	print(scoreboard.line_score())

#this is our main function where the app is run
if __name__ == "__main__":
	# run the app on local host with threads to run simultaneous calls
	app.run(host = "0.0.0.0", port = "8080", threaded = True, debug = True)

	#for a real server... the top line is for development
	#app.run(threaded=True)