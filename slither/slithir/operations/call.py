from typing import Optional, List, Union

from slither.core.declarations import Function
from slither.core.variables import Variable
from slither.slithir.operations.operation import Operation


class Call(Operation):
    def __init__(self) -> None:
        super().__init__()
        self._arguments = []

    @property
    def arguments(self):
        return self._arguments

    @arguments.setter
    def arguments(self, v):
        self._arguments = v

    # pylint: disable=no-self-use
    def can_reenter(self, _callstack: Optional[List[Union[Function, Variable]]] = None) -> bool:
        """
        Must be called after slithIR analysis pass
        :return: bool
        """
        return False

    def can_send_eth(self) -> bool:  # pylint: disable=no-self-use
        """
        Must be called after slithIR analysis pass
        :return: bool
        """
        return False
