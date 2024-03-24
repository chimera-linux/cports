pkgname = "libbsd"
pkgver = "0.12.2"
pkgrel = 0
build_style = "gnu_configure"
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
sha256 = "b88cc9163d0c652aaf39a99991d974ddba1c3a9711db8f1b5838af2a14731014"
# FIXME: ld.lld version 16 and up regressions, needs linkundefver to work around it
# https://lists.freedesktop.org/archives/libbsd/2024-January/000381.html
# lto deletes symbols needed for <nlist.h> tests
options = ["linkundefver", "!lto"]
# format.ld needs gnu syntax
exec_wrappers = [("/usr/bin/gsed", "sed")]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libbsd-devel")
def _devel(self):
    return self.default_devel()
