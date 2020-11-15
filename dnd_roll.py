    ###### D&D 5E Simple random character generator #########

import random as ran

###spellbook

#wizard's spells
#lv 0
w_0_spells = ['acid splash','blade ward','chill touch','dancing lights','fire bolt','light',
            'mage hand','message','minor ilusion','prestidigitation','ray of frost','shocking grasp']
#lv1
w_1_spells=['absorb elements','alarm','burning hands','charm person','cause fear','charm person',
            'chromatic orb','comprehend languages','ice knife','detect magic','feather fall',
            'disguise self','find familiar','mage armor','magic missile','unseen servant','shield','snare']

#cleric's spells
#lv 0
c_0_spells = ['decompose','guidance','hand of radiance','light','mending','resistance','sacred flame',
            'spare of dying','thaumaturgy','toll the dead','word of radiance']
#lv1
c_1_spells=['bane','bless','ceremony','command','create or destroy water','cure wounds','detect evil and good',
            'detect magic','detect poison and disease','guiding bolt','healing word','inflict wounds',
            'protection from evil and good','purify food and water','sanctuary','shield of faith','wrathful smite']

#rogue's 'spells'
#lv 0
r_1_spells = ['expertise','sneak attack',"thieve's cant"]

#fighter's 'spells'
#lv 0
f_1_spells = ['second wind']


#### all names
                            
#elves
elf_male_names = 'Adran, Aelar, Aramil, Arannis, Aust, Beiro, Berrian, Carric, Enialis, Erdan, Erevan, Galinndan, Hadarai, Heian, Himo, Immeral, Ivellios, Laucian, Mindartis, Paelias, Peren, Quarion, Riardon, Rolen, Soveliss, Thamior, Tharivol, Theren, Varis'
elf_female_names = "Adrie, Althaea, Anastrianna, Andraste, Antinua, Bethrynna, Birel, Caelynn, Drusilia, Enna, Felosial, Ielenia, Jelenneth, Keyleth, Leshanna, Lia, Meriele, Mialee, Naivara, Quelenna, Quillathe, Sariel, Shanairra, Shava, Silaqui, Theirastra, Thia, Vadania, Valanthe, Xanaphia"
elf_family_names= "Amakiir (Gemflower), Amastacia (Starflower), Galanodel (Moonwhisper), Holimion (Diamonddew), Ilphelkiir (Gemblossom), Liadon (Silverfrond), Meliamne (Oakenheel), Naïlo (Nightbreeze), Siannodel (Moonbrook), Xiloscient (Goldpetal)"

e_male = elf_male_names.split(sep=", ")
e_female = elf_female_names.split(sep=", ")
e_family = elf_family_names.split(sep=", ")

#humans
human_male_names = 'Darvin, Dorn, Evendur, Gorstag, Grim, Helm, Malark, Morn, Randal, Stedd, Bor, Fodel, Glar, Grigor, Igan, Ivor, Kosef, Mival, Orel, Pavel, Sergor, Ander, Blath, Bran, Frath, Geth, Lander, Luth, Malcer, Stor, Taman, Urth'
human_female_names = 'Amafrey, Betha, Cefrey, Kethra, Mara, Olga, Silifrey, Westra, Alethra, Kara, Katernin, Mara, Natali, Olma, Tana, Zora, Atala, Ceidil, Hama, Jasmal, Meilil, Seipora, Yasheira, Zasheida'
human_family_names = 'Basha, Dumein, Jassan, Khalid, Mostana, Pashar, Rein, Amblecrown, Buckman, Dundragon, Evenwood, Greycastle, Tallstag, Brightwood, Helder, Hornraven, Lackman, Stormwind, Windrivver'

hu_male = human_male_names.split(sep=", ")
hu_female = human_female_names.split(sep=", ")
hu_family = human_family_names.split(sep=", ")

#dwarfs
dwarf_male_names = 'Adrik, Alberich, Baern, Barendd, Brottor, Bruenor, Dain, Darrak, Delg, Eberk, Einkil, Fargrim, Flint, Gardain, Harbek, Kildrak, Morgran, Orsik, Oskar, Rangrim, Rurik, Taklinn, Thoradin, Thorin, Tordek, Traubon, Travok, Ulfgar, Veit, Vondal'
dwarf_female_names = 'Amber, Artin, Audhild, Bardryn, Dagnal, Diesa, Eldeth, Falkrunn, Finellen, Gunnloda, Gurdis, Helja, Hlin, Kathra, Kristryd, Ilde, Liftrasa, Mardred, Riswynn, Sannl, Torbera, Torgga, Vistra'
dwarf_family_names = 'Balderk, Battlehammer, Brawnanvil, Dankil, Fireforge, Frostbeard, Gorunn, Holderhek, Ironfist, Loderr, Lutgehr, Rumnaheim, Strakeln, Torunn, Ungart'

