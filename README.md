# TicTakToe-Raw-Sockets-Python
this is the implemntaion of the game TicTakToe using Raw Sockets in python 
I divided my python program in to 9 modules or functions

<img src="https://github.com/kunz398/TicTakToe-Raw-Sockets-Python/blob/master/readmefiles/1.png" />
<hr />

<p>What happens is it firstly calls the form_submit function to check if a submission has been made<br>
once it has been made the player_move function is invoked for the human’s movement on the board<br>
then after that inside a while loop the function computer_turn is made so that if the computer chooses a spot which has already been used<br>
it won’t select that space again after all that is done then the final function who_wins to decide who wins is called.</p>
<img src="https://github.com/kunz398/TicTakToe-Raw-Sockets-Python/blob/master/readmefiles/2.png" />

<h1>Who_wins</h1>
<img src="https://github.com/kunz398/TicTakToe-Raw-Sockets-Python/blob/master/readmefiles/3.png" />
Two arrays were declared then I used numpy to separate them in to parts , <br>
like this diagonal and the reverse diagonal and the first row and so on
Then I checked them with the <b>check_X</b. and <b>check_O</b> <br>
<b>check_X</b> = when a player makes a move <br>
<b>check_O</b> = when a computer makes a move
<hr/>

<h1>Who_wins</h1>
<img src="https://github.com/kunz398/TicTakToe-Raw-Sockets-Python/blob/master/readmefiles/4.png" />
I made a random number generator between 1 to 9. So what I did was ever time a move is made it is inserted in to
a variable called history so every move
gets recorded in the history array and If a move is present in the history array the computer will choose another move.

*I also made a supplementary 2D array for calculating where in the board a player has made a move and so this gave me a way to calculate who would win

<center><u><b>How to run</b></u></center>
1) open up <i>rawsockets.py</i> and run it it will say 
<i>Serving HTTP on port 8888</i>
2) Open up Browser and type <i>localhost:8888</i> 
3) you will see a display like so:
<img src="https://github.com/kunz398/TicTakToe-Raw-Sockets-Python/blob/master/readmefiles/5.png" />

