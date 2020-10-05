import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_columns = None
pd.options.display.max_rows = None

pokemon = "Pokemon.csv"
ds = pd.read_csv(pokemon).fillna('')

# Omitting specific unwanted pokemon in ds
ds =ds[~ds.Name.str.contains('Mega|%|Forme|Cloak|Rotom|Mode|Male|Size|Confined|Unbound|Female|KyuremBlack|KyuremWhite|Primal')]

# Make all future ds plots used apply only to generations 3 and below; Change int to correspond
# with preferred generation
ds =(ds.loc[ds['Generation']==1])
# Omit all future legendary pokemon from ds; Change to True if you wish to include in analysis
ds = ds.loc[ds['Legendary']==False]


def bestOverallPokemonPerStat():
    bestOfTheBest = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    for x in bestOfTheBest:
        print('\nBest overall Pokemon by %s\n' % (x))
        print((ds.loc[ds[x].idxmax()]))

# bestOverallPokemonPerStat()


# list to be used in future functions which contains extracted Type labels
poketypes = []
for x in ds['Type 1'].unique():
    poketypes.append(x)


hp = (ds.iloc[:, [2, 5]])

def highestHp(df, list):
    for x in poketypes:
        print('\nHighest HP Pokemon for %s\n' %(x))
        yes = ds.loc[ds['Type 1'] == x]
        y = yes.loc[yes['HP'].idxmax()]
        print(y)

    plota = []
    plotb = []
    for x in list:
        types = df[df['Type 1'].str.contains(x)]
        plota.append(x)
        j = (int(types['HP'].mean()))
        plotb.append(j)
    plt.plot(plota, plotb, color='g',marker='.')
    plt.title('Mean HP for each Type 1',fontsize=15)
    plt.ylabel('HP')
    plt.show()

highestHp(hp, poketypes)


attack = (ds.iloc[:, [2, 6]])

def highestAttack(df, list):
    for x in poketypes:
        print('\nHighest Attack Pokemon for %s\n' %(x))
        yes = ds.loc[ds['Type 1'] == x]
        y = yes.loc[yes['Attack'].idxmax()]
        print(y)

    plota = []
    plotb = []
    for x in list:
        types = df[df['Type 1'].str.contains(x)]
        plota.append(x)
        j = (int(types['Attack'].mean()))
        plotb.append(j)
    plt.plot(plota, plotb, color='r',marker='.')
    plt.title('Mean Attack for each Type 1',fontsize=15)
    plt.ylabel('Attack')
    plt.show()

# highestAttack(attack, poketypes)


defense = (ds.iloc[:, [2, 7]])

def highestDefense(df, list):
    for x in poketypes:
        print('\nHighest Defense Pokemon for %s\n' %(x))
        yes = ds.loc[ds['Type 1'] == x]
        y = yes.loc[yes['Defense'].idxmax()]
        print(y)

    plota = []
    plotb = []
    for x in list:
        types = df[df['Type 1'].str.contains(x)]
        plota.append(x)
        j = (int(types['Defense'].mean()))
        plotb.append(j)
    plt.plot(plota, plotb, color='b',marker='.')
    plt.title('Mean Defense for each Type 1',fontsize=15)
    plt.ylabel('Defense')
    plt.show()

# highestDefense(defense, poketypes)


speed = (ds.iloc[:, [2, 10]])

def highestSpeed(df, list):
    for x in poketypes:
        print('\nHighest Speed Pokemon for %s\n' %(x))
        yes = ds.loc[ds['Type 1'] == x]
        y = yes.loc[yes['Speed'].idxmax()]
        print(y)

    plota = []
    plotb = []
    for x in list:
        types = df[df['Type 1'].str.contains(x)]
        plota.append(x)
        j = (int(types['Speed'].mean()))
        plotb.append(j)
    plt.plot(plota, plotb, color='y',marker='.')
    plt.title('Mean Speed for each Type 1',fontsize=15)
    plt.ylabel('Speed')
    plt.show()

# highestSpeed(speed, poketypes)


spAtk = (ds.iloc[:, [2, 8]])

def highestspAtk(df, list):
    for x in poketypes:
        print('\nHighest Sp. Atk Pokemon for %s\n' %(x))
        yes = ds.loc[ds['Type 1'] == x]
        y = yes.loc[yes['Sp. Atk'].idxmax()]
        print(y)

    plota = []
    plotb = []
    for x in list:
        types = df[df['Type 1'].str.contains(x)]
        plota.append(x)
        j = (int(types['Sp. Atk'].mean()))
        plotb.append(j)
    plt.plot(plota, plotb, color='m',marker='.')
    plt.title('Mean Sp. Atk for each Type 1',fontsize=15)
    plt.ylabel('Sp. Atk')
    plt.show()

# highestspAtk(spAtk, poketypes)


spDef = (ds.iloc[:, [2, 9]])

def highestspDef(df, list):
    for x in poketypes:
        print('\nHighest Sp. Def Pokemon for %s\n' %(x))
        yes = ds.loc[ds['Type 1'] == x]
        y = yes.loc[yes['Sp. Def'].idxmax()]
        print(y)

    plota = []
    plotb = []
    for x in list:
        types = df[df['Type 1'].str.contains(x)]
        plota.append(x)
        j = (int(types['Sp. Def'].mean()))
        plotb.append(j)
    plt.plot(plota, plotb, color='c',marker='.')
    plt.title('Mean Sp. Def for each Type 1',fontsize=15)
    plt.ylabel('Sp. Def')
    plt.show()

# highestspDef(spDef, poketypes)


total = (ds.iloc[:, [2, 4]])

def highestTotal(df, list):
    for x in poketypes:
        print('\nBest Type 1 Pokemon for %s\n' %(x))
        yes = ds.loc[ds['Type 1'] == x]
        y = yes.loc[yes['Total'].idxmax()]
        print(y)

    plota = []
    plotb = []
    for x in list:
        types = df[df['Type 1'].str.contains(x)]
        plota.append(x)
        j = (int(types['Total'].mean()))
        plotb.append(j)
    plt.plot(plota, plotb, color='darkkhaki',marker='.')
    plt.title('Mean Total for each Type 1',fontsize=15)
    plt.ylabel('Total')
    plt.show()

# highestTotal(total, poketypes)