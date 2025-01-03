# Voyage relativiste

## La vidéo

https://www.youtube.com/watch?v=1jKPtu5m3DQ

## Le voyage

Le voyage d'un astronaute se déroule dans un vaisseau spatial qui se déplace le long d'une droite. Dans un référentiel inertiel, éloigné de toute masse (pas de gravitation), le vaisseau a une vitesse initiale nulle à $t=0$ et on lui applique une force constante $F$ pendant une durée $T$. Ainsi, il accélère pour atteindre une vitesse maximale à $t=T$, puis on lui applique une force $-F$ opposée à la précedente pour $T<t<3T$. Donc sa vitesse diminue, s'annule à $t=2T$, puis prend une valeur maximale à $t=3T$, opposée à celle atteinte à $t=T$. Pour $3T<t<4T$, on applique enfin la même force $F$ qu'au départ, de sorte qu'il ralentisse, puis retrouve son point de départ avec une vitesse nulle à $t=4T$.

L'astronaute à bord du vaisseau dispose d'une horloge qui mesure le **temps propre** noté $\tau$ au cours du voyage, initialisée à $0$ au départ. Une autre horloge restée au point de départ mesurera le temps $t$, initialisée aussi à $0$ au départ.

Quel seront les temps affichés par ces horloges à l'arrivée ?

C'est l'occasion de faire un peu de **relativité restreinte** avec des **mobiles accélérés**.

## Les calculs

Dans un référentiel inertiel, le principe fondamental de la dynamique en relativité restreinte s'écrit, pour une force $F$, une masse $m$ et une vitesse $v$ :

$$F=\dfrac{d}{dt}\left( m\gamma v \right)$$

avec :

$$\gamma=\dfrac{1}{\sqrt{1-v^2}}$$

On utilise ici des **unités réduites**, de sorte que $v=1$ corresponde à la vitesse de la lumière. Il en est de même pour la distance, avec $x=1$ qui correspond à la distance parcourue par la lumière pendant $t=1s$, soit $299792458$ m, soit **une seconde-lumière** (s.l.).

La force $F$ est choisie constante, avec $F=mg$, de sorte que l'astronaute **ressente la pesanteur terrestre** ($g=9.81/299792458$ s.l./s^2, attention aux unités). Pour illustrer le principe du calcul, on ne développera que sa première étape, pour $0<t<T$.

En intégrant $F=\dfrac{d}{dt}\left( m\gamma v \right)=mg$, on obtient :

$$\gamma v=gt$$

Ainsi :

$$v=\dfrac{gt}{\sqrt{1+(gt)^2}}$$

La vitesse $v$ ne dépasse jamais $1$ dans ce contexte relativiste. La métrique permettant d'accéder à la variation de temps propre $d\tau$ pour une variation de temps $dt$ et un déplacement $dx$ dans le référentiel inertiel est :

$$d\tau^2=dt^2-dx^2$$

(la forme simple de cette métrique résulte du fait que l'on a utilisé des unités réduites)

Ainsi :

$$\left(\dfrac{d\tau}{dt}\right)^2=1-\left(\dfrac{dx}{dt}\right)^2=1-v^2=\dfrac{1}{1+(gt)^2}$$

Soit :

$$\dfrac{d\tau}{dt}=\dfrac{1}{\sqrt{1+(gt)^2}}$$

$$\dfrac{dx}{dt}=\dfrac{gt}{\sqrt{1+(gt)^2}}$$

Une **intégration numérique** donnera accès à $\tau$ et $x$ en fonction de $t$, avec un pas temporel de calcul suffisament petit (on peut déjà procéder ainsi sans être "expert en calcul littéral des intégrales").

La distance $x$ et le temps $t$ permettront de tracer des **lignes d'univers** ($x$ en abscisse et $t$ en ordonnée), sur lesquelles on visualisera le temps propre $\tau$ via des points correspondant à des intervalles réguliers de temps propre. Pour les échelles lors du tracé des courbes, on choisira plutôt le **jour** comme unité de temps et le **jour-lumière** comme unité de distance.

On effectuera aussi une comparaison avec une version très simplifiée du voyage où la vitesse est constante à l'aller et au retour et la distance parcourue identique.

## Les tracés

```
>>> import RR
>>> RR.calcul_dis_tau(T=3600*24*1000,g=9.81,pasdelta=3600*24*100)

Résultats numériques

Accélération ressentie : 9.81 m/s^2
Temps t final: 10.95 années (4000.00 jours)
Temps tau final: 6.83 années (2493.39 jours)
Vitesse maximale atteinte : 0.943c
Distance atteinte : 3.87 années-lumière (1414.01 jours-lumière)

Graphiques
```

![Figure_1](https://github.com/user-attachments/assets/d5eaa4ab-e95b-48e7-9aa5-632f8e29282a)

![Figure_2](https://github.com/user-attachments/assets/b07f4b59-ac76-4579-b616-88e5f37482d4)

![Figure_3](https://github.com/user-attachments/assets/842f9e27-13b9-4540-aa1d-b7f4adf91bf9)

![Figure_4](https://github.com/user-attachments/assets/bf138780-ba55-45a1-9761-3c78a3d9385f)


## Les informations

Le notebook [RR.ipynb](RR.ipynb)

Le programme avec calcul numérique des intégrales [RR.py](RR.py)

Le programme avec expression littérale des intégrales [RRI.py](RRI.py)

Reproduction de l'exemple avec **Proxima Centauri** sur la page [https://fr.wikipedia.org/wiki/Voyage_relativiste](https://fr.wikipedia.org/wiki/Voyage_relativiste)

![image](https://github.com/user-attachments/assets/d8b4cbaa-4344-4021-b3ff-b17b817fb569)

```
>>> import RR
>>> RR.calcul_dis_tau(T=3600*24*365.25*11.8/4,g=10,pasdelta=3600*24*100)

Résultats numériques

Accélération ressentie : 10.00 m/s^2
Temps t final: 11.80 années (4309.95 jours)
Temps tau final: 7.03 années (2569.38 jours)
Vitesse maximale atteinte : 0.952c
Distance atteinte : 4.30 années-lumière (1569.99 jours-lumière)
```

```
>>> import RRI
>>> RRI.calcul_dis_tau(T=3600*24*365.25*11.8/4,g=10,pasdelta=3600*24*100)

Résultats numériques

Accélération ressentie : 10.00 m/s^2
Temps t final: 11.80 années (4309.95 jours)
Temps tau final: 7.03 années (2569.38 jours)
Vitesse maximale atteinte : 0.952c
Distance atteinte : 4.30 années-lumière (1569.99 jours-lumière)
```
