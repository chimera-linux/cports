pkgname = "alembic"
pkgver = "1.8.8"
pkgrel = 4
build_style = "cmake"
configure_args = ["-DUSE_HDF5=ON"]
# flaky in parallel
make_check_args = ["-j1"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "boost-devel",
    "hdf5-devel",
    "openexr-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Computer graphics interchange framework"
license = "BSD-3-Clause"
url = "https://www.alembic.io"
source = f"https://github.com/alembic/alembic/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ba1f34544608ef7d3f68cafea946ec9cc84792ddf9cda3e8d5590821df71f6c6"
hardening = ["vis", "!cfi"]

if self.profile().endian == "big":
    broken = "alembic is broken on big endian"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("alembic-devel")
def _(self):
    return self.default_devel()


@subpackage("alembic-progs")
def _(self):
    return self.default_progs()
