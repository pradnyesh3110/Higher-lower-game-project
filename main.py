import random
from game_data import data
from art import logo
print(logo)
def format_data(account):
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name},a {account_descr},from {account_country}"
def check_answer(user_guess,a_followers,b_followers):
    if a_followers>b_followers and user_guess=='a':
        return user_guess=='a'
    else:
        return user_guess=='b'
score=0
account_b=random.choice(data)
game_should_continue=True
while game_should_continue:
    account_a=account_b
    print(f"compare_a:{format_data(account_a)}")
    from art import vs
    print(vs)
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    print(f"compare_b:{format_data(account_b)}")
    guess=input("who has more followers than A or B:").lower()
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    if is_correct:
        score+=1
        print(f'YOU WIN and the score is{score}')
    else:
        print(f"sorry thats wrong then final score is:{score}")
        game_should_continue=False
