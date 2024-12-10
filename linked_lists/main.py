import node as n
import linked_list as ll


if __name__ == "__main__":
    one = n.Node("once")
    two = n.Node("upon")
    three = n.Node("a")
    four = n.Node("time")
    one.next = two
    two.next = three
    three.next = four

    head_of_node = ll.LinkedList(one)

    #Reading list
    head_of_node.traverseList()
    
    value_to_find = "a"
    node_to_delete = 0
    print("Index 1 is" , head_of_node.read_index(1))
    print("The index of {} is {}".format(value_to_find, head_of_node.index_of(value_to_find)))
    print("If we inset the value {} at index {}".format("Z", 2))
    head_of_node.insert_value(2, "Z")
    head_of_node.traverseList()
    print("If we delete the data at index {}, here is the resulting linked list".format(node_to_delete))
    head_of_node.delete_node(node_to_delete)
    head_of_node.traverseList()
    print("We will be reversing the linked list")
    head_of_node.reverseLinkedList()
    print("Linked list after reversing")
    head_of_node.traverseList()
    ###Numbers
    one_number = n.Node(1)
    two_number = n.Node(1)
    one_number.next = two_number
    third_number = n.Node(2)
    fourth_number = n.Node(4)
    third_number.next = fourth_number