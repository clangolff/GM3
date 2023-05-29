      program ang
      implicit none
      integer n
      parameter (n=3)
      real x(n),y(n),cosi,nx,ny,res,res2
      read(*,*) x,y
c norme, sqrt(x.x)
      nx=sqrt(dot_product(x,x))
      ny=sqrt(dot_product(y,y))
c cos(x,y)=(x.y)/(sqrt(x.x)*sqrt(y.y))
      cosi=dot_product(x,y)/(nx*ny)
      res=acos(cosi)
c angle en degrés 
      res2=res*180/(4*atan(1.0))
      write(*,*) 'en radians'
      write(*,*) res
      write(*,*) 'en degres'
      write(*,*) res2
      end
