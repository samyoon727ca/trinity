# main.py
import random

from ai.creator import CreatorAI
from ai.preserver import PreserverAI
from ai.destroyer import DestroyerAI
from ai.conversation import Conversation

def main():
    creator = CreatorAI()
    preserver = PreserverAI()
    destroyer = DestroyerAI()

    # initial_prompt = """
    # """

    conversation = Conversation(creator, preserver, destroyer)

    num_steps = 7
    current_step = 0

    conversation_history = []  # Initialize empty conversation history

    while current_step < num_steps:
        conversation = Conversation(creator, preserver, destroyer)  # Create new Conversation object
        conversation.start(conversation_history)  # Pass conversation history as argument
        conversation_history.extend(conversation.conversation_history)  # Update conversation history
        current_step += 1


    # User prompt to continue (same logic as before)
    while True:
        continue_choice = input("Continue the conversation (y/n)? ").lower()
        if continue_choice == "y":
            num_steps += 3
            break
        elif continue_choice == "n":
            print("Conversation terminated.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()