import node as n
import linked_list as ll


if __name__ == "__main__":
    one = n.Node("once")
    two = n.Node("upon")
    three = n.Node("a")
    four = n.Node("time")
    one.next_node = two
    two.next_node = three
    three.next_node = four

    head_of_node = ll.LinkedList(one)

    #Reading list
    current_node = head_of_node.first_node
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next_node
    
    head_of_node.read_index(1)
    head_of_node.index_of("a")
    head_of_node.insert_value(2, "Z")

    head_of_node.delete_node(0)