import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum! Eğer geri dönüşüm hakkında bilgi istiyorsan tam yerindesin.')
@bot.command()
async def plastik_el_isi(ctx):
    fikirler = [
        "1031 - Japonya'da ilk kez kağıt geri dönüştürülmeye başlandı.",
        "1800'ler - ABD'deki eski kıyafetler malzemesi olarak geri dönüştürüldü.",
        "1970 - İlk Dünya Günü'nün kutlanması, geri dönüşüm bilincini artırdı.",
        "1983 - Almanya, Yeşil Nokta Sistemi ile ambalajların geri dönüştürülmesini zorunlu hale getirdi."
        "1990'lar - E-atık geri",
        "2020 - AB, tek küresel plastiklerin yasaklanması için yeni politikalar başlattı."
    ]
    await ctx.send(f"Tarihleriyle birlikte özel bilgiler:\n- " + "\n- ".join(fikirler))


bot.run("token")
