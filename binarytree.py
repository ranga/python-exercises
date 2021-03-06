def leftchild(node):
    """Returns the left child of the given node.
    If the left child is absent, None is returned.
    """
    return node[0]

def rightchild(node):
    """Returns the right child of the given node.
    If the right child is absent, None is returned.
    """
    return node[2]

def getvalue(node):
    """Return the node value."""
    return node[1]

def makenode(value, left=None, right=None):
    """Creates a node with given value and left and right children.

    >>> a = makenode(1, makenode(2), makenode(3))
    >>> getvalue(a)
    1
    >>> getvalue(leftchild(a))
    2
    >>> getvalue(rightchild(a))
    3
    """
    return [left, value,right]

def is_leaf(node):
    """Tests whether a node is leaf.

    >>> a = makenode(1, makenode(2), None)
    >>> is_leaf(a)
    False
    >>> is_leaf(leftchild(a))
    True
    """
    return leftchild(node) is None and rightchild(node) is None

def leafcount(root):
    """Computes number of leaf nodes in a binary tree.

        >>> leafcount(makenode(1))
        1
        >>> leafcount(makenode(1, makenode(2), makenode(3)))
        2
    """
    if root is None:
        return 0
    elif is_leaf(root):
        return 1
    else:
        return leafcount(leftchild(root)) + leafcount(rightchild(root))


def deepest_node(node):
    """
    here lc & rc means left & rightchilds
    """
    lc = leftchild(node)
    rc = rightchild(node)
    if ((lc and len(lc)) or 0) > ((rc and len(rc)) or 0):
        return lc
    else:
        return rc

def treeheight(tree):
    """
    >>> treeheight(makenode(1))
    1
    >>> a = makenode(1, makenode(2), makenode(3, makenode(4), None))
    >>> treeheight(a)
    3
    >>> treeheight(leftchild(a))
    1
    >>> treeheight(rightchild(a))
    2
    """
    if leftchild(tree) is None and rightchild(tree) is None:
        return 1
    else:
        return 1 + treeheight(deepest_node(tree))

def preorder_traversal(tree):
    """
    In preorder traversal first it returns root,left and right values 
    >>> a = makenode(1, makenode(2), makenode(3, makenode(4), None))
    >>> preorder_traversal(a)
    [1, 2, 3, 4]
    >>> a = makenode(1, makenode(2, makenode(4),makenode(5)), makenode(3, makenode(6), makenode(7)))
    >>> preorder_traversal(a)
    [1, 2, 4, 5, 3, 6, 7]
    """
    if tree is None:
        return []
    else:
        return [getvalue(tree)] + preorder_traversal(leftchild(tree)) + preorder_traversal(rightchild(tree))

def postorder_traversal(tree):
    """
    In postorder traversal first it returns left,right and root values
    >>> a = makenode(1, makenode(2), makenode(3, makenode(4), None))
    >>> postorder_traversal(a)
    [2, 4, 3, 1]
    >>> a = makenode(1, makenode(2, makenode(4),makenode(5)), makenode(3, makenode(6), makenode(7)))
    >>> postorder_traversal(a)
    [4, 5, 2, 6, 7, 3, 1]
    """
    if tree is None:
        return []
    else:
        return postorder_traversal(leftchild(tree)) + \
            postorder_traversal(rightchild(tree)) + \
            [getvalue(tree)]

def inorder_traversal(tree):
    """
    In inorder traversal first it returns left,root and right values
    >>> a = makenode(1, makenode(2), makenode(3, makenode(4), None))
    >>> inorder_traversal(a)
    [2, 1, 4, 3]
    >>> a = makenode(1, makenode(2, makenode(4),makenode(5)), makenode(3, makenode(6), makenode(7)))
    >>> inorder_traversal(a)
    [4, 2, 5, 1, 6, 3, 7]
    """
    if tree is None:
        return [] 
    else:
        return inorder_traversal(leftchild(tree)) + \
            [getvalue(tree)] + \
            inorder_traversal(rightchild(tree))

def inorder_traversal_list(tree):
    """
    The above implementation of inorder_traversal is very inefficient because it creates many temporary lists so we improve the performance of that function by appending values to a single list.
    >>> a = makenode(1, makenode(2), makenode(3, makenode(4), None))
    >>> inorder_traversal_list(a)
    [2, 1, 4, 3]
    >>> a = makenode(1, makenode(2, makenode(4),makenode(5)), makenode(3, makenode(6), makenode(7)))
    >>> inorder_traversal_list(a)
    [4, 2, 5, 1, 6, 3, 7]
    """
    inorder = []
    if tree is None:
        return []
    else:
        inorder.extend(inorder_traversal_list(leftchild(tree)))
        inorder.append(getvalue(tree))
        inorder.extend(inorder_traversal_list(rightchild(tree)))
        return inorder

def hight(tree):
    """
    >>> a = makenode(1, makenode(2, makenode(4),makenode(5)), makenode(3, makenode(6), makenode(7)))
    >>> hight(a)
    2
    >>> a = makenode(1, makenode(2), None)
    >>> hight(a)
    1
    """

    if tree is None:
        return -1
    else:
        return max(hight(leftchild(tree)),hight(rightchild(tree))) + 1

def binary_search_tree(tree, key):
    """
    >>> a = makenode(1, makenode(2), makenode(3, makenode(4), None))
    >>> binary_search_tree(a, 3)
    3
    >>> binary_search_tree(a,1)
    1


    """
    if tree is None:
        return []
    if key < getvalue(tree):
        return binary_search_tree(leftchild(tree), key)
    elif key > getvalue(tree):
        return binary_search_tree(rightchild(tree), key)
    else:
        return getvalue(tree)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
