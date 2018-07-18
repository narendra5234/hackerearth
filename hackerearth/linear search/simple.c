
#include <stdio.h>

int main(){
	int n,x,c=0;
	scanf("%d", &n);
	int *a=(int *)malloc(sizeof(int)*n);
	for(int i=0;i<n;i++)scanf("%d",&a[i]);
	scanf("%d",&x);
	for(int i=0;i<n;i++)
	{
	   if(x==a[i])
	    {
	        printf("%d",i);
	        break;
	    }
	    //else c++;
	}
	//if(c==n) printf("-1");
	return 0;
}


