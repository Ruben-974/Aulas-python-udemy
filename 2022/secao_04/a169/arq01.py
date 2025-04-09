cities, states = ['Salvador', 'Ubatuba', 'Belo Horizonte'], ['BA', 'SP', 'MG', 'RJ']
zipper = [(cities[c], states[c]) for c in range(min(len(cities), len(states)))]

print(zipper)