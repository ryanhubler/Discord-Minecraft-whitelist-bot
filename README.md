# DISCORD-MINECRAFT-WHITELIST-BOT

DISCORD-MINECRAFT-WHITELIST-BOT is discord bot that will allow discord users to whitelist themselves.

## Installation and Dependency's 

Clone the repository
```
git clone https://github.com/ryanhubler/Discord-Minecraft-whitelist-bot.git
```
Install dependency's 
```bash
pip3 install mcrcon
```
## Seting up rcon on your minecraft server
1. In your mincecraft servers files a file called server.properties in this file there are two line you will need to change.
```
rcon.password= <PUT A STRONG PASSWORD HERE YOU WILL NEED IT LATER>
```
```
enable-rcon=true
```
## Usage
1. To use the bot in discord you must create a bot in the discord developer portal and add its token to this line
```python
TOKEN = 'YOUR TOKEN GOES HERE'
````
2. Adding your hostname (server address or url) and your strong password from earlier
```python
with MCRcon("HOSTNAMEOFMCSERVER", "PASSWORDGOESHERE") as mcr: #send the whitelist command to minecraft server
```
3. Once your bot is in discord run main.py
4. Then in discord use ```#whitelist <Minecraft Username>``` 
5. The default prefix ```#``` can be changed by changing this line 
```python
bot = commands.Bot(command_prefix='#', help_command=None) #sets your prefix
``` 

## License
[MIT](https://choosealicense.com/licenses/mit/)
