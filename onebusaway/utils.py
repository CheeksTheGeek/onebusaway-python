# utils.py
from dataclasses import field, make_dataclass
from typing import Any, Dict, List, Union, Type
from enum import Enum


def infer_type(
    value: Any,
) -> Union[
    Type[int], Type[float], Type[str], Type[bool], Type[Dict[str, Any]], Type[List[Any]]
]:
    if isinstance(value, dict):
        return Dict[str, Any]
    elif isinstance(value, list):
        return List[Any]
    return type(value)


def type_annotated_dataclass_from_dict(data: Dict[str, Any], class_name: str) -> Any:
    fields = []
    for key, value in data.items():
        if isinstance(value, dict):
            nested_class_name = f"{class_name}_{key.capitalize()}"
            nested_class = type_annotated_dataclass_from_dict(value, nested_class_name)
            # Use a default argument in the lambda to capture the current value
            fields.append(
                (
                    key,
                    nested_class,
                    field(default_factory=lambda value=value: nested_class(**value)),
                )
            )
        else:
            fields.append((key, infer_type(value), field(default=value)))
    return make_dataclass(class_name, fields)


def sanitize_keys(data: Dict[str, Any]) -> Dict[str, Any]:
    sanitized_data = {}
    for key, value in data.items():
        sanitized_key = (
            key.replace(".", "_").replace("-", "_").replace(" ", "_").replace("/", "_")
        )
        if isinstance(value, dict):
            sanitized_data[sanitized_key] = sanitize_keys(value)
        elif isinstance(value, list):
            sanitized_data[sanitized_key] = [
                sanitize_keys(v) if isinstance(v, dict) else v for v in value
            ]
        else:
            sanitized_data[sanitized_key] = value
    return sanitized_data


def dynamic_dataclass_from_dict(data: Dict[str, Any], class_name: str) -> Any:
    data = sanitize_keys(data)
    cls = type_annotated_dataclass_from_dict(data, class_name)
    return cls()


# class Deployment(Enum):
#     TAMPA = "api.tampa.onebusaway.org"  # Tampa, FL
#     PS = "api.pugetsound.onebusaway.org"  # Puget Sound, WA
#     MTA = "bustime.mta.info"  # MTA, NY
#     DC = "buseta.wmata.com"  # Washington, DC
#     ROGUE = "oba.rvtd.org"  # Rogue Valley, OR
#     SAN_JOAQUIN = "www.obartd.com"  # San Joaquin, CA
#     SAN_DIEGO = "realtime.sdmts.com"  # San Diego, CA
#     SPOKANE = "www.oba4spokane.com"  # Spokane, WA
#     MAYAGUEZ = "pr-oba.live"  # Mayaguez, PR
#     VICTORIA = "oba.gcrpc.org"  # Victoria, BC
#     ADELAIDE = "transit.nautilus-tech.com.au"  # Adelaide, SA
#     CUSTOM = "custom"  # Custom deployment


def generic_repr(self):
    attributes = ", ".join(
        f"{key}={value!r}"
        for key, value in self.__dict__.items()
        if key not in ["linked_references", "references"]
    )
    return f"{self.__class__.__name__}({attributes})"


def generic_repr_pretty(self, p, cycle):
    if cycle:
        p.text(f"{self.__class__.__name__}(...)")
    else:
        with p.group(1, f"{self.__class__.__name__}(", ")"):
            for idx, (key, value) in enumerate(self.__dict__.items()):
                if key not in ["linked_references", "references"]:
                    if idx:
                        p.text(",")
                        p.breakable()
                    p.text(f"{key}=")
                    p.pretty(value)