d_male = dwarf_male_names.split(sep=", ")
d_female = dwarf_female_names.split(sep=", ")
d_family = dwarf_family_names.split(sep=", ")

#halflings
halfling_male_names = 'Alton, Ander, Cade, Corrin, Eldon, Errich, Finnan, Garret, Lindal, Lyle, Merric, Milo, Osborn, Perrin, Reed, Roscoe, Wellby'
halfling_female_names = 'Andry, Bree, Callie, Cora, Euphemia, Jillian, Kithri, Lavinia, Lidda, Merla, Nedda, Paela, Portia, Seraphina, Shaena, Trym, Vani, Verna'
halfling_family_names = 'Brushgather, Goodbarrel, Greenbottle, High-hill, Hilltopple, Leagallow, Tealeaf, Thorngage, Tosscobble, Underbough'

ha_male = halfling_male_names.split(sep=", ")
ha_female = halfling_female_names.split(sep=", ")
ha_family = halfling_family_names.split(sep=", ")

m_names =[hu_male,d_male,e_male,ha_male]
f_names = [hu_female,d_female,e_female,ha_female]
family_names = [hu_family,d_family,e_family,ha_family]

#test
stats = ['str','dex','con','wis','int','char']

##########################
#equipment

class simple_weapon():
    def __init__(self,name,bonus,typ):
        self.name=name
        self.bonus = bonus
        self.typ=typ

club = simple_weapon('club','1d4','bludgeoning')
dagger= simple_weapon('dagger','1d4','piercing')
greatclub = simple_weapon('greatclub','1d8','bludgeoning')
handaxe= simple_weapon('handaxe','1d6','slashing')
javelin = simple_weapon('javelin','1d6','piercing')
light_hammer = simple_weapon('light hammer','1d4','bludgeoning')
mace = simple_weapon('mace','1d6','bludgeoning')
quaterstaff= simple_weapon('quaterstaff','1d6','bludgeoning')
sicle = simple_weapon('sicle','1d4','slashing')
spear = simple_weapon('spear','1d6','piercing')


list_simple = [club,dagger,greatclub,handaxe,javelin,light_hammer,mace,quaterstaff,sicle,spear]



#####################################################

class martial_weapon():
    def __init__(self,name,bonus,typ):
        self.name=name
        self.bonus = bonus
        self.typ=typ

battleaxe = martial_weapon('battleaxe','1d8','slashing')
flail= martial_weapon('flail','1d8','bludgeoning')
glaive= martial_weapon('glaive','1d10','slashing')
greataxe= martial_weapon('greataxe','1d12','slashing')
greatsword= martial_weapon('greatsword','2d6','slashing')
halberd= martial_weapon('halberd','1d10','slashing')
lance= martial_weapon('lance','1d12','piercing')
longsword = martial_weapon('Longsword','1d8','slashing')
maul= martial_weapon('maul','2d6','bludgeoning')
morningstar= martial_weapon('morningstar','1d8','piercing')
pike= martial_weapon('pike','1d10','piercing')
rapier= martial_weapon('rapier','1d8','piercing')
scimitar= martial_weapon('scimitar','1d6','slashing')
shortsword= martial_weapon('shortsword','1d6','piercing')
trident= martial_weapon('trident','1d6','piercing')
war_pick= martial_weapon('war pick','1d8','piercing')
warhammer= martial_weapon('warhammer','1d8','bludgeoning')
whip= martial_weapon('whip','1d4','slashing')

list_martial = [battleaxe,flail,glaive,greataxe,greatsword,halberd,lance,longsword,maul,morningstar,pike,rapier,scimitar,shortsword,trident,war_pick,warhammer,whip]


    
#####################################################
    
class s_range_weapon():
    def __init__(self,name,bonus,typ):
        self.name=name
        self.bonus = bonus
        self.typ=typ

light_crossbow=s_range_weapon('light crossbow','1d8','piercing')
dart = s_range_weapon('dart','1d4','piercing')
short_bow=s_range_weapon('short bow','1d6','piercing')
sling = s_range_weapon('sling','1d4','bludgeoning')


list_s_range = [light_crossbow,short_bow,dart,sling]


#####################################################
        
class armor():
    def __init__(self,name,bonus,dex_bonus):
        self.name=name
        self.bonus = bonus
        self.dex_bonus=dex_bonus

chain_mail=armor('chain mail','13',False)
scale_armor =armor('scale armor','14',True)#+dex
leather_armor =armor('leather armor','11',True)#+dex

list_armor = [chain_mail,scale_armor,leather_armor]

   

class rest_eq():
    def __init__(self,name):
        self.name = name

#PACKS
explorer_pack = rest_eq("explorer pack")

