import os
import pathlib

from .. import base


__filedir__ = os.path.dirname(
   os.path.realpath(__file__)
)

class FileDataset(base.BaseFileDataset):
    def __init__(self, base_path: str | bytes | os.PathLike):
        self.base_path = pathlib.Path(base_path)

    @property
    def datas(self):
        return self.base_path / 'datas'

    @property
    def models(self):
        return self.base_path / 'models'

    @property
    def weathers(self):
        return self.base_path / 'weathers'

dataset = FileDataset(pathlib.Path(__filedir__) / 'assets')

__all__ = [
    FileDataset,
    dataset,
]
