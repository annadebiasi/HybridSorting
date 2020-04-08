"""
PROJECT 3 - Quick/Insertion Sort
Name:
PID:
"""


def _insertion_wrapper(insertion_sort):
    """
    DO NOT EDIT
    :return:
    """
    def insertion_counter(*args, **kwargs):
        if args[0].size > 1:
            args[0].c += 1
        insertion_sort(*args, **kwargs)
    return insertion_counter

# ------------------------Complete function below---------------------------
@_insertion_wrapper
def insertion_sort(dll, low, high):
    pass
