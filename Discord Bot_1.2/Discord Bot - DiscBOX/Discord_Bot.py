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

#Documentations
#https://www.youtube.com/watch?v=Vr3wuXrT_pk
#https://github.com/Datavorous/dat-is-for-discord/blob/main/ButtonGames/rps.py
#https://github.com/SilentJungle399/discord_buttons_plugin

#==========Starting bot==========
print("Starting Bot...")
@bot.event
async def on_ready():
    DiscordComponents(bot)
    print("Bot is ready")
    print(f"Logged in as {bot.user}")
#================================

#======================Help=========================
@bot.group(invoke_without_command=True)
async def help(ctx):
    help_em = discord.Embed(
       title = "**Help for FuryX DiscBOX Gaming Bot**", description = "Here are all the features and commands avaiable in `Alpha` Version" ,
       color= discord.Color.red())
    help_em.add_field(
        name = "**How do you play ?**", 
        value = "This bot includes Chat-based-storymode games, where the charecters will be controled by the user using the chat, the user's desions will shape how the story moves on...\n\n To start a game use the Game Launcher")
    help_em.add_field(name="**⨊ G-XP**", value = "This is a in-game rewarding system, can be used for upgrading RIG hardware, *(more usese coming soon...)*\n\n Can be invoked by- `g-xp`, `g-gxp`, `g-G-XP`, `g-my xp`")
    help_em.add_field(name="**My Rig", value = "Your Virtual-PC-Bulid, get PC components from the PC Shop using G-XP, and upgrade them to get experices each upgrade's unique advantages and features!")
    await ctx.reply(embed = help_em)

    #================G-XP_HELP=================
@help.command(aliases = ["gxp", "G-XP", "my xp"])
async def xp(ctx):
    gxp_em = discord.Embed(title="**Help for ⨊ G-XP**", description = "This is a in-game rewarding system, can be used for upgrading RIG hardware, *(more uses coming soon...)*\n")
    gxp_em.add_field(name = "**Commands**", value = "Check your G-XP - `g-gxp`, `g-my xp` ")
    gxp_em.add_field(name = "**How to Earn G-XP**", value = "You can earn G-XPs by playing games")
    gxp_em.add_field(name = "**Rewarding Scheam**", value = "Game Rewards- after completing 1 Game, yoour reward depends on the game, factors that dictate your reward inculded the Duration of the game(longer the)")
    await ctx.reply(embed = gxp_em)
    #===========================================

    #================MY-RIG_HELP=================
@help.command(aliases = ["rig","my rig", "pc"])
async def rig_help(ctx):
    rig_help = discord.Embed(title="**Help for My Rig", description = "Your Virtual-PC-Bulid, get PC components from the PC Shop using your G-XP, and upgrade them to get experices each upgrade's unique advantages and features!\n")
    rig_help.add_field(name = "**Commands**", value = "Check your Inventory- `")
    rig_help.add_field(name = "**How to Earn G-XP**", value = "You can earn G-XPs by playing games")
    rig_help.add_field(name = "**Rewarding Scheam**", value = "Game Rewards- after completing 1 Game, yoour reward depends on the game, factors that dictate your reward inculded the Duration of the game(longer the)")
    await ctx.reply(embed = rig_help)
    #============================================

#===================================================


