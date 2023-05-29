clear;
n=20;
x=1.;
for i=1:n
  x = x/10.;
  fprintf('%6.2f  %30.20g \n', i,1+x)
%  fprintf('%6.2f  %12.5g \n', i,x)
end

