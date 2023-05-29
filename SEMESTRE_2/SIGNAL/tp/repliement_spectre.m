% Son et repliement du spectre
%
% fréquence instantanée: fi(t)=f0+lambda*t
% x(t)=cos(2*pi*f0*t+pi*lambda*t^2)
%
% durée d'écoute: durée=2s
% f0=1000Hz
% fréquence d'échantillonnage: fe=8000Hz
%
lambda=input('donner la valeur de lambda (1000 ou 2000):')
f0=1000;fe=8000;
duree=2;
t=(0:fe*duree-1)/fe;    % vecteur temps
theta=2*pi*f0*t+pi*lambda*t.^2;
x=cos(theta);
soundsc(x,fe)           % écoute du signal