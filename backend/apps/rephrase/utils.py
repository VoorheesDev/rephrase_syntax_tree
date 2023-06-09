from itertools import permutations
from typing import Generator

from nltk.tree import ParentedTree, Tree

NP = "NP"


def make_ptree(s: str) -> ParentedTree:
    return ParentedTree.convert(Tree.fromstring(s))


def rephrased_ptree_generator(
    ptree: ParentedTree, initial_ptree: ParentedTree, start_from: tuple[int] = ()
) -> Generator[ParentedTree, None, None]:
    # stop when reach the leaf value
    try:
        ptree.label()
    except AttributeError:
        return

    cur_pos = ptree.treeposition()
    if ptree.label() == NP and cur_pos > start_from:
        inner_np_trees = {
            subtree.treeposition(): subtree for subtree in ptree if subtree.label() == NP
        }
        if len(inner_np_trees) > 1:
            for perm in list(permutations(inner_np_trees.values()))[1:]:  # get only unique perms
                new_tree = initial_ptree.copy(deep=True)
                for idx, key in enumerate(inner_np_trees):
                    # to be able to set a new subtree: copy subtree to get rid of `parent` param
                    new_tree[key] = perm[idx].copy(deep=True)
                yield new_tree
                # also paraphrase trees from `new_tree` if there are some NPs left after current pos
                yield from rephrased_ptree_generator(new_tree, new_tree, cur_pos)

    for node in ptree:
        yield from rephrased_ptree_generator(node, initial_ptree, start_from)


def generate_rephrased_ptrees(ptree: ParentedTree, limit: int = 20) -> list[ParentedTree]:
    rephrased_ptrees = []
    generator = rephrased_ptree_generator(ptree, ptree)
    i = 1
    while i <= limit:
        try:
            rephrased_ptrees.append(next(generator))
        except StopIteration:
            break
        i += 1
    return rephrased_ptrees


def convert_ptree_to_str(ptree: ParentedTree) -> str:
    return " ".join(str(ptree).split())
