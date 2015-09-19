#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;
struct RobotAgent{
    int x;
    int y;
    int direct;
};
int N, M, S, sticker;
RobotAgent BIMArobot;
char robotCmmd[50004];
char maps[104][104];
void NextDirection(char newDirection)
{
    int currentDirection = BIMArobot.direct;
    if( newDirection=='D' ){
        currentDirection++;
        if (currentDirection==5)
            currentDirection=1;
    }else if(newDirection=='E'){
        currentDirection--;
        if (currentDirection==0)
            currentDirection=4;
    }else{
        exit(0);
    }
    BIMArobot.direct = currentDirection;
}
void start_rally(int nextCmmd)
{
    int xm = BIMArobot.x;
    int ym = BIMArobot.y;
    if(maps[xm][ym]=='*'){
        sticker++;
        maps[xm][ym] = '.';
    }
    if(nextCmmd==S){
        return;
    }else{
        if( robotCmmd[nextCmmd]=='F' ){
            switch(BIMArobot.direct)
            {
                case 1:
                    if( BIMArobot.x>0 && maps[xm-1][ym]!='#' ){
                        BIMArobot.x--;
                    }
                    break;
                case 2:
                    if( BIMArobot.y<M && maps[xm][ym+1]!='#' ){
                        BIMArobot.y++;
                    }
                    break;
                case 3:
                    if( BIMArobot.x<N && maps[xm+1][ym]!='#' ){
                        BIMArobot.x++;
                    }
                    break;
                case 4:
                    if( BIMArobot.y>0 && maps[xm][ym-1]!='#' ){
                        BIMArobot.y--;
                    }
                    break;
            }
        }else{
            NextDirection(robotCmmd[nextCmmd]);
        }
        start_rally(nextCmmd+1);
    }
}
void prepare_and_play()
{
    int found = 0;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            switch(maps[i][j])
            {
                case 'N':
                    BIMArobot.x = i;
                    BIMArobot.y = j;
                    BIMArobot.direct = 1; found = 1;
                    break;
                case 'L':
                    BIMArobot.x = i;
                    BIMArobot.y = j;
                    BIMArobot.direct = 2; found = 1;
                    break;
                case 'S':
                    BIMArobot.x = i;
                    BIMArobot.y = j;
                    BIMArobot.direct = 3; found = 1;
                    break;
                case 'O':
                    BIMArobot.x = i;
                    BIMArobot.y = j;
                    BIMArobot.direct = 4; found = 1;
                    break;
            }
            if (found>0){
                break;
            }
        }
    }
}
main()
{
    for(;;) {
        scanf("%d %d %d", &N, &M, &S);
        if(N==0 || N==0 || S==0){
            exit(0);
        }
        for(int i = 0; i < N; i++){
            scanf("%s",maps[i]);
        }
        scanf("%s",robotCmmd);
        sticker = 0;
        prepare_and_play();
        start_rally(0);
        printf("%d\n", sticker);
    }
    return 0;
}
