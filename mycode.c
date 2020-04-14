#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define ROWSIZE 5030
#define COLSIZE 3
#define ROW 20

typedef struct{
    int data;
    int* list;
}Node,*List;

void loadfile(char* filename,int** data){

    int ch;  //用来存储文件结尾的EOF
    //读文件
    FILE* fp;

    char *buff= (char*)malloc(sizeof(char*)*ROW);
    
    //open
    fp = fopen(filename,"r");
    //读取失败：
    if(fp==NULL){
        printf("Failed to open the file which is named %s",filename);
        exit(1);
    }
    int i=0;
    while(fgets(buff,ROW,fp))
    {
        
        char *token = strtok(buff,",");
        int j=0;
        while(token!=NULL)
        {
            data[i][j] = atoi(token);
            token = strtok(NULL,",");
            j++;
        }
        i++;
    }
    fclose(fp);
    if(fclose(fp)!=0)
    {
        printf("Error in closing file");
    }
}



int main(int argc, char const *argv[])
{
    char* filename = "test_data.txt";

    int **data = (int**)malloc(ROWSIZE*sizeof(int*));
    for(int i=0;i<ROWSIZE;i++)
    {
        data[i] = (int*)malloc(COLSIZE*sizeof(int));
    }
    loadfile(filename,data);
    printf("%d,%d,%d\n",data[0][0],data[0][1],data[0][2]);
    /* code */
    return 0;
}
