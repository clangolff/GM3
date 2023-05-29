Fe=100;
t=linspace(0,512/Fe,512);
% f=linspace(-Fe/2,Fe/2,length(m));


% N=1001;
% Fe=100;
% t=[0:N-1]/Fe;


% 0<f0<fe/2
x=sin(2*pi*5*t);
figure
plot(t(1:20),x(1:20))
hold on

%axe_freq=(0:N-1)*Fe/N;
%X=abs(fftshift(fft(x)));
%plot(X)
%
% fe/2<f0<fe
x1=sin(2*pi*60*t);
plot(t(1:20),x1(1:20),'r')
hold on
%
% fe<f0<3fe/2
x2=sin(2*pi*110*t);

plot(t(1:20),x2(1:20),'y')
hold on
% 3fe/2<f0<2fe
x3=sin(2*pi*170*t);

plot(t(1:20),x3(1:20),'g')
hold off
%
% représentation en fréquence
f=linspace(-Fe/2,Fe/2,length(x));

 
X=abs(fftshift(fft(x)));
X1=abs(fftshift(fft(x1)));
X2=abs(fftshift(fft(x2)));
X3=abs(fftshift(fft(x3)));
figure
plot(f,X),hold on
plot(f,X1,'r'),hold on
plot(f,X2,'y'),hold on
plot(f,X3,'g'),hold off
