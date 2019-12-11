import inspect
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class OutputPort:
    op: "Op"
    output_index: int


@dataclass
class InputPort:
    op: "Op"
    input_index: int
    src_port: OutputPort = None


class Op(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        ...

    @property
    @abstractmethod
    def output(self) -> OutputPort:
        ...


class FuncOp(Op):
    def __init__(self, func):
        self.func = func
        self.spec = inspect.getfullargspec(func)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    @property
    def output(self) -> OutputPort:
        return OutputPort(self, 0)

    def __getattr__(self, item) -> InputPort:
        if item in self.spec.args:
            return InputPort(self, self.spec.args.index(item))
        else:
            raise RuntimeError


class OpClass:
    def __init__(self, func):
        self.func = func

    def op(self) -> Op:
        return FuncOp(self.func)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


def op_class(func) -> OpClass:
    return OpClass(func)


def op(func) -> Op:
    return FuncOp(func)
