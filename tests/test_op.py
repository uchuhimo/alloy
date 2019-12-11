import alo
from alo import InputPort, Op, OutputPort


def add(x, y, z=1):
    return x + y + z


def test_func_op():
    op = alo.op(add)
    assert isinstance(op, Op)
    assert (
        isinstance(op.x, InputPort)
        and op.x.op == op
        and op.x.input_index == 0
        and op.x.src_port is None
    )
    assert (
        isinstance(op.y, InputPort)
        and op.y.op == op
        and op.y.input_index == 1
        and op.y.src_port is None
    )
    assert (
        isinstance(op.output, OutputPort)
        and op.output.op == op
        and op.output.output_index == 0
    )
