c histogramme de a(n) en nb boites
c xb fronteires de boite
c k tableau travail pour where


      program hist
      implicit none
      integer :: n,ib,nb
      real, allocatable :: a(:), xb(:)
      integer, allocatable :: b(:), k(:)
      real  :: db,maxa,mina

      read(*,*) n, nb
      allocate(a(n))
      allocate(xb(nb + 1))
      allocate(b(nb))
      allocate(k(n))
     
      read(*,*) a 
      maxa = maxval(a)
      mina = minval(a)
      write(*,*) '#  ',  mina, maxa
      maxa = maxa
      mina = mina
      db  = (maxa-mina)/nb

cc      call random_number(a)
     
c frontieres boite 
      do ib=0,nb
        xb(ib+1) = mina+ ib*db
        write(*,*) '#  ',xb(ib+1)
      enddo
     
c histogramme 
      b = 0
      do ib=1,nb
        k = 0
        where (a < xb(ib + 1) .and. a > xb(ib))
          k = 1
        end where
        b(ib) = sum(k)
      enddo

      do ib=1,nb
        write (*,*) ib,0.5*(xb(ib+1)+xb(ib)),b(ib),b(ib)/(1.*n)
      enddo
      
      deallocate(a)
      deallocate(xb)
      deallocate(b)
      end 
      
