import names as nm
import textwrap
import math

def Func(folder_selected,
        name,
        surname,
        real_name,
        level,prof_bonus,
        clas,
        race,languages,speed,
        bg_name,
        aligment,
        stats,stats_val,stats_modifier,ab_org,
        class_skill,sav,
        bg_pt,bg_ideal,bg_bond,bg_flaw,
        sav_values,pass_wis,
        eq,spells,
        hitdice):

    from reportlab.pdfgen import canvas
    from reportlab.lib.units import cm
    from reportlab.lib import colors
    import pathlib

    pdf_name=str(folder_selected+"/"+name+"_"+surname+".pdf")
    pdf_file = canvas.Canvas(pdf_name)
    print(pdf_name)
    page_width, page_height = pdf_file._pagesize
    bg_width = page_width -15
    bg_heigth = page_height - 15

    pdf_file.translate(cm,cm)
    #pdf_file.drawImage("C:\\Users\\Agnieszka\\Desktop\\python\\scrypty\\dnd\\background.jpg",0,0,width=bg_width,height=bg_heigth,preserveAspectRatio=True)
    bg_dir=pathlib.Path(__file__).parent.absolute()
    pdf_file.drawImage(str(bg_dir)+"/background.jpg",0,0,width=bg_width,height=bg_heigth,preserveAspectRatio=True)
    
    pdf_file.setFontSize(11)
    
    
    pdf_file.drawString(40, 180, "Known languages:")
    x=40
    y=165
    for i in languages:
        pdf_file.drawString(x, y, i)
        y=y-13


    pdf_file.setFontSize(11)
    #Name and Surname
    pdf_file.drawString(45, 728, name+" "+surname)
    pdf_file.drawString(260, 742, str(clas) + " " + str(level) + "lv")
    pdf_file.drawString(260, 718, str(race))
    pdf_file.drawString(372, 742, str(bg_name))
    #napraw imię
    pdf_file.drawString(468, 742, real_name)
    pdf_file.drawString(372, 718, str(aligment))
    pdf_file.drawString(468, 718, "0")

    #umięjętności i modyfikatory
    #zależne ułożenie od klasy

    for i in stats:
        if (i=="str"):
            a=stats.index(i)
            pdf_file.drawString(44, 632, str(stats_val[a]) )
            pdf_file.drawString(47, 610, str(stats_modifier[a]) )
        if (i=="dex"):
            a=stats.index(i)
            pdf_file.drawString(43, 565, str(stats_val[a]) )
            pdf_file.drawString(47, 542, str(stats_modifier[a]) )
        if (i=="con"):
            a=stats.index(i)
            pdf_file.drawString(43, 495, str(stats_val[a]) )
            pdf_file.drawString(47, 472, str(stats_modifier[a]) )
        if (i=="int"):
            a=stats.index(i)
            pdf_file.drawString(43, 425, str(stats_val[a]) )
            pdf_file.drawString(47, 402, str(stats_modifier[a]) )
        if (i=="wis"):
            a=stats.index(i)
            pdf_file.drawString(43, 358, str(stats_val[a]) )
            pdf_file.drawString(47, 334, str(stats_modifier[a]) )
        if (i=="cha"):
            a=stats.index(i)
            pdf_file.drawString(44, 288, str(stats_val[a]) )   
            pdf_file.drawString(47, 265, str(stats_modifier[a]) )    


    pdf_file.setFontSize(10)
    #proficiecy bonus
    pdf_file.drawString(98,626, str(prof_bonus))

    #passive wisdom
    pdf_file.drawString(30,215, str(pass_wis))


    pdf_file.setFontSize(7)    
    #saving throws dodaj kropki
    x=110
    y=593
    for i in sav_values:
        pdf_file.drawString(x,y, str(i))
        y=y-13 

    #stats_modifier dodaj kropki
    x=110
    y=481
    for i in nm.list_of_skills:
        for ab in ab_org:
            if (i['stat']==ab):
                num=ab_org.index(ab)
                #profitciency bonus
                if i in class_skill:
                    pdf_file.drawString(x,y, str(stats_modifier[num]+prof_bonus)) 
                    
                else:
                    pdf_file.drawString(x,y, str(stats_modifier[num]))
                y=y-13
    
    #personality traits
    #font
    pdf_file.setFontSize(7)
    #lista wszystkich
    personality = [bg_pt,bg_ideal['id'],bg_bond,bg_flaw]
    #startowa wysokość
    y=655
    #ponieważ pierwsze pole jest większe niż inne
    pt_field = True
    for i in personality:
        #ilość wierszy do obliczenia wysokości
        row_num=-1
        #maks szerokość
        txt_width = 40
        #okreslenie ilości rzędów
        rows = len(str(i))/txt_width
        rows=math.ceil(rows)        
        
        #jeśli więcej niż jeden rząd        
        if (len(str(i))>txt_width):
            wrap_text = textwrap.wrap(str(i),width=txt_width)
            
            for cur_row in range(0,rows):
                pdf_file.drawString(410, y, wrap_text[cur_row])
                y=y-8    
                row_num+=1 
                 
        #jeśli jeden rząd      
        else:
            pdf_file.drawString(410, y,str(i))
            row_num-=1   
        #nowa wysokość  
        if (pt_field==True):
            y=y-55+(row_num*6)
            pt_field=False
        else:
            y=y-45+(row_num*6)
        
   #----------------------------------
   #Attack and Spellcasting
      
    x=215
    y=410
    x_2=270
    y_2=195    
    
    for i in eq:                  
        if (str(i.__class__.__name__)=='armor'):
            pdf_file.drawString(270, 210, i.name )
        elif (str(i.__class__.__name__)=="rest_eq"):
            pdf_file.drawString(x_2, y_2, i.name )
            y_2=y_2-15            
        else:            
            pdf_file.drawString(x, y, i.name)
            pdf_file.drawString((x+70),y,i.bonus)
            pdf_file.drawString((x+100),y,i.typ)
            y=y-20



    
    x=215
    y=350
    spell_book=[]
    
    for spell_level in range (0,len(spells)):
         spell_cur=", ".join(map(str,spells[spell_level]))
         spell_book.append(spell_cur)
    
    row_num=-1
    #maks szerokość
    txt_width = 55
         



    for spell_level in range (0,len(spells)):

        #okreslenie ilości rzędów
        rows = len(spell_book[spell_level])/txt_width
        rows=math.ceil(rows) 

        pdf_file.drawString(x, y, ("Lv"+str(spell_level)))
        y=y-8
        #zawijanie tekstu
        wrap_text = textwrap.wrap(spell_book[spell_level],width=txt_width)
                        
        for cur_row in range(0,rows):
            
            pdf_file.drawString(x, y, wrap_text[cur_row])
            y=y-8    
            row_num+=1 

        y=y-12
       

    #armor class
    #if you got no armor AC = 10 + dex modifier
    #if you got armor AC = armor bonus + dex (if armor call's for it)

    AC=0
    
    for i in eq:
        if ("armor" == i.__class__.__name__):  
            if(i.dex_bonus==True):
                AC=int(i.bonus) + int(stats_modifier[1])
            else:
                AC=int(i.bonus)
            break
        else:
            AC=10+int(stats_modifier[1])
    pdf_file.setFontSize(11)
    pdf_file.drawString(230,650,str(AC))
    
    #initiative
    pdf_file.drawString(285,645,str(stats_modifier[1]))

    #speed
    pdf_file.drawString(345,645,str(speed))

    
    #hit dice based on class
    dice=(str(level)+"d"+str(hitdice))
    
    total_dice=level*hitdice

    pdf_file.setFontSize(11)
    pdf_file.drawString(230,465,dice)
    pdf_file.setFontSize(7)
    pdf_file.drawString(240,485,str(total_dice))

    #HP max =max hit dice value + con modifier
    hp_max = total_dice+stats_modifier[2]
    pdf_file.setFontSize(7)
    pdf_file.drawString(285,605,str(hp_max))

    #current HP = MAX HP for start :)



    #save and open pdf
    pdf_file.save()


