"""
============================
Typing (:mod:`numpy.typing`)
============================

Large parts of the NumPy API have PEP-484-style type annotations. In
addition, the following type aliases are available for users.

- ``typing.ArrayLike``: objects that can be converted to arrays
- ``typing.DtypeLike``: objects that can be converted to dtypes

Roughly speaking, ``typing.ArrayLike`` is "objects that can be used as
inputs to ``np.array``" and ``typing.DtypeLike`` is "objects that can
be used as inputs to ``np.dtype``".

Differences from the runtime NumPy API
--------------------------------------

NumPy is very flexible. Trying to describe the full range of
possibilities statically would result in types that are not very
helpful. For that reason, the typed NumPy API is often stricter than
the runtime NumPy API. This section describes some notable
differences.

ArrayLike
~~~~~~~~~

The ``ArrayLike`` type tries to avoid creating object arrays. For
example,

.. code-block:: python

  np.array(x**2 for x in range(10))

is valid NumPy code which will create an object array. The types will
complain about this usage however.

ndarray
~~~~~~~

It's possible to mutate the dtype of an array at runtime. For example,
the following code is valid:

.. code-block:: python

  x = np.array([1, 2])
  x.dtype = np.bool_

This sort of mutation is not allowed by the types. Users who want to
write statically typed code should insted use the `numpy.ndarray.view`
method to create a view of the array with a different dtype.

"""
from ._array_like import _SupportsArray, ArrayLike
from ._shape import _Shape, _ShapeLike
from ._dtype_like import DtypeLike
