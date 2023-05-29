f = linspace(-5,5,1000);

y3 = abs(sin(pi*f)/f)*sqrt(5+4*cos(2*pi*f));

plot(f,y3);
xlabel('fréquences')
ylabel('module de X(f)')
xlim([-4,4])
title('module de la transformé de Fourier')