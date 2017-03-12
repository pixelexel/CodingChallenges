#include <stdio.h>


void main()
{
  int T,i,N,a[100000],j,cost,counter,k;

  scanf("%d", &T);
  for(i=0;i<T;i++)
  {
      counter=0;
      cost=0;
      k=0;
      scanf("%d", &N);
      for(j=0;j<N;j++)
      {
        scanf("%d", &a[j]);
      }
      while(k!=N)
      {

        if(a[k]==0)
        {
          cost += 1100;
          counter++;
        }
        else{
          if(counter!=0)
          {
            cost += 100;
            counter--;
          }
        }
        k++;
      }

      printf("\n%d", cost);


      }
  }
