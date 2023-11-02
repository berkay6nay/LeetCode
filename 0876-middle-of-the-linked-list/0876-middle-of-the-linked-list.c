/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    
    struct ListNode* temp = head;
    
    int length = 0;
    
    while(temp){
        length += 1;
        temp = temp->next;
    }
    temp = head;
    
    int middle_node = length/2 + 1;
    int flag = 1;
    
    while(temp){
        if(flag == middle_node) return temp;
        flag += 1;
        temp = temp->next;
    }
    
    return NULL;
}