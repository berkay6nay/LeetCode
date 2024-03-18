/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int getDecimalValue(struct ListNode* head){
    
    int coef = 1;
    int output = 0;
    int length = 0;
    struct ListNode *iterator = head;
    
    while(iterator){
        length = length + 1;
        iterator = iterator->next;
        }
    iterator = head;
    coef = pow(2 , length - 1);
    while(iterator){
        if(iterator->val == 1){
            output += coef;
        }
        coef = coef/2;
        iterator = iterator->next;
    }
    return output;
    
    
    }
    
    

