pkgname = "alembic"
pkgver = "1.8.7"
pkgrel = 0
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
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://www.alembic.io"
source = f"https://github.com/alembic/alembic/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3590f51f82e3675bb907f7a6a7149a76c06c23ef25d153e64391bcd22d86cc8c"
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
