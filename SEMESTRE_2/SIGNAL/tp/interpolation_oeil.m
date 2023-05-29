% oeil: mauvais interpolateur
%
% x(t)=3sin(2*pi*f0*t)  % f0=80Hz
% fe1=200Hz (200 échantillons par seconde)
% fe2=1500Hz ( 1500 échantillons par seconde)
% duree=60ms
%
f0=80;
fe1=200; fe2=1500;
duree=0.06;
%

n1=round(duree*fe1);    % nombre d'échantillons pour fe1
n2=round(duree*fe2);    % nombre d'échantillons pour fe2
%
 
t1=[0:n1-1]/fe1;        % valeurs temporelles des échantillons pour fe1
t2=[0:n2-1]/fe2;        % valeurs temporelles des échantillons pour fe2
%

x1=3*sin(2*pi*f0*t1);
x2=3*sin(2*pi*f0*t2);

%
% visualisation
figure
subplot(2,1,1),plot(t1,x1,'x')
title('échantillons d''une sinusoïde à f0=80Hz échantillonnée à 200Hz')
subplot(2,1,2),plot(t2,x2,'x')
title('échantillons d''une sinusoïde à 80HZ échantillonnée à 1500Hz')

figure
subplot(2,1,1),stem(t1,x1,'x')
title('signal xd d''unesinusoide à f0=80Hz échantillonnée à 200Hz')
subplot(2,1,2),stem(t2,x2,'x')
title('signal xd d''une sinusoide à 80HZ échantillonnée à 1500Hz')