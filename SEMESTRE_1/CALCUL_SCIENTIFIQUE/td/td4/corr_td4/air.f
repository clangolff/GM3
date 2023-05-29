      program air
      implicit none
      integer n
      parameter (n=3)
      real x(n),y(n),v(n),res
      read(*,*) x,y
c produit vectoriel  v=x^y
      call vprod(n,x,y,v)
c aire =sqrt((x^y).(x^y))
      res=sqrt(dot_product(v,v))
      write(*,*) res
      end
