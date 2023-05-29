 t = linspace(-10,10,1000);

y1 = (t>=0) & (t<1);
y2 = (t>=0) & (t<2);

plot(t,y1+y2);
xlabel('temps')
ylabel('x(t)')
ylim([-0.5,2.5])
xlim([-1,3])
title('Somme des fonctions Indicatrices de 0 à 1 et de 0 à 2')
