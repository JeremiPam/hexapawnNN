import keras
from keras import Input, Model
from keras.src.backend.jax.nn import relu6
from keras.src.layers import Dense

inp=Input(28,)
l1=Dense(128,activation='relu')(inp)
l2=Dense(128,activation='relu')(l1)
l3=Dense(128,activation='relu')(l2)

policyOut=Dense(28,name='policyHead',activation='softmax')(l3)
valueOut=Dense(1,name='valueOut',activation='tanh')(l3)

bce=keras.losses.categorical_crossentropy(from_logits=False)
model=Model(inp,[policyOut,valueOut])
model.compile(optimizer='SGD',loss={'valueHead':'mean_squared_error','policyHead':bce})
model.save('random_model.keras')