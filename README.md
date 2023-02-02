# Discord GPA Bot
This is a Discord Bot built with Python that scrapes University websites to get GPA information with the `/gpa` command.

## Features
- Login securely to your university website with `/adduser`
- Easily check your semester GPA with `/gpa`
- View your current semester GPA and cumulative GPA

## Requirements
- Python 3+
- [Discord.py](https://discordpy.readthedocs.io/en/latest/)
- [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)

## Installation
1. Clone the repository using the command `git clone https://github.com/apikmeister/umt-discord-bot.git`
2. Install dependencies using the command `pip install -r requirements.txt`
3. Create a .env file in the root folder of the project and add your bot token as `BOT_TOKEN=<your_bot_token>`
4. Run the bot using `python main.py`

## Usage
1. Invite the bot to your server using the OAuth2 URL provided (Coming soon!) in the repository
2. Login to your University website with the `/adduser` command
3. Get your GPA information with the `/gpa` command

## Disclaimer
This repository has no affiliation with Universiti Malaysia Terengganu and is not endorsed by the university or its affiliates and is not responsible for any lawsuit or legal responsibility related to the scraping of data from university websites. The repository is intended for educational purposes only. This code repository is not responsible for any financial or legal consequences resulting from the use of this code repository. We are not liable for any damage or loss of data incurred from the use of this code repository.

We are not responsible for any loss or damage resulting from your use of this repository. We are not responsible for any legal or other repercussions that may result from your use of this repository. By using this repository, you agree to bear all risks associated with the use of this repository.

## License
This project is released under the MIT license. See [LICENSE](https://github.com/apikmeister/umt-discord-bot/blob/master/LICENSE) for more information.
