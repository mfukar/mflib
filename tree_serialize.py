#!/usr/bin/env python
# @file        C:\Documents and Settings\mfoukara\tree_serialize.py
# @author      Michael Foukarakis
# @version     1.0
# @date        Created:     Tue Oct 25, 2011 12:46 GTB Daylight Time
#              Last Update: Δευ Οκτ 13, 2014 18:03 GTB Daylight Time
#------------------------------------------------------------------------
# Description: Tree serialization routines
#------------------------------------------------------------------------
# History:     <+history+>
# TODO:        <+missing features+>
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------

def serialize_tree(root_node):
    """ Given a tree root node (some object with a 'data' attribute and a 'children'
    attribute which is a list of child nodes), serialize it to a list, each element of
    which is either a pair (data, has_children_flag), or None (which signals an end of a
    sibling chain).
    """
    lst = []
    def serialize_aux(node):
        # Recursive visitor function
        if len(node.children) > 0:
            # The node has children, so:
            #  1. add it to the list & mark that it has children
            #  2. recursively serialize its children
            #  3. finally add a null entry to signal that the children
            #     of this node have ended
            lst.append((node.data, True))
            for child in node.children:
                serialize_aux(child)
            lst.append(None)
        else:
            # The node is child-less, so simply add it to
            # the list & mark that it has no chilren
            lst.append((node.data, False))
    serialize_aux(root_node)
    return lst

def deserialize_tree(nodelist):
    """ Expects a node list of the form created by serialize_tree.  Each entry in the list
    is either None or a pair of the form (data, has_children_flag).
    Reconstruct the tree back from it and return its root node.
    """
    # The first item in the nodelist represents the tree root
    root = TreeNode(nodelist[0][0])
    parentstack = [root]
    for item in nodelist[1:]:
        if item is not None:
            # This node is added to the list of children of the current parent.
            node = TreeNode(item[0])
            parentstack[-1].children.append(node)
            if item[1]: # has children?
                parentstack.append(node)
        else:
            # end of children for current parent
            parentstack.pop()
    return root
