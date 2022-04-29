import numpy as np
from principal_component_analysis import PrincinpalComponents

data = [(1,2,0), (2,3,1), (2,1,3), (3,4,2), (3,2,4), (4,3,6)]

pca = PrincinpalComponents()
pca.fit(data)
print(pca.transform((1,2,0)))
print(pca.transformed_data)