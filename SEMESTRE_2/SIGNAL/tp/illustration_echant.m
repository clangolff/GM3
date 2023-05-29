% Illustration du théorème d'échantillonnage
%
%
% x(t)=cos(2*pi*f0*t)  % f0=200Hz
% fe1=500Hz     % sur-échantillonnage
% fe2=250Hz     % sous-échantillonnage
% duree=0.1 s
%
f0=200;
fe1=500; fe2=250;
duree=0.1;
%
Te1=1/fe1;Te2=1/fe2;                % périodes d'échantillonnage
ne1=duree/Te1+1;ne2=duree/Te2+1;    % nombre d'échantillons
%
t1=[0:ne1-1]/fe1;       % valeurs temporelles des échantillons pour fe1
t2=[0:ne2-1]/fe2;        % valeurs temporelles des échantillons pour fe2
%
x1=cos(2*pi*f0*t1);     % échantillons pour fe1
x2=cos(2*pi*f0*t2);     % échantillons pour fe2
%
% interpolation: signal continu
K=40;
Ti1=Te1/K;Ti2=Te2/K;
ni1=duree/Ti1+1;ni2=duree/Ti2+1;    % nombre de points du signal continu
%
ti1=[0:ni1-1]*Ti1;
ti2=[0:ni2-1]*Ti2;
%
xi1=cos(2*pi*f0*ti1);       % signal continu
xi2=cos(2*pi*f0*ti2);       % signal continu
%
 subplot(2,1,1),stem(t1,x1)
hold on
plot(ti1,xi1,'r')
hold off
title('sinusoide à f0=200Hz échantillonnée à 500Hz')
subplot(2,1,2),stem(t2,x2)
hold on
plot(t2,x2,'r')
hold off
title('sinusoide à 200HZ échantillonnée à 250Hz')
%



