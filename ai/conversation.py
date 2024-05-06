# ai/conversation.py
from typing import List, Tuple

class Conversation:
    def __init__(self, creator, preserver, destroyer):
        self.creator = creator
        self.preserver = preserver
        self.destroyer = destroyer
        self.conversation_history = []

    def start(self, conversation_history):
        # Build the initial prompt from the conversation history
        initial_prompt = "\n".join(f"{role}: {output}" for role, output in conversation_history)

        creator_output = self.creator.generate_idea(initial_prompt)  # Use initial prompt
        self.log_conversation("Creator", creator_output)
        current_prompt = creator_output
        self.log_prompt(current_prompt)  # Log the initial prompt

        while True:  # Loop for two conversation cycles (adjust as needed)
            # Update the prompt with the last output from each role
            last_outputs = "\n".join(f"{role}: {output}" for role, output in self.conversation_history[-2:])
            current_prompt = last_outputs
            self.log_prompt(current_prompt)  # Log the updated prompt

            # Generate responses from preserver and destroyer
            preserver_output = self.preserver.generate_preservation(current_prompt)
            self.log_conversation("Preserver", preserver_output)
            current_prompt += f"\nPreserver: {preserver_output}"

            destroyer_output = self.destroyer.generate_destruction(current_prompt)
            self.log_conversation("Destroyer", destroyer_output)
            current_prompt += f"\nDestroyer: {destroyer_output}"

            # Update the prompt for the next creator turn
            creator_output = self.creator.generate_idea(current_prompt)
            self.log_conversation("Creator", creator_output)
            current_prompt += f"\nCreator: {creator_output}"

            # Break the loop after a set conversation length (adjust as needed)
            if len(self.conversation_history) >= 7:  # Example: Break after 10 conversation entries
                break  # Exit the loop

    def log_conversation(self, role, output):
        self.conversation_history.append((role, output))
        print(f"{role}: {output}")
        # Optionally, you can write the conversation to a log file
        with open("logs/conversations.log", "a") as f:
            f.write(f"{role}: {output}\n")

    def log_prompt(self, prompt):
        print(f"Current Prompt: {prompt}")
        # Optionally, you can write the prompt to a log file
        with open("logs/prompts.log", "a") as f:
            f.write(f"Current Prompt: {prompt}\n\n")

    def get_last_output(self):
        # Access the last conversation entry (assuming preserver)
        if self.conversation_history:
            last_role, last_output = self.conversation_history[-1]
            return last_output
        else:
            return ""  # Handle empty conversation history