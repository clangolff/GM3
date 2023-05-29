
c histogramme de a(n) en nb boites
c xb fronteires de boite
c k tableau travail pour where
      program hist
      implicit none
      integer :: n,ib,nb
      real, allocatable :: a(:), xb(:)
      integer, allocatable :: b(:)
      logical, allocatable :: mask(:)
      real  :: da,maxa,mina

      read(*,*) n, nb
      allocate(a(n))
      allocate(xb(nb + 1))
      allocate(b(nb))
      allocate(mask(n))
      
      read(*,*) a
      maxa = maxval(a)
      mina = minval(a)
      write(*,*) '#  ',  mina, maxa
      maxa = maxa
      mina = mina
      da  = (maxa-mina)/nb

cc      call random_number(a)
      
      do ib=0,nb
        xb(ib+1) = ib*da
        write(*,*) '#  ',xb(ib+1)
      enddo
      
      b = 0
      do ib=1,nb
        mask = (a < xb(ib + 1) .and. a > xb(ib)) 
        b(ib) = count(mask)
      enddo

      do ib=1,nb
        write (*,*) ib,0.5*(xb(ib+1)+xb(ib)),b(ib),b(ib)/(1.*n)
      enddo
      
      deallocate(a)
      deallocate(xb)
      deallocate(b)
      deallocate(mask)
      end 
      
