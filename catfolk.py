catfolk

from disco.bot import Bot, Plugin


class SimplePlugin(Plugin):
    
    @Plugin.listen('ChannelCreate')
    def on_channel_create(self, event):
        event.channel.send_message('Woah, a new channel huh!')

    
    @Plugin.command('ping')
    def on_ping_command(self, event):
        event.msg.reply('Pong!')

    @Plugin.command('echo', '<content:str...>')
    def on_echo_command(self, event, content):
        event.msg.reply(content)


@Plugin.command('/flip')
def on_ping_command(self, event):
    event.msg.reply('You just flipped one card and gained one point! (the result will randomize in the future!)')


    @Plugin_command('/wot')
    def on_ping_command(self, event):
        event.msg.reply('I do not get this but this sounds cool')


