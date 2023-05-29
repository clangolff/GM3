%------------------------
%Gauss Seidel iteration for A X = 2
% x^{k+1} = BG x^k + C
%
% BG = -(L+I)^(-1)*U     ;  C = (L+I)^(-1) *D^{-1} b
%
% where A= D( L + I + U) 
%------------------------
clear all;
tol=1.e-12;imax = 120;
%n=3;
%A=[ 2 0 3
    %2 5 -1
    %1 -1 3];
%b=[1 1 -1]';
n=5;
A=[2.0000    0.5000    0.3333    0.2500    0.2000
0.5000    1.3333    0.2500    0.2000    0.1667
0.3333    0.2500    1.2000    0.1667    0.1429
0.2500    0.2000    0.1667    1.1429    0.1250
0.2000    0.1667    0.1429    0.1250    1.1111];
b=sum(A,2);
L= zeros(n); U= zeros(n);

%preparation
D = diag(diag(A));
D1= 1./diag(A);
DM1=diag(D1);
DMA = DM1*A;
L = tril(DMA);
L= L -diag(diag(L));
U = triu(DMA);
U= U -diag(diag(U));
IL = eye(n)+L ;
[ILM]= inve(IL,n);
BG = -ILM * U;
C= ILM *DM1*b;

%iteration
x0=zeros(n,1);x1=zeros(n,1);
x0=rand(n,1);
for i=1:imax
   x1 = BG*x0 +C;
   res= norm(x1-x0);
   if (res < tol)
	   break;
   end
   res1= norm(A*x1-b);
   fprintf('%2d    %7.4e   %7.4e \n',i,res,res1);
   x0=x1;
end
