pkgname = "libbsd"
pkgver = "0.12.2"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gsed",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libmd-devel",
    "linux-headers",
    "musl-bsd-headers",
]
pkgdesc = "Commonly used BSD functions not implemented by all libcs"
license = "BSD-3-Clause"
url = "https://libbsd.freedesktop.org"
source = f"{url}/releases/libbsd-{pkgver}.tar.xz"
sha256 = "b88cc9163d0c652aaf39a99991d974ddba1c3a9711db8f1b5838af2a14731014"
# lto deletes symbols needed for <nlist.h> tests
options = ["linkundefver", "!lto"]
# format.ld needs gnu syntax
exec_wrappers = [("/usr/bin/gsed", "sed")]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libbsd-devel")
def _(self):
    self.depends = [self.parent, "libmd-devel"]
    return self.default_devel()
