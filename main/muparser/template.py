pkgname = "muparser"
pkgver = "2.3.4"
pkgrel = 0
build_style = "cmake"
configure_args = []
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = []
pkgdesc = "Qt implementation of freedesktop.org xdg specs"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "BSD-2-Clause"
url = "https://beltoforion.de/en/muparser"
source = f"https://github.com/beltoforion/muparser/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0c3fa54a3ebf36dda0ed3e7cd5451c964afbb15102bdbcba08aafb359a290121"

if self.profile().arch in ["aarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]:
    makedepends += ["libomp-devel"]
else:
    configure_args += ["-DENABLE_OPENMP=OFF"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("muparser-devel")
def _(self):
    return self.default_devel()
