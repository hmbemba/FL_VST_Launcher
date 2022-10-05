
from dataclasses import dataclass, field
from typing import Any, List
from abc import ABCMeta, abstractmethod

@dataclass
class xx(metaclass=ABCMeta):
    _: List = field(default_factory=lambda: [])

    @abstractmethod
	def foo(self):
		pass

@dataclass
class xx:
    _: List = field(default_factory=lambda: [])
    