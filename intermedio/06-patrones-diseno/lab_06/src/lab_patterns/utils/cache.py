from collections.abc import Mapping
from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar, cast

P = ParamSpec("P")
R = TypeVar("R")


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return tuple(sorted((key, _freeze(val)) for key, val in value.items()))

    if isinstance(value, (list, tuple, set)):
        return tuple(_freeze(item) for item in value)

    try:
        hash(value)
        return value
    except TypeError:
        return (value.__class__.__name__, id(value))


def _build_key(args: tuple[Any, ...], kwargs: dict[str, Any]) -> tuple[Any, Any]:
    return (_freeze(args), _freeze(kwargs))


def cache_result(func: Callable[P, R]) -> Callable[P, R]:
    cache: dict[tuple[Any, Any], R] = {}

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        key = _build_key(args, kwargs)

        if key in cache:
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        return result

    setattr(wrapper, "_cache", cache)

    return cast(Callable[P, R], wrapper)
