#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n,q,k,x,mid;
	scanf("%d", &n);
	int *a = (int*)malloc(sizeof(int)*n);
	for (int i = 0; i < n; i++) scanf("%d", &a[i]);
		scanf("%d", &q);
	int *b = (int*)malloc(sizeof(int)*q);
	for (int i = 0; i < q; i++) scanf("%d", &b[i]);
		int low = 0, high = n - 1;
		for (int i = 0; i < q; i++)
		{
			while (low <= high)
			{
				mid = (low + high) / 2;
				if (a[mid] < b[i])
					low = mid + 1;
				else if (a[mid] > b[i])
					high = mid - 1;
				else if (a[mid] == b[i])
				{
					x = mid + 1;
					break;
				}
			}
			if (low > high)
			{
				x = n;
			}
			int sum = 0;
			for (int i = 0; i <x; i++)
			{
				sum += a[i];
			}
			printf("%d %d", x, sum);
			printf("\n");
		}
	
	system("pause");
	return 0;
}