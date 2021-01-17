/**
 * Definition for singly-linked list.{
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* i,* j,*ans,*head;
    
    ans = malloc(sizeof(struct ListNode));
    head = malloc(sizeof(struct ListNode));
    head = ans;
    ans->next = NULL;
    int num1=0,num2=0,b = 1;
    for(i = l1;i != NULL;i=i->next){
        num1+=(i->val)*b;
        b*=10;
    }
    b=1;
    for(j = l2;j != NULL;j=j->next){
        num2+=(j->val)*b;
        b*=10;
    }
    struct ListNode* k ;
    num1 +=num2;
    while(num1!=0){
            ans->val = num1%10;
            num1/=10;
            if(num1 != 0){
                k = malloc(sizeof(struct ListNode));
                ans -> next = k;
                k->next = NULL;
                ans = ans->next;
            }
            
    }
    //printf("%d",head->next->val);
    return head;   
}