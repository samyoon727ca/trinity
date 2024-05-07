# ai/conversation.py
from typing import List, Tuple

class Conversation:
    def __init__(self, creator, preserver, destroyer):
        self.creator = creator
        self.preserver = preserver
        self.destroyer = destroyer
        self.conversation_history = []

    def start(self, conversation_history):
        # Initialize self.conversation_history with the provided conversation_history
        # or with ["imagine"] if conversation_history is empty
        self.conversation_history = conversation_history if conversation_history else ["imagine"]

        # Build the initial prompt from the conversation history
        initial_prompt = ""
        for entry in self.conversation_history:
            if isinstance(entry, tuple):
                role, output = entry
                initial_prompt += f"\n{role}: {output}"
            else:
                initial_prompt += f"\n{entry}"

        creator_output = self.creator.generate_idea(initial_prompt)  # Use initial prompt
        self.log_conversation("", creator_output)
        current_prompt = creator_output
        self.log_prompt(current_prompt)  # Log the initial prompt
        
        while True:  # Loop for two conversation cycles (adjust as needed)
            # Update the prompt with the last output from each role
            last_outputs = ""
            for entry in self.conversation_history[-1:]:
                if isinstance(entry, tuple):
                    role, output = entry
                    last_outputs += f"\n{role}: {output}"
                else:
                    last_outputs += f"\n{entry}"

            current_prompt = last_outputs
            self.log_prompt(current_prompt)  # Log the updated prompt

            # Generate responses from preserver and destroyer
            preserver_output = self.preserver.generate_preservation(current_prompt)
            self.log_conversation("", preserver_output)
            current_prompt += f"\n{preserver_output}"

            destroyer_output = self.destroyer.generate_destruction(current_prompt)
            self.log_conversation("", destroyer_output)
            current_prompt += f"\n{destroyer_output}"

            # Update the prompt for the next creator turn
            creator_output = self.creator.generate_idea(current_prompt)
            self.log_conversation("", creator_output)
            current_prompt += f"\n{creator_output}"

            # Break the loop after a set conversation length (adjust as needed)
            if len(self.conversation_history) >= 20:  # Example: Break after 20 conversation entries
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