from collections import deque
from tree_node import *


def nodes_the_same(p, q):
    # if both are None
    if not p and not q:
        return True
    # one of p and q is None
    if not q or not p:
        return False
    if p.val != q.val:
        return False
    return True


class TreeAlgorithms:

    def do_level_traversal(self):
        tn = TreeNode.build_sample_tree2()
        result = self.show_tree_by_level(tn)
        print(result)
        return result

    def do_same_test(self):
        tn, tn2 = TreeNode.build_sample_tree1()
        result = self.is_same_tree(tn, tn2)
        print(result)
        return result

    @staticmethod
    def is_same_tree( p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        deq = deque([(p, q)])
        while deq:
            p, q = deq.popleft()
            if not nodes_the_same(p, q):
                return False

            if p:
                print(p.val)
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True

    @staticmethod
    def show_tree_by_level(root):

        result_array = []
        deq = deque([root])

        current_level = 0
        cnt = 0
        curr_list = []
        fact = 1
        while deq:

            curr = deq.popleft()
            if curr:
                curr_list.append(curr.val)

            cnt += 1

            next_level = float(cnt + 1) / float(fact)
            if next_level >= 2.0:
                fact = fact * 2.0
                result_array.append(curr_list)
                curr_list = []

            if curr:
                deq.append(curr.left)
                deq.append(curr.right)

        if curr_list:
            result_array.append(curr_list)

        return result_array




