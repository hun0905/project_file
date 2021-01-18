/**
 * Definition for singly-linked list.{
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* i,* j,*tmp,*head,* k ;
    int carry = 0;;
    tmp = malloc(sizeof(struct ListNode));
    head = malloc(sizeof(struct ListNode));
    head = tmp;
    tmp->next = NULL;
    i = l1;
    j = l2;
    while(i!=NULL || j!=NULL){
        if(i  != NULL && j  != NULL){
        tmp->val = (i->val + j->val+carry)%10;
        carry = (i->val + j->val+carry)/10;
        }
        else if(i  != NULL && j  == NULL){
            tmp->val = (i->val + carry)%10;
            carry = (i->val+carry)/10;
        }
        else{
            tmp->val = (j->val + carry)%10;
            carry = (j->val+carry)/10;
        }
        if(i != NULL)
            i = i->next;
        if(j !=NULL)
            j = j->next;
        if(i != NULL  || j  != NULL){
        
            k = malloc(sizeof(struct ListNode));
            tmp -> next = k;
            k->next = NULL;
            tmp = tmp->next;    
        } 
    }
    if(carry == 1){
        k = malloc(sizeof(struct ListNode));
        tmp -> next = k;
        k->next = NULL;
        tmp = tmp->next;    
        tmp->val = 1;
    }
    return head;   
}