priest_pack = rest_eq("priest pack")
buglar_pack = rest_eq("buglar's pack")
dungeoneer_pack = rest_eq("dungeoneer pack")
scholar_pack = rest_eq("scholar's pack")
#other items
shield = rest_eq('shield')
holy_symbol = rest_eq("holy symbol")
spell_book = rest_eq('spell book')
thieves_tools = rest_eq("thieves' tools")
component_pouch = rest_eq("component pouch")
arcane_focus = rest_eq('arcane focus')
#empty
none_eq=rest_eq(" ")

list_rest = [explorer_pack,priest_pack,buglar_pack,dungeoneer_pack,scholar_pack,shield,holy_symbol,spell_book,thieves_tools,component_pouch,arcane_focus]




##########################
#ALIGMENT
############################

###aligment
aligment_f = ['lawful','netural','chaotic']
aligment_s = ['good','neutral']
aligment = {1:ran.choice(aligment_f),2:ran.choice(aligment_s)}



##########################
#Backgrounds
############################


    

class background:
    def __init__(self,bg_name,tool_prof,skill_prof,pt,ideal,bond,flaw):
        self.bg_name = bg_name
        self.tool_prof=tool_prof
        self.skill_prof=skill_prof
        self.pt=pt
        self.ideal=ideal
        self.bond=bond
        self.flaw=flaw

        

#acolyte
aco_pt= ['I idolize a particular hero of my faith, and constantly refer to that person’s deeds and example.',
            'I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.',
            'I see omens in every event and action. The gods try to speak to us, we just need to listen.',
            'Nothing can shake my optimistic attitude.',
            'I quote (or misquote) sacred texts and proverbs in almost every situation.',
            'I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods.',
            'I’ve spent so long in the temple that I have little practical experience dealing with people in the outside world.']
#possible ideal option
aco_ideal_option=[{'id':'Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld','ali':'lawful'},
                    {'id':'Charity. I always try to help those in need, no matter what the personal cost.','ali':'good'},
                    {'id':'Change. We must help bring about the changes the gods are constantly working in the world.','ali':'chaotic'},
                    {'id':'Power. I hope to one day rise to the top of my faith’s religious hierarchy.','ali': 'lawful'},
                    {'id':'Faith. I trust that my deity will guide my actions. I have faith that if I work hard, things will go well.','ali': 'lawful'},
                    {'id':'Aspiration. I seek to prove myself worthy of my god’s favor by matching my actions against his or her teachings.','ali': 'any'}]
aco_ideal_list = []
#check with alligment
for i in aco_ideal_option:
    if (i['ali'] == aligment[1]):
        aco_ideal_list.append(i)
    elif(i['ali'] == aligment[2]):
        aco_ideal_list.append(i)
    elif(i['ali'] == 'any'):
        aco_ideal_list.append(i)
#aco_ideal=ran.choice(aco_ideal_list)

aco_bond=['I would die to recover an ancient relic of my faith that was lost long ago.',
                    'I will someday get revenge on the corrupt temple hierarchy who branded me a heretic'
                    'I owe my life to the priest who took me in when my parents died.',
                    'Everything I do is for the common people.',
                    'I will do anything to protect the temple where I served.',
                    'I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.']
aco_flaw=['I judge others harshly, and myself even more severely.',
                    'I put too much trust in those who wield power within my temple’s hierarchy.',
                    'My piety sometimes leads me to blindly trust those that profess faith in my god.',
                    'I am inflexible in my thinking.',
                    'I am suspicious of strangers and expect the worst of them.',
                    'Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.']
aco_tool = ['none']
aco_skills = ['insight','religion']
# acolyte = background('acolyte',aco_tool,aco_skills,aco_pt,aco_ideal,aco_bond,aco_flaw)

#soldier
sol_pt= ["I’m always polite and respectful.",
                    "I’m haunted by memories of war. I can’t get the images of violence out of my mind.",
                    "I’ve lost too many friends, and I’m slow to make new ones.",
                    "I’m full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.",
                    "I can stare down a hell hound without flinching.",
                    "I enjoy being strong and like breaking things.",
                    "I have a crude sense of humor.",
                    "I face problems head-on. A simple, direct solution is the best path to success."]
#possible ideal option
sol_ideal_option=[{'id':'Greater Good. Our lot is to lay down our lives in defense of others.','ali':'good'},
                    {'id':'Responsibility. I do what I must and obey just authority.','ali':'lawful'},
                    {'id':'Independence. When people follow orders blindly, they embrace a kind of tyranny.','ali':'chaotic'},
                    {'id':'Might. In life as in war, the force wins.','ali': 'neutral'},
                    {'id':'Live and Let Live. Ideals aren’t worth killing over or going to war for.','ali': 'neutral'},
                    {'id':'Nation. My city, nation, or people are all that matter.','ali': 'any'}]
