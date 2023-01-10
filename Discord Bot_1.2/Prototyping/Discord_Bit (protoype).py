
import discord
import random
import json
import os
from discord.ext.commands import Bot
from discord_components import *
from discord.ext import commands
from asyncio import TimeoutError

bot = commands.Bot(command_prefix='g-')
bot.remove_command("help")

print("Starting Bot...")
@bot.event
async def on_ready():
    DiscordComponents(bot)
    print("Bot is ready")
    print(f"Logged in as {bot.user}")

#Documentations
#https://www.youtube.com/watch?v=Vr3wuXrT_pk
#https://github.com/Datavorous/dat-is-for-discord/blob/main/ButtonGames/rps.py
#https://github.com/SilentJungle399/discord_buttons_plugin


#====-Help-====
@bot.group(invoke_without_command=True)
async def help(ctx):
    help_em = discord.Embed(
       title = "**Help for FuryX DiscBOX Gaming Bot**", description = "Here are all the features and commands avaiable in `Alpha` Version",
       color= discord.Color.red())
    help_em.add_field(
        name = "**How do you play ?**", 
        value = "This bot includes Chat-based-storymode games, where the charecters will be controled by the user using the chat, the user's desions will shape how the story moves on...\n\n To start a game use the Game Launcher")
    help_em.add_field(name="**⨊ G-XP**", value = "This is a in-game rewarding system, can be used for upgrading RIG hardware, *(more usese coming soon...)*\n\n Can be invoked by- `g-xp`, `g-gxp`, `g-G-XP`, `g-my xp`")
    help_em.add_field(name="**My Rig", value = "Your Virtual-PC-Bulid, get PC components from the PC Shop using G-XP, and upgrade them to get experices each upgrade's unique advantages and features!")
    await ctx.send(embed = help_em)

    #===-G-XP_Help-===
@help.command(aliases = ["gxp", "G-XP", "my xp"])
async def xp(ctx):
    gxp_em = discord.Embed(title="**Help for ⨊ G-XP**", description = "This is a in-game rewarding system, can be used for upgrading RIG hardware, *(more uses coming soon...)*\n")
    gxp_em.add_field(name = "**Commands**", value = "Check your G-XP - `g-gxp`, `g-my xp` ")
    gxp_em.add_field(name = "**How to Earn G-XP**", value = "You can earn G-XPs by playing games")
    gxp_em.add_field(name = "**Rewarding Scheam**", value = "Game Rewards- after completing 1 Game, yoour reward depends on the game, factors that dictate your reward inculded the Duration of the game(longer the)")
    await ctx.send(embed = gxp_em)
    #=================

    #===-My-Rig_Help
@help.command(aliases = ["rig","my rig", "pc"])
async def rig_help(ctx):
    rig_help = discord.Embed(title="**Help for My Rig", description = "Your Virtual-PC-Bulid, get PC components from the PC Shop using your G-XP, and upgrade them to get experices each upgrade's unique advantages and features!\n")
    rig_help.add_field(name = "**Commands**", value = "Check your Inventory- `")
    rig_help.add_field(name = "**How to Earn G-XP**", value = "You can earn G-XPs by playing games")
    rig_help.add_field(name = "**Rewarding Scheam**", value = "Game Rewards- after completing 1 Game, yoour reward depends on the game, factors that dictate your reward inculded the Duration of the game(longer the)")

#================

