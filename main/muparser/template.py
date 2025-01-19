pkgname = "muparser"
pkgver = "2.3.5"
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
sha256 = "20b43cc68c655665db83711906f01b20c51909368973116dfc8d7b3c4ddb5dd4"

if self.profile().arch in ["aarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]:
    makedepends += ["libomp-devel"]
else:
    configure_args += ["-DENABLE_OPENMP=OFF"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("muparser-devel")
def _(self):
    return self.default_devel()
