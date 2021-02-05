import discord
token = 'Nzk3NzAyNjM1MzM5MjUxNzYy.X_qUeA.rN9wvtxDmKYgIwIzqPApv6RQ9w8'
client = discord.Client()
@client.event
async def on_ready():
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    game = discord.Game('『당신의 오늘은 어떤가요?』질문')
    await client.change_presence(status=discord.Status.online, activity=game)
    print('====================================')

client.run(token)