#========-DashBoard-=========
@bot.command(aliases=["dashboard", "board", "main menue", "menu"])
async def dash(ctx):
    dash_em = discord.Embed(title = "**Welcome to FuryX DiscBOX Gaming Bot**", description = "This is your dashboard for DiscBOX!\n\n (*NOTE:Devolopment is stil in progress, few features may not work as intended*)")
    dash_em.add_field(name = "**How do you play ?**", value = "This bot inculed Chat-based-storymode games, where the charecters will be controled by the user using the chat, the user's desions will shape hw the story moves on...\n\n To start a game use the Game Launcher")
    dash_em.add_field(name="**⨊ G-XP**", value = "This is a in-game rewarding system, can be used for upgrading RIG hardware, *(more uses coming soon...)*\n\n **Can be invoked by**-\n `g-xp`, `g-gxp`, `g-G-XP`, `g-my xp`")
    dash_em.add_field(name="**Game Launcher**", value = "All in one laucher for all your games ...")
    dash_em.add_field(name="**My RIG**", value = "Your Virtual-PC bulid,(*This is a Virtual PC Build my not accurately represent real life PC Bulids*)\n\n **To open your rig**-\n `g-rig`, `g-inv`, g-`build`\n")

    await ctx.send(
        embed = dash_em,
        components=[[Button(style=4, label="Help", custom_id = "hlep"),Button(style=4, label="⨊ G-XP", custom_id = "xp"),Button(style=ButtonStyle.red, label="My RIG", custom_id = "rig"),Button(style=ButtonStyle.red, label="Game Laucher", custom_id = "gl")]])
    
#===-Dashboard_Embeds-===
    #===-Help_embed-====    
    dash_help_em = discord.Embed(
       title = "**Help for FuryX DiscBOX Gaming Bot**", description = "Here are all the features and commands avaiable in `Alpha` Version",
       color= discord.Color.red())
    dash_help_em.add_field(
        name = "**How do you play ?**", 
        value = "This bot includes Chat-based-storymode games, where the charecters will be controled by the user using the chat, the user's desions will shape how the story moves on...\n\n To start a game use the Game Launcher")
    dash_help_em.add_field(name="**⨊ G-XP**", value = "This is a in-game rewarding system, can be used for upgrading RIG hardware, *(more uses coming soon...)*\n\n **Can be invoked by**-\n `g-xp`, `g-gxp`, `g-G-XP`, `g-my xp`")
    dash_help_em.add_field(name="**My Rig**", value = "Your Virtual-PC bulid,(*This is a Virtual PC Build my not accurately represent real life PC Bulids*)\n\n **To open your rig**-\n `g-rig`, `g-inv`, `g-build`\n")
    #====================

    #===-G-XP_embed===
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    xp_am = users[str(user.id)]["xp"]
    xp_amt = str(xp_am)
    gxp_em = discord.Embed(title="**My ⨊ G-XP**", color= discord.Color.red())
    gxp_em.add_field(name = f"G-XP Earned by {ctx.author}", value = '**⨊ **' + xp_amt)
    #=================

    #===-Game_Launcher_embed===
    gl_em = discord.Embed(title="**DiscBOX Game-Launcher**", description = "**Your games:**\n -N/A-", color= discord.Color.red())
    gl_em.add_field(name="Progress (%)", value = "-N/A-")
    #==========================

    #===-My_rig_embed===
    
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    rig_em = discord.Embed(title = "My Inventory", description = "All the PC Componets you have brought in one place:-", color = discord.Color.red())
    for item in bag:
        rig_em.add_field(name = f"{item}", value="------", inline=False)  

    #===================

    #===-DashBoard_Reply-===-
    while True:
        def check(res):
            return ctx.author == res.user and res.channel == ctx.channel

        res = await bot.wait_for("button_click", check=check)
        player = res.component.label

        try:
            if player in "Help":
                await res.respond(
                    embed = dash_help_em)
                    
                    
            elif player in "⨊ G-XP":
                await res.respond(
                    embed = gxp_em)

            elif player in "Game Laucher":
                await res.respond(
                    embed = rig_em)

            elif player in "My RIG":
               await res.respond(
                    embed = rig_em,
                    components=[Button(style=4, label="Shop", custom_id = "Shop")])

               res = await bot.wait_for("button_click", check=check)
               player = res.component.label

               try:
                   if player in "Shop":
                       em = discord.Embed(title = "Shop", 
                       description  = "Available PC hardware for your rig, Upgrade your rig to have a better expercise, each upgrade comes with it's own features and advantages", 
                       color= discord.Color.red())

                       for item in mainshop_for_shop:
                           name = item["name"]
                           price = item["price"]
                           desc = item["description"]
                           em.add_field(name = name, value = f"⨊ {price} | {desc}")

                       await ctx.send(embed = em)

               except:
                   break

        except TimeoutError:
            print("DASHBOARD NOT USED!- TimeoutError")
