''' We create a sample class '''
from typing import List, Dict, Callable
from pathlib import Path
from glob import glob

class Sample:
    def __init__(self, name, tag, where, branches, selec = None, isdata = False, files = None):
        self._name = name
        self._tag = tag if isinstance(tag, list) else [tag]
        self._location = [Path(direc) for direc in where] if isinstance(where, list) else [Path(where)]
        self._branches = branches
        self.selec = selec
        self._isdata = isdata
        self._data = None
        self.pythfiles = files
    
    @property
    def name(self: "Sample")-> str :
        return self._name
    
    @property
    def sel(self: "Sample")-> str :
        return self.selec

    @property
    def branches(self: "Sample")->Dict[str, List["Branch"]] :
        return self._branches
    
    @property 
    def location(self: "Sample")->Path:
        return self._location

    @property
    def tag(self:"Sample")->str:
        return self._tag

    @property
    def data(self:"Sample"):
        return self._data

    @data.setter
    def data(self:"Sample", val: dict):
        self._data = val
    
    @property
    def isdata(self:"Sample"):
        return self._isdata

    @isdata.setter
    def isdata(self:"Sample", val: bool):
        self._isdata = isdata