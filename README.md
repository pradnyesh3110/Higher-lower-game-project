# Higher-lower-game-project
Higher Lower Game 
This is a simple Higher-Lower command-line game built using Python.
You guess which account has more followers based on given data.
If your guess is correct, you continue playing; if wrong, the game ends.

 How It Works:
Randomly selects two accounts from a data list (game_data).

Displays account name, description, and country (but not the follower count).

You guess which account (A or B) has more followers.

If you guess correctly:

Your score increases by 1.

The next round continues with the previous "B" becoming the new "A".

If you guess incorrectly:

The game ends.

Your final score is displayed.

 How to Run:
Make sure you have Python 3 installed.

Clone or download this repository.

Ensure you have the files:

game_data.py (contains account info)

art.py (contains ASCII art for logo and "vs")

Run the following command in terminal:

bash
Copy
Edit
python main.py
 Project Structure:
bash
Copy
Edit
- main.py         # Game logic
- game_data.py    # Data source for accounts
- art.py          # ASCII art for logo and "vs"
- README.md       # Project description
 Example Output:
vbnet
Copy
Edit
Welcome to the Higher Lower Game!

Compare A: Cristiano Ronaldo, a footballer, from Portugal
VS
Compare B: Selena Gomez, a singer and actress, from United States

Who has more followers? Type 'A' or 'B': a

YOU WIN and the score is 1
...
 Notes:
The account data (name, description, country, follower_count) is preloaded from game_data.py.

After each round, a new random account is selected for comparison.

If by chance the same account is chosen twice, a new random selection happens automatically.

 Future Improvements:
Add levels of difficulty (easy, medium, hard).

Add animations or better UI (using libraries like curses or simple GUI like tkinter).

Keep track of highest score across plays.

