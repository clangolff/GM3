clear;
% a matrice 5 5
a = rand(5);
for j=1,3
   [M,I] = max(a(:))
   [I_row, I_col] = ind2sub(size(a),I)
 %  write(*,*) maxloc(a),maxval(a)
 %        write(*,*) k(1),k(2),a(k(1),k(2))
 %        a(k(1),k(2))=-10000.
enddo

deallocate(a)
deallocate(b)

end 
      
