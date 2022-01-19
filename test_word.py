import pickle

with open('data/censor.txt', 'r') as f:
    a = f.read().split(', ')

with open('data/censor.pkl', 'wb') as f:
    pickle.dump(a, f)

