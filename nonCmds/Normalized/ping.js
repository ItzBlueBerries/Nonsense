module.exports = {
    name: "ping",
    category: "Normalized",
    description: "Just a ping command for mostly testing.",
    usage: "ping",
    nonsenseLevel: "0",
    run: async (nonsense, message, args) => {
        message.channel.send(`Uh...\n**${nonsense.ws.ping}ms**`)
        return
    }
}