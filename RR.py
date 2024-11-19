import numpy as np
import matplotlib.pyplot as plt


def d_tau_sur_dt(g, t):
    return np.sqrt(1/(1+g**2*t**2))


def vitesse(g, t):
    return g*t/np.sqrt(1+g**2*t**2)

# T : un quart de la durée du voyage, en secondes
# g : accélération de la pesanteur ressentie, en m/s^2
# pasdelta : écart de temps entre deux points sur les lignes d'univers, en secondes


def calcul_dis_tau(T=3600*24*1000, g=9.81, pasdelta=3600*24*100):
    # pas temporel de calcul pour l'intégration numérique
    pas = T/1e4
    # vitesse de la lumière en m/s
    c = 299792458
    # accélération en unité réduite
    g = g/c

    # 0<t<T
    ts = np.arange(0, T, pas)
    dtt = d_tau_sur_dt(g, ts)
    vit = vitesse(g, ts)
    t = ts.copy()

    # T<t<3*T
    ts = np.arange(-T, T, pas)
    dtt = np.append(dtt, d_tau_sur_dt(g, ts))
    vit = np.append(vit, -vitesse(g, ts))
    t = np.append(t, 2*T+ts)

    # 3*T<t<4*T
    ts = np.arange(0, T+pas, pas)
    dtt = np.append(dtt, d_tau_sur_dt(g, T-ts))
    vit = np.append(vit, -vitesse(g, T-ts))
    t = np.append(t, 3*T+ts)

    # intégration numérique
    dis = pas*np.cumsum(vit)
    tau = pas*np.cumsum(dtt)

    # calculs en vitesse constante
    dis_max = np.max(dis)
    V = dis_max/(2*T)
    tau2 = t*np.sqrt(1-V**2)
    vit2 = V*(t < 2*T)-V*(t >= 2*T)
    dis2 = pas*np.cumsum(vit2)

    # calculs pour le tracé de tau à intervalles temporels réguliers
    deltat = np.arange(0, t[-1], pasdelta)
    indext = [np.where(t >= dt)[0][0] for dt in deltat]
    deltatau = np.arange(0, tau[-1], pasdelta)
    indextau = [np.where(tau >= dt)[0][0] for dt in deltatau]
    deltatau2 = np.arange(0, tau2[-1], pasdelta)
    indextau2 = [np.where(tau2 >= dt)[0][0] for dt in deltatau2]

    # conversions en jours et en jours-lumière
    t = t/(3600*24)
    tau = tau/(3600*24)
    tau2 = tau2/(3600*24)
    dis = dis/(3600*24)
    dis2 = dis2/(3600*24)

    # affichage des résultats en texte
    print('\nRésultats numériques\n')
    print(f'Accélération ressentie : {g*c:.2f} m/s^2')
    print(f'Temps t final: {max(t)/365.25:.2f} années ({max(t):.2f} jours)')
    print(
        f'Temps tau final: {max(tau)/365.25:.2f} années ({max(tau):.2f} jours)')
    print(f'Vitesse maximale atteinte : {max(vit):.3f}c')
    print(
        f'Distance atteinte : {max(dis)/365.25:.2f} années-lumière ({max(dis):.2f} jours-lumière)')
    print('\nGraphiques\n')

    # tracés des graphiques
    plt.figure()
    plt.plot(t, t, 'r', label='temps (référentiel inertiel)')
    plt.plot(t, tau, 'b', label='temps propre (force constante)')
    plt.plot(t, tau2, 'g', label='temps propre (vitesse uniforme)')
    plt.xlabel('temps (jours)')
    plt.ylabel('temps propre (jours)')
    plt.grid('on')
    plt.text(t[-1], t[-1], f'{t[-1]:.2f} jours',
             ha='right', c='r', weight='bold')
    plt.text(t[-1], tau[-1], f'{tau[-1]:.2f} jours',
             ha='right', c='b', weight='bold')
    plt.text(t[-1], tau2[-1], f'{tau2[-1]:.2f} jours',
             ha='right', c='g', weight='bold')
    plt.legend()

    plt.figure()
    plt.plot(t, vit, 'b', label='vitesse (force constante)')
    plt.plot(t, vit2, 'g', label='vitesse (vitesse uniforme)')
    plt.grid('on')
    plt.xlabel('temps (jours)')
    plt.ylabel('vitesse (v/c)')
    n = np.where(t >= T/(3600*24))[0][0]
    plt.text(t[n], vit[n], f'{vit[n]:.3f}c', ha='right', c='b', weight='bold')
    plt.text(t[n], vit2[n], f'{vit2[n]:.3f}c',
             ha='right', c='g', weight='bold')
    plt.legend()

    plt.figure()
    plt.plot(np.zeros(len(t)), t, 'r', label='référentiel inertiel')
    plt.plot(dis, t, 'b', label='force constante')
    plt.plot(dis2, t, 'g', label='vitesse constante')
    plt.grid('on')
    plt.title('Lignes d\'univers')
    plt.ylabel('temps (jours)')
    plt.xlabel('distance (jours-lumière)')
    plt.legend()

    plt.figure()
    plt.plot(np.zeros(len(t)), t, 'r', label='référentiel inertiel', lw=0.5)
    plt.plot(np.zeros(len(indext)), t[indext], 'r.', ms=8)
    plt.plot(0, t[-1], 'r.', ms=8)
    plt.plot(dis, t, 'b', label='force constante', lw=0.5)
    plt.plot(dis[indextau], t[indextau], 'b.', ms=8)
    plt.plot(dis2, t, 'g', label='vitesse constante', lw=0.5)
    plt.plot(dis2[indextau2], t[indextau2], 'gx', ms=6)
    plt.grid('on')
    plt.ylabel('temps (jours)')
    plt.xlabel('distance (jours-lumière)')
    plt.title(
        f'Lignes d\'univers (pas de temps={pasdelta/(3600*24):.2f} jours)')
    plt.legend()

    plt.show()
