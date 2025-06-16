# Made by xxxb
# see on github: https://github.com/xxxb-g/TT---Terminal-Taschenrechner
def addiere(a="0",b='0',c="0",d='0',e="0",f='0',g="0",h='0'):
    try:
        x=float(a)+float(b)+float(c)+float(d)+float(e)+float(f)+float(g)+float(h)
        if float(c) != 0 or float(d) !=0 or float(e) !=0 or float(f) !=0 or float(g) != 0 or float(h) != 0:
            print("Diese Werte addiert ergeben")
        else:
            print(str(a)+"+"+str(b)+"=")
        return x
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")



def subtrahiere(a,b):
    try:
        x=float(a)-float(b)
        print(str(a)+"-"+str(b)+"=")
        return x
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")



def dividiere(a,b):
    try:
        x=float(a)/float(b)
        print(str(a)+"/"+str(b)+"=")
        return x
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")



def multipliziere(a="1",b='1',c="1",d='1',e="1",f='1',g="1",h='1'):
    try:
        x=float(a)*float(b)*float(c)*float(d)*float(e)*float(f)*float(g)*float(h)
        if float(c) != 1 or float(d) !=1 or float(e) !=1 or float(f) !=1 or float(g) != 1 or float(h) != 1:
            print("Diese Werte multipliziert ergeben:")
        else:
            print(str(a)+"*"+str(b)+"=")
        return x
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")



def Löse(a="interaktiv",z="interaktiv",b="interaktiv"):
    try:
        if a=="interaktiv" or z=="interaktiv" or b == "interaktiv":
            Interaktiv = True

        if a=="interaktiv":
            while True:
                try:
                    a = input("Was ist die erste Zahl?")
                    temp = float(a)
                    break
                except ValueError:
                    print("Ungültige Eingabe. Versuche es erneut!")

        while True:
            if z=="interaktiv":
                z = input("Welche Rechenoperation willst du nutzen? (+ für Addition, - für Subtraktion, * für Multiplikation, / für Division)")
            if z!= "+" and z!="-" and z!="*" and z!="/":
                print("Ungültige Eingabe. Versuche es erneut!")
                z = "interaktiv"
            else:
                break

        if b=="interaktiv":
            while True:
                try:
                    b = input("Was ist die erste Zahl?")
                    temp = float(b)
                    break
                except ValueError:
                    print("Ungültige Eingabe. Versuche es erneut!")

        if Interaktiv==True:
            print("\n")


        if z=="+":
            return addiere(a,b)
        if z=="-":
            return subtrahiere(a,b)
        if z=="*":
            return multipliziere(a,b)
        if z=="/":
            return dividiere(a,b)
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")



def Taschenrechner(a="interaktiv",b="interaktiv"):
    return Löse(a,b)
