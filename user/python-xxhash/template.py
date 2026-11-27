pkgname = "python-xxhash"
pkgver = "4.1.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"XXHASH_LINK_SO": "1"}
# requires the pyright binary, which is not packaged
make_check_args = ["--ignore=tests/test_stubs_pyright.py"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel", "xxhash-devel"]
depends = ["python"]
checkdepends = ["python-pytest", "python-pytest-benchmark"]
pkgdesc = "Python bindings for xxHash"
license = "BSD-2-Clause"
url = "https://github.com/ifduyue/python-xxhash"
source = f"$(PYPI_SITE)/x/xxhash/xxhash-{pkgver}.tar.gz"
sha256 = "c9b288e4c1f5dae54417bc8a05e6f6daf505783d916b4783f4dd2f2e7d5db486"


def pre_check(self):
    # would shadow the installed module, which has the compiled extension
    self.rm("xxhash", recursive=True)


def post_install(self):
    self.install_license("LICENSE")