sol_ideal_list = []
#check with alligment
for i in sol_ideal_option:
    if (i['ali'] == aligment[1]):
        sol_ideal_list.append(i)
    elif(i['ali'] == aligment[2]):
        sol_ideal_list.append(i)
    elif(i['ali'] == 'any'):
        sol_ideal_list.append(i)
# sol_ideal=ran.choice(aco_ideal_list)
sol_bond=['I would still lay down my life for the people I served with.',
                    'Someone saved my life on the battlefield. To this day, I will never leave a friend behind.',
                    'My honor is my life.',
                    'I’ll never forget the crushing defeat my company suffered or the enemies who dealt it.',
                    'Those who fight beside me are those worth dying for.',
                    'I fight for those who cannot fight for themselves.']
sol_flaw=['The monstrous enemy we faced in battle still leaves me quivering with fear.',
                    'I have little respect for anyone who is not a proven fighter.',
                    'I made a terrible mistake in battle that cost many lives—and I would do anything to keep that mistake secret.',
                    'My hatred of my enemies is blind and unreasoning.',
                    'I obey the law, even if the law causes misery.',
                    'I’d rather eat my armor than admit when I’m wrong.']
soldier_tool = ['insignia of rank','set of dice']
soldier_skills = ['athletics','intimidation']



#criminal
cri_pt= ['I always have a plan for what to do when things go wrong.',
            'I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.',
            'The first thing I do in a new place is note  the locations of everything valuable—or where such things could be hidden.',
            'I would rather make a new friend than a new enemy.',
            'I am incredibly slow to trust. Those who seem the fairest often have the most to hide.',
            'I don’t pay attention to the risks in a situation. Never tell me the odds.',
            'The best way to get me to do something is to tell me I can’t do it.',
            'I blow up at the slightest insult.']
#possible ideal option
cri_ideal_option=[{'id':'Honor. I don’t steal from others in the trade. ','ali':'lawful'},
                    {'id':'Freedom. Chains are meant to be broken, as are those who would forge them.','ali':'chaotic'},
                    {'id':'Charity. I steal from the wealthy so that I can help people in need. ','ali':'good'},
                    {'id':'Greed. I will do whatever it takes to become wealthy.','ali': 'neutral'},
                    {'id':'People. I’m loyal to my friends, not to any ideals, and everyone else can take a  trip down the Styx for all I care. ','ali': 'neutral'},
                    {'id':'Redemption. There’s a spark of good in everyone.','ali': 'good'}]
cri_ideal_list = []
#check with alligment
for i in cri_ideal_option:
    if (i['ali'] == aligment[1]):
        cri_ideal_list.append(i)
    elif(i['ali'] == aligment[2]):
        cri_ideal_list.append(i)
    elif(i['ali'] == 'any'):
        cri_ideal_list.append(i)
#cri_ideal=ran.choice(aco_ideal_list)
cri_bond=['I’m trying to pay off an old debt I owe to a generous benefactor.',
                    'My ill-gotten gains go to support my family.'
                    'Something important was taken from me, and I aim to steal it back.',
                    'I will become the greatest thief that ever lived.',
                    'I’m guilty of a terrible crime. I hope I can redeem myself for it.',
                    'Someone I loved died because of a mistake I made. That will never happen again.']
cri_flaw=['When I see something valuable, I can’t think about anything but how to steal it.',
                    'When faced with a choice between money and my friends, I usually choose the money.',
                    'If there’s a plan, I’ll forget it. If I don’t forget it, I’ll ignore it.',
                    'I have a “tell” that reveals when I’m lying.',
                    'I turn tail and run when things look bad.',
                    'An innocent person is in prison for a crime that I committed. I’m okay with that.']
criminal_tool = ['disguise kit','forgery kit']
crimnal_skills = ['deception','sleight of hand']





#folk hero
fol_pt= ['I stood up to a tyrant’s agents.',
                    'I saved people during a natural disaster.',
                    'I stood alone against a terrible monster.',
                    'I stole from a corrupt merchant to help the poor.',
                    'I led a militia to fight off an invading army.',
                    'I broke into a tyrant’s castle and stole weapons to arm the people.',
                    'I trained the peasantry to use farm implements as weapons against a tyrant’s soldiers.',
                    'A lord rescinded an unpopular decree after I led a symbolic act of protest against it.',
                    'A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.',
                    'Recruited into a lord’s army, I rose to leadership and was commended for my heroism.']
#possible ideal option
fol_ideal_option=[{'id':'Respect. People deserve to be treated with dignity and respect.','ali':'good'},
                    {'id':'Fairness. No one should get preferential treatment before the law, and no one is above the law. ','ali':'lawful'},
                    {'id':'Freedom. Tyrants must not be allowed to oppress the people.','ali':'chaotic'},
                    {'id':'Might. If I become strong, I can take what I want—what I deserve','ali': 'neutral'},
                    {'id':'Sincerity. There’s no good in pretending to be something I’m not.','ali': 'neutral'},
                    {'id':'Destiny. Nothing and no one can steer me away from my higher calling. ','ali': 'any'}]
