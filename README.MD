# Timer Bot

This project contains a Telegram messaging bot. The bot sets a timer based on user input and displays a visual progress bar in the chat that updates every second until the timer expires.

## Installation

1. Get your Telegram API key by creating a new bot using [BotFather](https://core.telegram.org/bots#botfather).
2. Clone the repository and create a `.env` file in the project root directory with the following content:

`TELEGRAM_BOT_TOKEN=your_telegram_bot_token`\
`TELEGRAM_CHAT_ID=your telegram chat_id`

3. Python3 must be installed on your computer. Then use `pip` (or `pip3` if there is a conflict with Python2) to install the dependencies:

`pip install -r requirements.txt`

## Launch bot

To start the bot, run:

`python main.py`

While chatting with your bot, send a message containing the length of time (for example, "30s" - 30 seconds, "10m" - 10 minutes, "1h" - 1 hour). The bot will then start a timer and send a message with a progress bar that will update every second.

When the timer ends, the bot will send a “Time Up” message.

## Project structure

The project consists of two main files:

- `ptbot.py` - contains the Bot class, which provides methods for sending and updating messages, creating timers and countdowns, and starting the bot.

- `main.py` - Contains the main logic of the bot, including callback functions for processing user input and notifying users when time has expired. The file also contains the render_progressbar function, which creates a visual progress bar for the timer.

## Objective of the project

This project was written for educational purposes for the dvmn.org online web developer course.