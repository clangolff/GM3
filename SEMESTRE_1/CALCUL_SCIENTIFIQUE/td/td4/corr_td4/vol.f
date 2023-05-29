      program vol
      implicit none
      integer, parameter:: n=3
      real x(n),y(n),z(n),v(n),res

      read(*,*) x,y,z
      call vprod(n,y,z,v)

c v=x.(y^z)
c valeur absolue pour éviter les résultats négatifs

      res=abs(dot_product(x,v))
      write(*,*) res
      end
