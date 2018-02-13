from src import trie, rlp

(
    NODE_TYPE_BLANK,
    NODE_TYPE_LEAF,
    NODE_TYPE_EXTENSION,
    NODE_TYPE_BRANCH
) = tuple(range(4))


def traverse(hash, tab=0):
    if not hash:
        return
    if type(hash) is list:
        return
    node = state._decode_to_node(hash)
    node_type = state._get_node_type(node)
    node_type_str = ''
    if node_type == NODE_TYPE_BLANK:
        node_type_str = 'BLNK'
    elif node_type == NODE_TYPE_BRANCH:
        node_type_str = 'BRCH'
    elif node_type == NODE_TYPE_EXTENSION:
        node_type_str = 'EXTN'
    elif node_type == NODE_TYPE_LEAF:
        node_type_str = 'LEAF'
    print_node(node, hash.encode("hex"), node_type_str, tab)

    if node_type == NODE_TYPE_EXTENSION:
        traverse(node[1], tab=tab+1)
    elif node_type == NODE_TYPE_LEAF:
        pass
    elif node_type == NODE_TYPE_BRANCH:
        for n in node[:15]:
            traverse(n, tab=tab+1)


def print_node(node, hash, node_type_str, tab=0):
    print "{0}[{1}][{2}]{3}".format(" "*tab, node_type_str, hash, [n.encode('hex') if type(n) is not list and len(n) == 32 else n for n in node]).upper()


print 'x01x01x02', ['VALUE_010102']
state = trie.Trie('triedb', trie.BLANK_ROOT)
state.update('\x01\x01\x02', rlp.encode(['VALUE_010102']))
traverse(state.root_hash)
print "=" * 100

print 'x01x01x02', ['VALUE_010102']
state.update('\x01\x01\x02', rlp.encode(['VALUE_010102_REPLACE']))
traverse(state.root_hash)


print "=" * 100

print 'x01x01x03', ['VALUE_010103']
state.update('\x01\x01\x03', rlp.encode(['VALUE_010103']))
traverse(state.root_hash)

print "=" * 100

print 'x01x01', ['VALUE_0101']
state.update('\x01\x01', rlp.encode(['VALUE_0101']))
traverse(state.root_hash)
print "=" * 100

print 'x01x01x02x55', ['VALUE_01010255']
state.update('\x01\x01\x02\x55', rlp.encode(['VALUE_01010255']))
traverse(state.root_hash)
print "=" * 100

print 'x01x01x02x57', ['VALUE_01010257']
state.update('\x01\x01\x02\x57', rlp.encode(['VALUE_01010257']))
traverse(state.root_hash)
print "=" * 100


print 'x01x01x03x57', ['VALUE_01010357']
state.update('\x01\x01\x03\x57', rlp.encode(['VALUE_01010357']))
traverse(state.root_hash)
print "=" * 100

print rlp.decode(state.get('\x01\x01'))
print rlp.decode(state.get('\x01\x01\x02'))
print rlp.decode(state.get('\x01\x01\x03'))
print rlp.decode(state.get('\x01\x01\x02\x55'))
print rlp.decode(state.get('\x01\x01\x02\x57'))
print rlp.decode(state.get('\x01\x01\x03\x57'))


