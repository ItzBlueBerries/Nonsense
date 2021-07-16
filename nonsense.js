const Discord = require("discord.js");
const nonsense = new Discord.Client({disableEveryone: true});
const nonsenseConfig = require('./nonsense.json');

// .Env Stop Lol DotEnvvv
require('dotenv').config()

nonsense.commands = new Discord.Collection();
nonsense.aliases = new Discord.Collection();

["command"].forEach(handler => {
  require(`./handlers/${handler}`)(nonsense)
})

nonsense.on("ready", async () => {
    console.log(`${nonsense.user.username} is online.`)
    status = `What are you? What am I? | n?help`
      nonsense.user.setStatus('idle');
      nonsense.user.setActivity(status, {type: "PLAYING"});
})

nonsense.on("message", async message => {
    if(message.author.nonsense || message.channel.type === "dm") return;

    if(!message.guild) return;
    if(nonsenseConfig.NONSENSE_PREFIX === null) PREFIX = nonsenseConfig.NONSENSE_PREFIX
    
    
    if(!message.content.startsWith(nonsenseConfig.NONSENSE_PREFIX)) return;
    
        // If message.member is uncached, cache it.
      if (!message.member) message.member = await message.guild.fetchMember(message);
  
      const args = message.content.slice(nonsenseConfig.NONSENSE_PREFIX.length).trim().split(/ +/g);
      const cmd = args.shift().toLowerCase();
      
      if (cmd.length === 0) return;
      
      // Get the command
      let command = nonsense.commands.get(cmd);
      // If none is found, try to find it by alias
      if (!command) command = nonsense.commands.get(nonsense.aliases.get(cmd));
  
      // If a command is finally found, run the command
      if (command) 
       command.run(nonsense, message, args);
    
    
   })

nonsense.login(nonsenseConfig.NONSENSE_TOKEN);