#======================DASHBOARD=========================
@bot.command(aliases=["dashboard", "board", "main menue", "menu"])
async def dash(ctx):
    dash_em = discord.Embed(title = "**Welcome to FuryX DiscBOX Gaming Bot**", description = "This is your dashboard for DiscBOX!\n\n (*NOTE:Devolopment is stil in progress, few features may not work as intended*)")
    dash_em.add_field(name = "**How do you play ?**", value = "This bot inculed Chat-based-storymode games, where the charecters will be controled by the user using the chat, the user's desions will shape hw the story moves on...\n\n To start a game use the Game Launcher")
    dash_em.add_field(name="**⨊ G-XP**", value = "This is a in-game rewarding system, can be used for upgrading RIG hardware, *(more uses coming soon...)*\n\n **Can be invoked by**-\n `g-xp`, `g-gxp`, `g-G-XP`, `g-my xp`")
    dash_em.add_field(name="**Game Launcher**", value = "All in one laucher for all your games ...")
    dash_em.add_field(name="**My RIG**", value = "Your Virtual-PC bulid,(*This is a Virtual PC Build my not accurately represent real life PC Bulids*)\n\n **To open your rig**-\n `g-rig`, `g-inv`, g-`build`\n")

    await ctx.send(
        embed = dash_em,
        components=[
            [Button(style=4, label="Help", custom_id = "hlep"),
             Button(style=4, label="⨊ G-XP", custom_id = "xp"),
             Button(style=ButtonStyle.red, label="My RIG", custom_id = "rig"),
             Button(style=ButtonStyle.red, label="Game Laucher", custom_id = "gl")]
            ]
        )

    #===============DASH-LEVEL2_EMBED==============

    #===============HELP_EMBED==================
    dash_help_em = discord.Embed(
       title = "**Help for FuryX DiscBOX Gaming Bot**", description = "Here are all the features and commands avaiable in `Alpha` Version",
       color= discord.Color.red())
    dash_help_em.add_field(
        name = "**How do you play ?**", 
        value = "This bot includes Chat-based-storymode games, where the charecters will be controled by the user using the chat, the user's desions will shape how the story moves on...\n\n To start a game use the Game Launcher")
    dash_help_em.add_field(name="**⨊ G-XP**", 
                           value = "This is a in-game rewarding system, can be used for upgrading RIG hardware, *(more uses coming soon...)*\n\n **Can be invoked by**-\n `g-xp`, `g-gxp`, `g-G-XP`, `g-my xp`")

    dash_help_em.add_field(name="**My Rig**", 
                           value = "Your Virtual-PC bulid,(*This is a Virtual PC Build my not accurately represent real life PC Bulids*)\n\n **To open your rig**-\n `g-rig`, `g-inv`, `g-build`\n")
    #============================================

    #===============GXP_EMBED====================
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    xp_am = users[str(user.id)]["xp"]
    xp_amt = str(xp_am)
    gxp_em = discord.Embed(title="**My ⨊ G-XP**", color= discord.Color.red())
    gxp_em.add_field(name = f"G-XP Earned by {ctx.author}", value = '**⨊ **' + xp_amt)
    #============================================

        #===-Game_Launcher_embed===
    gl_em = discord.Embed(title="**DiscBOX Game-Launcher**", description = "**Your games:**\n -N/A-", color= discord.Color.red())
    gl_em.add_field(name="Progress (%)", value = "-N/A-")
    #==========================

    #===============MY-RIG_EMBED=================
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

    #============================================

#======================DASHBOARD_BUTTON_EVENTS=========================
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
#============================================================================================


#======================GXP_MAIN=========================
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
#===================================================

#======================MY_RIG_MAIN=========================

    #====================DATA-ACCSES-FEED========================
with open("C:\Programming\_Projects\Visual Studio Projects\_On-Going\Discord Bot_1.2\Discord Bot - DiscBOX\database\mainshopforbuy.json", "r") as f:
        mainshop_for_buy = json.load(f)

with open("C:\Programming\_Projects\Visual Studio Projects\_On-Going\Discord Bot_1.2\Discord Bot - DiscBOX\database\mainshopforshop.json", "r") as f2:
        mainshop_for_shop = json.load(f2)
    #============================================================

    #====================DATA-ACCSES-FEED========================

    #====================SHOP-DISPLAY========================
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
    #======================================================================================================

    #====================BUY-COMMAND========================

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

    #=========================================================================================

    #====================BAG-COMMAND========================

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
    #====================================================================================

#====================BUY-THIS-BG-COMMAND==================================

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
#=============================================================================

#===============================SELL-COMMAND============================
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
#=======================================================================

#===============================SELL-THIS-BG-COMMAND============================
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
#=====================================================================
#jdjjdwdjwijije

bot.run()