#===========================

#=====-G-XP-=====
@bot.command(aliases = ["gxp", "my xp", "bal"])
async def xp(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    xp_am = users[str(user.id)]["xp"]
    xp_amt = str(xp_am)


    gxp_em = discord.Embed(title="**My ⨊ G-XP**", color= discord.Color.red())
    gxp_em.add_field(name = f"G-XP Earned by {ctx.author}", value = '**⨊ **' + xp_amt)

    await ctx.send(embed = gxp_em)



async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)]  = {}
        users[str(user.id)]["xp"] = 1000

    with open ("database//user_gxp.json", "w") as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    with open("database//user_gxp.json", "r") as f:
        users = json.load(f)
    return users

async def update_bank(user,change = 0, mode = "xp"):
    users = await get_bank_data()
    users[str(user.id)][mode] += change

    with open ("database//user_gxp.json", "w") as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["xp"]]
    return bal

#===============

#====-My_Rigs-====

mainshop_for_shop = [{
    #=====-CPUs-=====
    "name":"<:ryzen:867354626716991498> Ryzen-9-5900X",
    "price":699,
    "description":"16C/32T"
    },
    {
        "name":"<:ryzen:867354626716991498> Ryzen-7-5800X",
        "price":449,
        "description":"8C/16T"
    },
    {
        "name":"<:ryzen:867354626716991498> Ryzen-5-5600X",
        "price":299,
        "description":"6C/12t"
    },
    {
        "name":"<:i9:867353861324800040> Intel-i9-11900K",
        "price":549,
        "description":"8C/16T"
    },
    {
        "name":"<:i7:867353861819727882> Intel-i7-11700K",
        "price":399,
        "description":"8C/16t"
    },
    {
        "name":"<:i5:867353861885788200> Intel-i5-11600K",
        "price":299,
        "description":"6C/12t"
    },
    {
    #=====-Graphics_Cards-====
        "name":"<:nvidi:867353861752750132> Nvidia-RTX-3080-Ti",
        "price":945,
        "description":"12 GB GDDR6X/Bclock ~ 1.67 GHz"
    },
    {
        "name":"<:nvidi:867353861752750132> Nvidia-RTX-3070-Ti",
        "price":899 ,
        "description":"8 GB GDDR6X/Bclock ~ 1.71 GHz"
    },
    {
        "name":"<:nvidi:867353861752750132> Nvidia-RTX-3060-Ti",
        "price":415,
        "description":"8 GB GDDR6X/Bclock ~ 1.71 GHz"
    },
    #=====-Motherborads-=====
    {
        "name":"<:asus:867353861471731713> Asus-ROG-X570-Crosshair-VIII",
        "price":739,
        "description":"AM4 Socket"
    },
    {
        "name":"<:asus:867353861471731713> Asus-TUF-X570+",
        "price":415,
        "description":"AM4 Socket"
    },
    {
        "name":"<:msi:867353861719064586> MSI-MPG-B550-Edge",
        "price":309,
        "description":"AM4 Socket"
    },
    {
        "name":"<:asus:867353861471731713> ASUS-ROG-Maximus-XIII-H",
        "price":729,
        "description":"LGA 1200 Socket"
    },
    {
        "name":"<:aorus:867356930677932032> Gigabyte-Z590-AORUS-ELITE-AX",
        "price":436,
        "description":"LGA 1200 Socket"
    },
    {
        "name":"<:asrock:867353861353504788> ASRock-B560-Steel-Legend",
        "price":299,
        "description":"LGA 1200 Socket"
    },

        ]

