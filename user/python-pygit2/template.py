pkgname = "python-pygit2"
pkgver = "1.21.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # can't import
    "--deselect=test/test_odb_backend.py::test_index_add",
]
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = [
    "libgit2-devel",
    "python-devel",
]
depends = [
    "python-cffi",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Bindings to libgit2"
license = "GPL-2.0-only WITH GCC-exception-2.0"
url = "https://www.pygit2.org"
source = f"$(PYPI_SITE)/p/pygit2/pygit2-{pkgver}.tar.gz"
sha256 = "1e987fbef899d1bf12aecc10b33acc917d60266ca114428dfc260df4451a555f"
