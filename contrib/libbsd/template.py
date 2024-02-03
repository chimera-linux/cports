pkgname = "libbsd"
pkgver = "0.12.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gmake",
    "gsed",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libmd-devel",
    "linux-headers",
    "musl-bsd-headers",
    "musl-devel",
]
pkgdesc = "Commonly used BSD functions not implemented by all libcs"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://libbsd.freedesktop.org"
source = f"{url}/releases/libbsd-{pkgver}.tar.xz"
sha256 = "d7747f8ec1baa6ff5c096a9dd587c061233dec90da0f1aedd66d830f6db6996a"
# FIXME: ld.lld version 16 and up regressions, needs linkundefver to work around it
# https://lists.freedesktop.org/archives/libbsd/2024-January/000381.html
# lto: breaks <nlist.h> test
options = ["linkundefver", "!lto"]
# format.ld needs gnu syntax
exec_wrappers = [("/usr/bin/gsed", "sed")]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libbsd-devel")
def _devel(self):
    return self.default_devel()
