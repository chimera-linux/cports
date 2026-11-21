pkgname = "python-xxhash"
pkgver = "4.0.2"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"XXHASH_LINK_SO": "1"}
make_check_args = ["--ignore=tests/test_stubs_pyright.py"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel", "xxhash-devel"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python bindings for xxHash"
license = "BSD-2-Clause"
url = "https://github.com/ifduyue/python-xxhash"
source = f"https://files.pythonhosted.org/packages/source/x/xxhash/xxhash-{pkgver}.tar.gz"
sha256 = "af3d1b3cfa5280e84d8968e9f30c9eca75781db4915eb6d6acb0dd4fc93e0f47"


def pre_check(self):
    # would shadow the installed module, which has the compiled extension
    self.rm("xxhash", recursive=True)


def post_install(self):
    self.install_license("LICENSE")
