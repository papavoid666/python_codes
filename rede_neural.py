#rede completa para regressão linear
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#D train (data set)
xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = 2 * xs - 1
# criando a rede neural
model = tf.keras.Sequential(name='rede_IF_01')
#configurando a primeira camada da rede
model.add(tf.keras.layers.Dense(1, input_dim=1, use_bias=1, activation='linear'))
opt=tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.0)
#model.compile(optimizer=opt, loss='mean_squared_error', metrics='mean_absolute_error')
print(model.summary())
# treinando a rede
history =model.fit(xs, ys, epochs = 1000,verbose=0)
#testando a rede
xs_test=np.linspace(-2,2,11);
ys_test=model.predict(xs_test)
#fazendo os gráficos
plt.rcParams.update({'font.size': 12})
plt.figure()
plt.plot(xs_test,ys_test,'r.')
plt.plot(xs_test,(2 * xs_test - 1),'b-')
plt.legend(['previsões','reta original'])
plt.xlabel('x');plt.ylabel('y')
# mostra os dados em history
print(history.history.keys())
# plota o loss e a metrica
plt.figure()
plt.subplot(2,1,1)
plt.plot(history.history['loss'],'k')
plt.legend(['loss'])
plt.subplot(2,1,2)
plt.plot(history.history['mean_absolute_error'],'k--')
plt.legend(['métrica'])
plt.xlabel('epoch')
plt.tight_layout()
plt.show()

