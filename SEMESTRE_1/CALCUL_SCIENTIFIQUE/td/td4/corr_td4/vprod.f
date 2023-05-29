c calcule le produit vectoriel en dimension 3
c v=x^y      
      subroutine vprod(n,x,y,v)
      implicit none
      integer n
      real x(n),y(n),v(n)

      v(1)=x(2)*y(3)-x(3)*y(2)
      v(2)=x(3)*y(1)-x(1)*y(3)
      v(3)=x(1)*y(2)-x(2)*y(1)

      return 
      end