fol_ideal_list = []
#check with alligment
for i in fol_ideal_option:
    if (i['ali'] == aligment[1]):
        fol_ideal_list.append(i)
    elif(i['ali'] == aligment[2]):
        fol_ideal_list.append(i)
    elif(i['ali'] == 'any'):
        fol_ideal_list.append(i)

fol_bond=['I have a family, but I have no idea where they are. One day, I hope to see them again.',
                    'I worked the land, I love the land, and I will protect the land.',
                    'A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.',
                    'My tools are symbols of my past life, and I carry them so that I will never forget my roots.',
                    'I protect those who cannot protect themselves.',
                    'I wish my childhood sweetheart had come with me to pursue my destiny.']
fol_flaw=['The tyrant who rules my land will stop at nothing to see me killed.'
                    'I’m convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.',
                    'The people who knew me when I was young know my shameful secret, so I can never go home again.',
                    'I have a weakness for the vices of the city, especially hard drink.',
                    'Secretly, I believe that things would be better if I were a tyrant lording over the land.',
                    'I have trouble trusting in my allies.']
folk_hero_tool = ['shovel','cartographer’s tools']
folk_hero_skills = ['animal handling','survival']






# list_background=[acolyte]
# p_background = ran.choice(list_background)



#Skills

list_of_skills = [{'name':'acrobatics','stat':'dex'},
                  {'name':'animal handling','stat':'wis'},
                  {'name':'arcana','stat':'int'},
                  {'name':'athletics','stat':'str'},
                  {'name':'deception','stat':'cha'},
                  {'name':'history','stat':'int'},
                  {'name':'insight','stat':'wis'},
                  {'name':'intimidation','stat':'cha'},
                  {'name':'investigation','stat':'int'},
                  {'name':'medicine','stat':'wis'},
                  {'name':'nature','stat':'int'},
                  {'name':'perception','stat':'wis'},
                  {'name':'performance','stat':'cha'},
                  {'name':'persuasion','stat':'cha'},
                  {'name':'religion','stat':'int'},
                  {'name':'sleight of hand','stat':'dex'},
                  {'name':'stealth','stat':'dex'},
                  {'name':'survival','stat':'wis'}]












####
#Właściwy skrypt

import random as ran

import tkinter as tk
from tkinter import filedialog
from tkinter import *
import pdf_script

def first ():
    #define bacgrounds classes obj
    aco_pt_f=ran.choice(aco_pt)
    aco_ideal = ran.choice(aco_ideal_list)
    aco_bond_f=ran.choice(aco_bond)
    aco_flaw_f=ran.choice(aco_flaw)
    acolyte = background('acolyte',aco_tool,aco_skills,aco_pt_f,aco_ideal,aco_bond_f,aco_flaw_f)
   
    sol_pt_f=ran.choice(sol_pt)
    sol_ideal = ran.choice(sol_ideal_list)
    sol_bond_f=ran.choice(sol_bond)
    sol_flaw_f=ran.choice(sol_flaw)
    soldier = background('soldier',soldier_tool,soldier_skills,sol_pt_f,sol_ideal,sol_bond_f,sol_flaw_f)

    cri_pt_f=ran.choice(sol_pt)
    cri_ideal = ran.choice(cri_ideal_list)
    cri_bond_f=ran.choice(cri_bond)
    cri_flaw_f=ran.choice(cri_flaw)
    criminal = background('criminal',criminal_tool,crimnal_skills,cri_pt_f,cri_ideal,cri_bond_f,cri_flaw_f)

    fol_pt_f=ran.choice(sol_pt)
    fol_ideal = ran.choice(fol_ideal_list)
    fol_bond_f=ran.choice(fol_bond)
    fol_flaw_f=ran.choice(fol_flaw)
    folk_hero = background('folk hero',folk_hero_tool,folk_hero_skills,fol_pt_f,fol_ideal,fol_bond_f,fol_flaw_f)

    list_background=[acolyte,soldier,criminal,folk_hero]
    p_background = ran.choice(list_background)
    
    ####GUI
    #określenie okna
    window = tk.Tk()

    #zawartość
    a=tk.Label(text="D&D random character generator")

    #input player name

    a.pack()
    #player name input
    e1 = tk.Label(text = "Please enter player's name")
    e1.pack(side = 'left')
    
    e2 = tk.Entry(window)
    e2.pack(side='left')
    

    b=tk.Label(text="Class:")
    b.pack(side = 'left')
    var_class = StringVar(window)
    var_class.set("random") #default value

    var_class_option = OptionMenu(window,var_class,"random","fighter","wizard","cleric","rogue")
    var_class_option.pack(side = 'left')


    c=tk.Label(text="Race:")
    c.pack(side = 'left')
    var_race = StringVar(window)
    var_race.set("random") #default value

    var_race_option = OptionMenu(window,var_race,"random","elf","human","hafling","dwarf")
    var_race_option.pack(side = 'left')


    def close_window():
        real_name=e2.get()
        window.destroy()
        char_roll(var_race.get(),var_class.get(),real_name,p_background)
       
        

    button = tk.Button(
        text = "roll for character",
        width = 25,
        height = 5,
        bg = 'white',
        fg='black',
        command = close_window)
    button.pack(side = 'bottom')

    window.mainloop()



