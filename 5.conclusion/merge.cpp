// Copyright 2021 aaaaaaaalesha

ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
    if (l1 == nullptr && l2 == nullptr) {
        return nullptr;
    }
    auto *out = new ListNode();

    ListNode *ptr = out;
    for (; l1 != nullptr && l2 != nullptr; ptr = ptr->next) {
        if (l1->val < l2->val) {
            ptr->val = l1->val;
            l1 = l1->next;
        } else {
            ptr->val = l2->val;
            l2 = l2->next;
        }

        if (l1 == nullptr && l2 == nullptr) {
            ptr->next = nullptr;
            continue;
        }
        ptr->next = new ListNode();
    }

    for (; l1 != nullptr; ptr = ptr->next) {
        ptr->val = l1->val;
        l1 = l1->next;

        if (l1 == nullptr) {
            ptr->next = nullptr;
            continue;
        }
        ptr->next = new ListNode();
    }

    for (; l2 != nullptr; ptr = ptr->next) {
        ptr->val = l2->val;
        l2 = l2->next;

        if (l2 == nullptr) {
            ptr->next = nullptr;
            continue;
        }
        ptr->next = new ListNode();
    }


    return out;
}
