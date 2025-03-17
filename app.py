import streamlit as st
import random
st.title("🎲 High-Low Game!")

NUM_ROUNDS = 5
score = 0

st.write("Welcome to High-Low game!")
st.write("-" * 30)

for round_number in range(1, NUM_ROUNDS + 1):

  my_random_num:int = random.randint(1, 100)
  computer_random_num:int = random.randint(1, 100)

  st.write(f'Round {round_number}')
  st.write("-" * 30)
  st.write(f"Your number is {my_random_num}")

  user_guess = st.text_input("Do you think your number is Higher or lower than the computer's?: ").lower()

  if ((user_guess == "higher" and computer_random_num > my_random_num)
  or (user_guess == "lower" and computer_random_num < my_random_num)):
    st.write(f"✅you got a point +1.The computer number is {computer_random_num}")
    score += 1
  else:
    st.write(f"❌wrong answer.The computer number is {computer_random_num}")
st.write(f'🎉Game over!Your final score is {score}')


if score == NUM_ROUNDS:
  st.write(f' 🏆 Wow! you played perfectly')
elif score >= NUM_ROUNDS-3:
  st.write(f' 👏 Good job you played really well')
else:
  st.write(f' 💡 luck next time')