def char_roll(gui_race,gui_class,real_name,p_background):
    
    ############
    #imports
    import random as ran
    #import names as nm
    
    #####################
    #choices that race or class has no influence
    #age
    #percentage of maximum living age
    old =[0.50,0.65]
    medium=[0.31,0.49]
    young = [0.18,0.30]

    #3 age options
    age_options = [old,medium,young]
    player_age_range = ran.choice(age_options)

    #sex
    sex=['male','female']
    player_sex = ran.choice(sex)

    #languages
    #every race know common
    #player_languages = ['common']

    

    ###################
    #abilities names
    stats = ['str','dex','wis','con','int','cha']
    #ab_value = [15,14,13,13,12,11]


    ##################################
    #roll for dice values function
    def roll(num_roll,dice):
        
        #list of first 4 throws
        vals=[]
        while (num_roll>0):
            k=ran.randint(1,dice)
            vals.append(k)
            num_roll=num_roll-1

        #removing lowest roll
        m_val = min(vals)
        vals.remove(m_val)

        #adding other 3 rolls
        stat_val = 0
        for i in vals:
            stat_val=stat_val+i   
        
        #final ability value
        return stat_val
        
        
    ####################
    #actuall rolling for ability values

    #some variables
    #number of abilites
    stat_num = 6
    #not sorted values
    stat_vals = []
    #sorted values
    stat_vals_new = []


    #checking for not sorted values
    while (stat_num>0):
        rzut=roll(4,6)
        stat_vals.append(rzut)
        stat_num=stat_num-1

    #sorting values
    for i in sorted(stat_vals, reverse=True):
        stat_vals_new.append(i)
    




    ####################
    class race ():
        def __init__ (self,race_name,name,surname,age,languages,ability_mod,speed):
            self.race_name = race_name
            self.name = name
            self.surname = surname
            self.age = age
            self.languages = languages
            self.ability_mod = ability_mod
            self.speed=speed



    #############    START OF RACES     ###########################

    #      ELF

    #surname
    player_surname=ran.choice(e_family)
    #name for males and females
    if(player_sex == 'male'):
        player_name = ran.choice(e_male)
    else:
        player_name = ran.choice(e_female)
    #
    max_age = 750
    player_age_val = ran.choice([(player_age_range[0]*max_age),(player_age_range[1]*max_age)])
    end_age = player_age_val % 1
    player_age_val = player_age_val - end_age

    #languages
    elf_languages=['common','elvish']

    #speed
    e_speed=6

    #make this race a class object
    elf = race("elf",player_name,player_surname,player_age_val,elf_languages,'dex',e_speed)

    ############################################################################################################


    #     HUMAN

    #surname
    player_surname=ran.choice(hu_family)
    #name for males and females
    if(player_sex == 'male'):
        player_name = ran.choice(hu_male)
    else:
        player_name = ran.choice(hu_female)
    #age
    max_age = 100
    player_age_val = ran.choice([(player_age_range[0]*max_age),(player_age_range[1]*max_age)])
    end_age = player_age_val % 1
    player_age_val = player_age_val - end_age

    human_languages = ['common']

    #Abilties bonus
    human_ab_op = []
    a=2
    abili = ['str','dex','wis','con','int','cha']
    while (a>0):
        
        b=ran.choice(abili)
        abili.remove(b)
        human_ab_op.append(b)
        a=a-1

    #speed
    hu_speed=4
    #make this race a class object
    human = race("human",player_name,player_surname,player_age_val,human_languages,human_ab_op,hu_speed)

    ############################################################################################################



    #      HAFLING
    #surname
    player_surname=ran.choice(ha_family)
    #name for males and females
    if(player_sex == 'male'):
        player_name = ran.choice(ha_male)
    else:
        player_name = ran.choice(ha_female)
    #age
    max_age = 70
    player_age_val = ran.choice([(player_age_range[0]*max_age),(player_age_range[1]*max_age)])
    end_age = player_age_val % 1
    player_age_val = player_age_val - end_age

    #languages
    hafling_languages=['common','hafling']

    #speed
    ha_speed=4


    #make this race a class object
    hafling = race("hafling",player_name,player_surname,player_age_val,hafling_languages,'dex',ha_speed)

    ############################################################################################################


    #    DWARF

    #surname
    player_surname=ran.choice(d_family)
    #name for males and females
    if(player_sex == 'male'):
        player_name = ran.choice(d_male)
    else:
        player_name = ran.choice(d_female)
    #age
    max_age = 350
    player_age_val = ran.choice([(player_age_range[0]*max_age),(player_age_range[1]*max_age)])
    end_age = player_age_val % 1
    player_age_val = player_age_val - end_age

    #languages
    dwarf_languages=['common','dwarvish']


    #speed
    d_speed=4

    #make this race a class object
    dwarf = race("dwarf",player_name,player_surname,player_age_val,dwarf_languages,'con',d_speed)

    list_of_races = [elf,human,hafling,dwarf]
    gui_race_check = ['elf','human','hafling','dwarf']
    #######################################################

    
    #RACE
    #check if user choice is not random
    if (gui_race in gui_race_check):
        a=gui_race_check.index(gui_race)
        player_race = list_of_races[a]        
    else:
        player_race = ran.choice(list_of_races)
    

    

    #############    END OF RACES     ###########################


    ######## START OF CLASSES ################################3333


    class clas ():
        def __init__ (self,class_name,ability_order,skill,sav,eq,spells,hitdice):
            self.class_name = class_name
            self.ability_order = ability_order
            self.skill=skill
            self.sav=sav
            self.eq =eq
            self.spells = spells
            self.hitdice=hitdice
            
    # fighter

    fighter_order = [0,3,1,2,5,4]
    fighter_sav = ['str','con']
    fighter_skill_list = ['acrobatics','animal handling','athletics','history','insight','intimidation','perception']
    fighter_skill = ran.sample(fighter_skill_list,2)
   
    f_w_1 = [ran.choice(list_martial),ran.choice(list_martial)]
    f_w_2= [light_crossbow,[handaxe,short_bow]]
    f_armor = [chain_mail,leather_armor]
    f_pack = [dungeoneer_pack, explorer_pack]
    f_eq1=[none_eq]
    f_eq2 = [none_eq]

    f_hitdice= 10

    fighter_eq_list = [f_w_1, f_w_2, f_armor, f_pack, f_eq1, f_eq2] 
    


    fighter_eq = []
    for i in fighter_eq_list:
        fighter_eq.append(ran.choice(i))
    #jeśli wybrana została lista w fw2 trzeba ją podzielić
    for i in fighter_eq:
        if (type(i)==list):
            for a in i:
                fighter_eq.append(a)
            num = fighter_eq.index(i)
            fighter_eq.pop(num)
    
    #figter spell list
    fighter_spell_list=[]
    fighter_1=f_1_spells
    fighter_spell_list.append(fighter_1)



    fighter = clas('fighter',fighter_order,fighter_skill,fighter_sav,fighter_eq,fighter_spell_list,f_hitdice)

    #rogue
    rogue_order = [1,4,0,3,2,5]
    rogue_sav = ['dex','int']
    rogue_skill_list = ['acrobatics','athletics','deception','insight','intimidation','investigation','perception','performance','persuation','sleight of hand','stealth']
    rogue_skill = ran.sample(rogue_skill_list,2)

    r_w_1 = [rapier,shortsword]
    r_w_2= [short_bow,shortsword]
    r_armor = [leather_armor]
    r_pack = [buglar_pack, explorer_pack]
    r_eq1=[dagger]
    r_eq2 = [thieves_tools]

    rogue_eq_list = [r_w_1, r_w_2, r_armor, r_pack,r_eq1,r_eq2] 
    rogue_eq = []
    for i in rogue_eq_list:
        rogue_eq.append(ran.choice(i))
    
    #spells
    rogue_spell_list=[]
    rogue_1=r_1_spells
    rogue_spell_list.append(rogue_1)

    r_hitdice=8

    rogue= clas('rogue',rogue_order,rogue_skill,rogue_sav,rogue_eq,rogue_spell_list,r_hitdice)

    #wizard
    wizard_order=[4,2,1,3,0,5]
    wizard_sav = ['int','wis']
    wizard_skill_list = ['arcana','history','investigation','medicine','religion']
    wizard_skill = ran.sample(wizard_skill_list,2)

    w_w_1 = [quaterstaff,dagger]
    w_pack = [scholar_pack, explorer_pack]
    w_eq1=[spell_book]
    w_eq2 = [component_pouch,arcane_focus]

    wizard_eq_list = [w_w_1, w_pack,w_eq1,w_eq2] 
    wizard_eq = []
    for i in wizard_eq_list:

        wizard_eq.append(ran.choice(i))
    
    #ogólna lista
    wizard_spell_list=[]

    wizard_0=ran.sample(w_0_spells,3)
    wizard_spell_list.append(wizard_0)

    wizard_1=ran.sample(w_1_spells,2)
    wizard_spell_list.append(wizard_1)

    w_hitdice=6

    wizard = clas('wizard',wizard_order,wizard_skill,wizard_sav,wizard_eq,wizard_spell_list,w_hitdice)

    #cleric
    cleric_order=[5,2,3,0,4,1]
    cleric_sav = ['wis','cha']
    cleric_skill_list = ['history','insight','medicine','persuation','religion']
    cleric_skill = ran.sample(cleric_skill_list,2)

    #cleric eq
    c_w_1 = [mace,warhammer]
    c_w_2= [light_crossbow,ran.choice(list_simple)]
    c_armor = [scale_armor,leather_armor]
    c_pack = [priest_pack, explorer_pack]
    c_eq1=[shield]
    c_eq2 = [holy_symbol]

    cleric_eq_list = [c_w_1, c_w_2, c_armor, c_pack, c_eq1, c_eq2] 
    cleric_eq = []
    for i in cleric_eq_list:
        cleric_eq.append(ran.choice(i))
    
    #spells
    cleric_spell_list=[]

    cleric_0=ran.sample(c_0_spells,3)
    cleric_spell_list.append(cleric_0)

    cleric_1=ran.sample(c_1_spells,2)
    cleric_spell_list.append(cleric_1)

    c_hitdice=8

    #define cleric as a class
    cleric = clas('cleric',cleric_order,cleric_skill,cleric_sav,cleric_eq,cleric_spell_list,c_hitdice)


    #############END of CLASS
    

    #GUI class option
    player_class_option = [wizard,rogue,fighter,cleric]
    gui_class_check = ["wizard","rogue","fighter","cleric"]


    #check if user choice is not random
    if (gui_class in gui_class_check):
        a=gui_class_check.index(gui_class)
        player_class = player_class_option[a]
    #if random roll for class
    else:
        player_class = ran.choice(player_class_option)


