/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head){
    
    struct ListNode* temp = head;
    struct ListNode* stack = NULL;
        
    while(temp){
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = temp->val;
        node->next = stack;
        stack = node;
        temp = temp->next;
    }
    temp = head;
    
    while(temp){
        if(temp->val != stack->val) return false;
        temp = temp->next;
        stack = stack->next;
    }
    return true;
    
        

}