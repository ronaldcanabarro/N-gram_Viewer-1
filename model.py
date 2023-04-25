# from typing import List
# from typing import Any
# from dataclasses import dataclass
#
#
# @dataclass
# class Dataset:
#     label: str
#     data: List[int]
#
#     @staticmethod
#     def from_dict(obj: Any) -> 'Dataset':
#         _label = str(obj.get("label"))
#         _data = [.from_dict(y) for y in obj.get("data")]
#         return Dataset(_label, _data)
#
# @dataclass
# class Root:
#     labels: List[str]
#     dataset: List[Dataset]
#
#     @staticmethod
#     def from_dict(obj: Any) -> 'Root':
#         _labels = [.from_dict(y) for y in obj.get("labels")]
#         _dataset = [Dataset.from_dict(y) for y in obj.get("dataset")]
#         return Root(_labels, _dataset)


# {
# "labels":["2017","2018"],
#   "dataset":[{
#   "label":"ana",
#   "data":[1,2]
#   },
# {
#   "label":"Luciano",
#   "data":[1,2]
#   }
# ]
# }