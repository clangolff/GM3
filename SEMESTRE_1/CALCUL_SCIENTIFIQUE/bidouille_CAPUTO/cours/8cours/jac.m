
%------------------------
%Jacobi iteration for A X = b
% x^{k+1} = F x^k + G
%
% F = -(L+U)    ;  G = D^{-1} b
%
% where A= D( L + I + U) 
%------------------------
clear all;
tol=1.e-12;imax = 60;
n=5; w=1;
%A=[ 2 0 1
    %2 5 -1
    %1 -1 3];
%b=[1 1 1]';
A = hilb(n)+ w*eye(n);b=sum(A,2);
F= zeros(n);
x0=zeros(n,1);x1=zeros(n,1);

%preparation
D1= 1./diag(A);
DM1=diag(D1);
F = eye(n)-DM1*A;
G= DM1*b;
%iteration
x0=1;
for i=1:imax
   x1 = F*x0 +G;
   res= norm(x1-x0);
   if (res < tol)
	   break;
   end
   res1= norm(A*x1-b);
   fprintf('%2d    %7.4e   %7.4e \n',i,res,res1);
   x0=x1;
end


