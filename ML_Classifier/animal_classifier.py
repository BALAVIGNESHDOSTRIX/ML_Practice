from sklearn import tree

class AnimalsDetector:
    def __init__(self):
        self.labels = [0,0,1,1,0] # Here '0' for Fishes '1' for animals
        self.features = [[0,50],[0,150000],[4,5],[4,6],[0,0.05]] # Here array list first parameter no of leg and weight of the animals

    def AnimalDetector(self,userdata):
        algorithm = tree.DecisionTreeClassifier()
        algorithm = algorithm.fit(self.features, self.labels)
        return algorithm.predict(userdata)


animal = AnimalsDetector()
leg_c = input("Enter the Legs count of animal: ")
weight = input("Enter the Animal weight: ")
result = animal.AnimalDetector([[leg_c, weight]])
# print(result)
if result <= 0:
    print('This is a Fish category Animal')
elif result >= 4 or result > 0:
    print('This is a animal category')


