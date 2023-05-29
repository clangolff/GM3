%--------------------
%inverse matrice triang <
%
%--------------------
function [ILM]= inve(L,n)
b = zeros(n,1); x = zeros(n,1);ILM=zeros(n,0);
for j=1 :n
   b(:)=0; b(j)=1;
   for i=1 :n
     x(i) = b(i)- L(i,1:i-1)*x(1:i-1);
   end
   ILM = [ILM x];
end


