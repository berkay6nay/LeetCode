/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    
    
    struct ListNode* i1 = headA;
    struct ListNode* i2 = headB;
    
    
    
    while(i1){
        
        while(i2){
            
            if(i1 == i2){
                return i1;
            }
            
            i2 = i2->next;
            
            
        }
        
        i2 = headB;
        i1 = i1->next;
        
        
    }
    
    return NULL;
}