#-----------------------------------------

    #uszereguj umiętności
    ab_org=[]
    
    for i in player_class.ability_order:
        ab_org.append(stats[i])

    #stats modifires
    stats_modifier = []

    for i in stat_vals_new:
        #parzyste
        if (i%2 == 0):
            a=(i-10)/2
            a=int(a)
            stats_modifier.append(a)
        else:
            a=(i-11)/2
            a=int(a)
            stats_modifier.append(a)
    
    


    #poziom i prof bonus
    level = 1
    prof_bonus = 2
    pass_wis = 10+prof_bonus+stats_modifier[4]


    #saving throws
    sav_names = ['str','dex','con','int','wis','cha']
    sav_values=[]
    for i in sav_names:
        a=sav_names.index(i)
        if ( i in player_class.sav):
            sav_values.append(stats_modifier[a]+2)
        else:
            sav_values.append(stats_modifier[a])

    for i in stats:
        for a in player_race.ability_mod:
            if (i == a):        
                a=ab_org.index(i)    
                stat_vals_new[a]=stat_vals_new[a]+1


   # print(gui_name)

    player_alligment = str(aligment[1] + " " + aligment[2])
    

    #background
    player_background = p_background

    #dictinary z posortowanych umiejętności i ich wartości
    stats_dic = dict(zip(ab_org,stat_vals_new))
    
   

    ########################################
    #Drugie okno


    result_win = tk.Tk()

    #zawartość
    title=tk.Label(text="Short sneak peak:")
    title.pack()
    gui_name = tk.Label(text="Your name is "+player_name+ " "+player_surname)
    gui_name.pack()
    
    gui_race_class = tk.Label(text= str(player_race.race_name)+ " "+str(player_class.class_name))
    gui_race_class.pack()

    gui_stats = tk.Label(text =stats_dic)
    gui_stats.pack()


    def char_roll_again():
        result_win.destroy()
        first()

    def print_pdf():
        

        root=Tk()
        root.withdraw()
        folder_selected=filedialog.askdirectory()
        
        pdf_script.Func(folder_selected,
                        player_name,
                        player_surname,
                        real_name,
                        level,prof_bonus,
                        player_class.class_name,
                        player_race.race_name,
                        player_race.languages,
                        player_race.speed,
                        player_background.bg_name,
                        player_alligment,
                        ab_org, stat_vals_new,stats_modifier,ab_org,
                        player_class.skill, player_class.sav,
                        player_background.pt,
                        player_background.ideal,
                        player_background.bond,
                        player_background.flaw,
                        sav_values,pass_wis,
                        player_class.eq,player_class.spells,
                        player_class.hitdice)
        root.destroy()


    roll_button = tk.Button(
        text = "roll again",
        width = 25,
        height = 5,
        bg = 'white',
        fg='black',
        command = char_roll_again)
    roll_button.pack()

    print_button = tk.Button(
        text = "print full character sheet to PDF",
        width = 25,
        height = 5,
        bg = 'white',
        fg='black',
        command = print_pdf)
    print_button.pack()


    result_win.mainloop()
first()
