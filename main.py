import random
from ai.creator import CreatorAI
from ai.preserver import PreserverAI
from ai.destroyer import DestroyerAI
from ai.conversation import Conversation

def main():
    creator = CreatorAI()
    preserver = PreserverAI()
    destroyer = DestroyerAI()

    conversation_history = []  # Initialize empty conversation history
    num_steps = 1
    current_step = 0

    while True:  # Outer loop to continue the conversation
        while current_step < num_steps:
            conversation = Conversation(creator, preserver, destroyer)
            conversation.start(conversation_history)
            conversation_history.extend(conversation.conversation_history)
            current_step += 1

        continue_choice = input("Continue the conversation (y/n)? ").lower()

        if continue_choice == "n":
            print("Conversation terminated.")
            break

        elif continue_choice == "y":
            num_steps += 1
            current_step = 0
            continue

        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()