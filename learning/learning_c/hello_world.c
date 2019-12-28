# include <stdio.h>
# include
int main()
{
	char message[255];
	printf("Message: ");
	scanf("%S[0-9a-zA-Z ]", message);
	printf("%s\n", message);
	return(0);
}

