# Rule-Based Chatbot

A simple yet effective rule-based chatbot implemented in Python that responds to user input with predefined responses based on pattern matching.

## Overview

This chatbot uses a straightforward rule-based approach to understand and respond to user queries. It analyzes user input for specific keywords and phrases, then provides appropriate responses from a predefined set of rules.

## Features

- **Simple Rule-Based Pattern Matching**: Uses basic conditional logic to identify user intents
- **Predefined Responses**: Maintains a set of responses for common user inputs
- **Interactive Console Interface**: Runs as a command-line application for easy interaction
- **Exit Functionality**: Allows users to gracefully exit the conversation
- **Keyword Detection**: Recognizes common greetings, questions, and requests

## Requirements

- Python 3.x
- No external dependencies required

## Installation

Clone the repository:

```bash
git clone https://github.com/ritvikvr/rule-based-chatbot.git
cd rule-based-chatbot
```

## Usage

Run the chatbot:

```bash
python chatbot.py
```

The chatbot will start with a welcome message:
```
💬 Chatbot: Hello! Type 'bye' to exit.
```

Then you can interact with it by typing messages:

```
You: hello
💬 Chatbot: Hello there!

You: how are you
💬 Chatbot: I'm doing great!

You: name
💬 Chatbot: I'm your assistant chatbot.

You: help
💬 Chatbot: I can respond to greetings and simple questions.

You: bye
💬 Chatbot: Goodbye!
```

## How It Works

The chatbot operates using a simple rule-based system:

1. **Input Reception**: Waits for user input and converts it to lowercase for consistency
2. **Pattern Matching**: Checks if the input contains specific keywords
3. **Response Selection**: Returns the corresponding predefined response
4. **Default Response**: If no pattern matches, returns a default "I don't understand" message

### Recognized Patterns

| User Input (Pattern) | Chatbot Response |
|---|---|
| "hello" or "hi" | "Hello there!" |
| "how are you" | "I'm doing great!" |
| "name" | "I'm your assistant chatbot." |
| "help" | "I can respond to greetings and simple questions." |
| "bye" | "Goodbye!" (and exits) |
| Other | "I don't understand that yet." |

## Project Structure

```
rule-based-chatbot/
├── chatbot.py      # Main chatbot implementation
└── README.md       # Documentation (this file)
```

## Code Example

The core logic of the chatbot:

```python
while True:
    user_input = input("You: ").lower()
    
    if "hello" in user_input or "hi" in user_input:
        print("💬 Chatbot: Hello there!")
    elif "how are you" in user_input:
        print("💬 Chatbot: I'm doing great!")
    elif "name" in user_input:
        print("💬 Chatbot: I'm your assistant chatbot.")
    elif "help" in user_input:
        print("💬 Chatbot: I can respond to greetings and simple questions.")
    elif "bye" in user_input:
        print("💬 Chatbot: Goodbye!")
        break
    else:
        print("💬 Chatbot: I don't understand that yet.")
```

## Future Enhancements

Potential improvements for this project:

- **Machine Learning Integration**: Implement NLP with libraries like NLTK or spaCy
- **Context Memory**: Remember conversation history for better responses
- **Expanded Knowledge Base**: Add more patterns and responses
- **Sentiment Analysis**: Analyze user sentiment to tailor responses
- **Intent Recognition**: Use more sophisticated NLP for intent classification
- **Database Integration**: Store and retrieve user interactions
- **GUI Interface**: Create a graphical user interface for easier interaction

## Limitations

- **No Natural Language Understanding**: Simple keyword matching, not true NLP
- **Limited Context**: Cannot remember previous conversations
- **Rigid Patterns**: Doesn't handle variations in phrasing well
- **No Learning**: Cannot improve from user interactions
- **Limited Scope**: Only handles predefined patterns

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## Author

**Ritvik** (@ritvikvr)

## License

This project is open source and available under the MIT License.

## Disclaimer

This is a basic educational project demonstrating fundamental chatbot concepts. For production-level chatbots, consider using advanced NLP frameworks and machine learning models.

## Contact

For questions or suggestions, feel free to open an issue on GitHub.

---

**Happy Chatting! 💬**
