function [x] = inve(l,n)
b=eye(n);x=zeros(n);
for i=1:n
 x(i,:)=(b(i,:)-l(i,1:i-1)*x(1:i-1,:) )/l(i,i);
end

