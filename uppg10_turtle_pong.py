"""
Uppgift 10 - Turtle Pong

Skapa en enkel Pong-match med en boll och två paddlar.

Krav:
- Styr vänster paddel med W och S.
- Styr höger paddel med piltangenterna.
- Låt bollen studsa mot över- och underkanten.
- Upptäck när bollen träffar en paddel och ändra bollens x-riktning.
- När bollen passerar en paddel ska motståndaren få poäng.
- Visa poängen och starta om bollen efter en poäng.

Kollisionshjälp:
- Använd boll.xcor() och boll.ycor().
- En paddel kan ses som en rektangel.
- Testa till exempel om bollens x-position är nära paddelns x-position
  och om bollens y-position ligger mellan paddelns övre och undre kant.

Börja i denna ordning:
1. Få en paddel att flytta sig med tangentbordet.
2. Få bollen att röra sig och studsa mot väggarna.
3. Lägga till paddelkollision.
4. Lägga till poäng och omstart.

Bonus:
- Låt bollen öka farten efter varje retur.
- Lägga till en mittlinje.
- Låt datorn styra den ena paddeln.
"""
