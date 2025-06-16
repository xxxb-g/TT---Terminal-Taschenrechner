# TT - Terminal-Taschenrechner
Ein einfacher Taschenrechner, in Python geschrieben.
## Funktionen:
- addiere() Funtion, die bis zu 8 Argumente addiert. 
- subtrahiere(a,b) Funktion, die a minus b rechnet
- multipliziere() Funktion, die bis zu 8 Argumente multipliziert
- dividiere(a,b) Funktion, die a geteilt durch b rechnet.
- Löse(a,z,b) Funktion, die eine der oberen Rechenoperationen durchführt, je nach Angabe von z. Wenn ein Argument nicht angegeben wird, wird es interaktiv abgefragt.
- Taschenrechner(a,z,b) siehe Löse()
- TT() siehe Löse() 

## Beispiele:
- `addiere(7,3)
7+3=
10.0`
-`subtrahiere(15,2.5)
15-2.5=
12.5`
-`multipliziere(32,0.5,0.75,2.3)
Diese Werte multipliziert ergeben:
27.599999999999998`
- `dividiere(21,"7")
21/7=
3.0`
- `Taschenrechner(15)
Welche Rechenoperation willst du nutzen? (+ für Addition, - für Subtraktion, * für Multiplikation, / für Division) vertippt
Ungültige Eingabe. Versuche es erneut!
Welche Rechenoperation willst du nutzen? (+ für Addition, - für Subtraktion, * für Multiplikation, / für Division)+
Was ist die zweite Zahl?3

15+3=
18.0`
-`TT(1,"+",1)
1+1=
2.0`

Natürlich können Werte ungenau sein, wie im 3. Beispiel, was eigentlich 27,6 sein muss, was an der Rechenweise von Python liegt, nicht an mir. Auch schließe ich nicht aus, dass ich fehlerhaft programmiert habe. Weißt mich gern auf jeden Bug hin, der auf meinen Code zurückzuführen ist.
