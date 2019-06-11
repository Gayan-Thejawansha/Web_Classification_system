#include <stdio.h>
int main(int argn, char ** args)
{
    char line[20000];
    int i, j;

  //  char * fileName=args[1];   // printf("%s",fileName);
    FILE *fOp=fopen(args[1],"r");
    gets(line);
    for(i = 0; line[i] != '\0'; ++i)
    {
        while (!( (line[i] >= 'a' && line[i] <= 'z') || line[i] ==' ' || (line[i] >= 'A' && line[i] <= 'Z') || line[i] == '\0') )
        {
            for(j = i; line[j] != '\0'; ++j)
            {
                line[j] = line[j+1];
            }
            line[j] = '\0';
        }
    }

    puts(line);
    return 0;
}
