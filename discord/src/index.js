const { Client, Events, GatewayIntentBits } = require('discord.js');
const dotenv = require('dotenv');

dotenv.config();

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
    ],
});

client.once(Events.ClientReady, (instance) => {
    console.info(`Logged in as ${instance.user.tag}`);
});

client.on(Events.MessageCreate, async (message) => {});

client.on(Events.MessageDelete, async (message) => {});

client.on(Events.GuildCreate, async (guild) => {});

client.on(Events.GuildDelete, async (guild) => {});

const token = process.env.DISCORD_TOKEN;
client.login(token);
