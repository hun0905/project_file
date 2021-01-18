struct link{
    char c;
    struct link *next;
};
int lengthOfLongestSubstring(char * s){
    struct link *sub_s,*tmp,*head,*middle;
    bool add = 1;  
    int max,count;
    sub_s = malloc(sizeof(struct link));
    head = sub_s;
    middle = sub_s;
    count = 0;
    max = 0;
    sub_s->next = NULL;
    for(int l = 0; l < strlen(s); l++){
        count = 0;
        for(int i = l ; i < strlen(s); i++){
            for(struct link *j = middle ; j ->next != NULL && add != 0; j = j->next){
                if(j->c == s[i]){
                    add = 0;
                    i = strlen(s);
                    //count = 0;
                }
            }
            if(add == 1){
                tmp = malloc(sizeof(struct link));
                sub_s -> c = s[i];
                sub_s->next = tmp; 
                sub_s = sub_s->next;
                sub_s->next = NULL;
                count++;
            }
            else{
                middle = sub_s;
                count = 0;
            }
            if(count > max)
                max = count;
            add=1;
        }
    }
    struct link *i = head ;
    /*while(i -> next != NULL){
        tmp = i;
        i = i -> next;
        free(tmp);
    }*/
    return max;
}