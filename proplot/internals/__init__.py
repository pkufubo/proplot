#!/usr/bin/env python3
"""
Internal classes and utilities.
"""
import inspect

try:  # print debugging (used with internal modules)
    from icecream import ic
except ImportError:  # graceful fallback if IceCream isn't installed
    ic = lambda *args: print(*args)  # noqa: E731


def _kwargs_to_args(options, *args, allow_extra=False, **kwargs):
    """
    Translate keyword arguments to positional arguments.
    """
    # NOTE: This fills missing positional arguments with None so that plotting
    # functions can subsequently infer defaults from the input metadata.
    nargs, nopts = len(args), len(options)
    if nargs > nopts and not allow_extra:
        raise ValueError(f'Expected up to {nopts} positional arguments. Got {nargs}.')
    args = list(args)  # WARNING: Axes.text() expects return type of list
    args.extend(None for _ in range(nopts - nargs))  # fill missing args
    for idx, keys in enumerate(options):
        if isinstance(keys, str):
            keys = (keys,)
        opts = {}
        if args[idx] is not None:  # positional args have first priority
            opts[keys[0] + '_positional'] = args[idx]
        for key in keys:  # keyword args
            opts[key] = kwargs.pop(key, None)
        args[idx] = _not_none(**opts)  # may reassign None
    return args, kwargs


def _not_none(*args, default=None, **kwargs):
    """
    Return the first non-``None`` value in the positional or keyword argument list.
    """
    # NOTE: This is used with keyword arg aliases and for setting default values.
    # Passing keyword args instead of positional args will emit warnings.
    first = default
    if args and kwargs:
        raise ValueError('_not_none can only be used with args or kwargs.')
    elif args:
        for arg in args:
            if arg is not None:
                first = arg
                break
    elif kwargs:
        for name, arg in list(kwargs.items()):
            if arg is not None:
                first = arg
                break
        kwargs = {name: arg for name, arg in kwargs.items() if arg is not None}
        if len(kwargs) > 1:
            warnings._warn_proplot(
                f'Got conflicting or duplicate keyword arguments: {kwargs}. '
                'Using the first keyword argument.'
            )
    return first


def _pop_parameters(kwargs, *funcs, ignore_internal=False):
    """
    Pop parameters of the input functions or methods.
    """
    # NOTE: This is mainly used to distribute user kwargs to different functions but
    # also used in PlotAxes to detect ignored parameters. In the latter case need to
    # omit parameters internal to PlotAxes parsing utilities so that they are excluded
    # from any subsequent warning messages.
    internal_parameters = (
        'inbounds',
        'default_cmap',
        'default_discrete',
        'plot_contours',
        'plot_lines',
        'skip_autolev',
        'to_centers',
    )
    output = {}
    for func in funcs:
        if isinstance(func, inspect.Signature):
            sig = func
        elif callable(func):
            sig = inspect.signature(func)
        elif func is None:
            continue
        else:
            raise RuntimeError(f'Internal error. Invalid function {func!r}.')
        for key in sig.parameters:
            value = kwargs.pop(key, None)
            if ignore_internal and key in internal_parameters:
                continue
            if value is not None:
                output[key] = value
    return output


def _pop_items(kwargs, *keys, **aliases):
    """
    Pop the input properties and return them in a new dictionary.
    """
    output = {}
    aliases.update({key: () for key in keys})
    for key, aliases in aliases.items():
        aliases = (aliases,) if isinstance(aliases, str) else aliases
        opts = {key: kwargs.pop(key, None) for key in (key, *aliases)}
        value = _not_none(**opts)
        if value is not None:
            output[key] = value
    return output


# Top-level imports
# WARNING: Must come after _not_none because this is leveraged inside other funcs
from . import (  # noqa: F401
    benchmarks,
    context,
    defaults,
    docstring,
    fonts,
    guides,
    inputs,
    labels,
    properties,
    settings,
    styles,
    validate,
    versions,
    warnings
)
from .properties import _pop_properties  # noqa: F401
from .settings import _pop_settings  # noqa: F401
from .versions import _version_mpl, _version_cartopy  # noqa: F401
from .warnings import ProplotWarning  # noqa: F401