mainshop_for_buy = [{
    #=====-CPUs-=====
    "name":"Ryzen-9-5900X",
    "price":699,
    "description":"16C/32T"
    },
    {
        "name":"Ryzen-7-5800X",
        "price":449,
        "description":"8C/16T"
    },
    {
        "name":"Ryzen-5-5600X",
        "price":299,
        "description":"6C/12t"
    },
    {
        "name":"Intel-i9-11900K",
        "price":549,
        "description":"8C/16T"
    },
    {
        "name":"Intel-i7-11700K",
        "price":399,
        "description":"8C/16t"
    },
    {
        "name":"Intel-i5-11600K",
        "price":299,
        "description":"6C/12t"
    },
    {
    #=====-Graphics_Cards-====
        "name":"Nvidia-RTX-3080-Ti",
        "price":945,
        "description":"12 GB GDDR6X/Bclock ~ 1.67 GHz"
    },
    {
        "name":"Nvidia-RTX-3070-Ti",
        "price":899 ,
        "description":"8 GB GDDR6X/Bclock ~ 1.71 GHz"
    },
    {
        "name":"Nvidia-RTX-3060-Ti",
        "price":415,
        "description":"8 GB GDDR6X/Bclock ~ 1.71 GHz"
    },
    #=====-Motherborads-=====
    {
        "name":"Asus-ROG-X570-Crosshair-VIII",
        "price":739,
        "description":"AM4 Socket"
    },
    {
        "name":"Asus-TUF-X570+",
        "price":415,
        "description":"AM4 Socket"
    },
    {
        "name":"MSI-MPG-B550-Edge",
        "price":309,
        "description":"AM4 Socket"
    },
    {
        "name":"ASUS-ROG-Maximus-XIII-H",
        "price":729,
        "description":"LGA 1200 Socket"
    },
    {
        "name":"Gigabyte-Z590-AORUS-ELITE-AX",
        "price":436,
        "description":"LGA 1200 Socket"
    },
    {
        "name":"ASRock-B560-Steel-Legend",
        "price":299,
        "description":"LGA 1200 Socket"
    },

        ]
     

@bot.command(aliases = ["shop", "rigshop", "pc shop"])
async def pc_shop(ctx):
    em = discord.Embed(title = "Shop", 
                       description  = "Available PC hardware for your rig, Upgrade your rig to have a better expercise, each upgrade comes with it's own features and advantages", 
                       color= discord.Color.red())

    for item in mainshop_for_shop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"⨊ {price} | {desc}")


    await ctx.send(embed = em)



@bot.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send(embed = discord.Embed(title = "That Object isn't there!", color = discord.Color.red()))
            return
        if res[1]==2:
            await ctx.send(embed = discord.Embed(title = f"You don't have enough money in your wallet to buy {amount} {item}", color = discord.Color.red()))
            return
        if res[1]==3:
            await ctx.send(embed = discord.Embed(title = f"You already own a {item}!", color = discord.Color.red()))
            return

    await ctx.send(embed = discord.Embed(title = f"You just bought {amount} {item}"))

@bot.command(aliases = ["inv", "bulid", "rig"])
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    em = discord.Embed(title = "My Inventory", description = "All the PC Componets you have brought in one place:-", color = discord.Color.red())
    for item in bag:
        em.add_field(name = f"{item}", value="------", inline=False)    

    await ctx.send(embed = em)
    
async def buy_this(user,item_name,amount):
    with open("database//user_gxp.json","r") as f:
        json.load(f)

    item_name_lowerd = item_name.lower()
    name_ = None
    for item in mainshop_for_buy:
        name = item["name"].lower()
        if name == item_name_lowerd:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]       

    try:
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                return [False,3]
                break

        if t == None:
            obj = item_name
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = item_name
        users[str(user.id)]["bag"].append(obj)
        
        
    with open("database//user_gxp.json","w") as f:
        json.dump(users,f) 

    await update_bank(user,cost*-1,"xp")

    return [True,"Worked"]

@bot.command()
async def sell(ctx,item):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {item}.")

async def sell_this(user,item_name,price = None):
    item_name_lowered = item_name.lower()
    name_ = None
    for item in mainshop_for_buy:
        name = item["name"].lower()
        if name == item_name_lowered:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*1

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                obj = users[str(user.id)]["bag"]
                del obj[obj.index(item_name)]
                t = 1
                break
            index+=1 
        if t == None:   
            return [False,3]
    except:
        obj = users[str(user.id)]["bag"]
        del obj[obj.index(item_name)]
        

    with open("database//user_gxp.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"xp")

    return [True,"Worked"]



bot.run("STOH5tRUYjQJfQDWZu4NO6qw__A2dPCY")