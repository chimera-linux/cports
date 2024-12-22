pkgname = "libaacs"
pkgver = "0.11.1"
pkgrel = 3
build_style = "gnu_configure"
configure_args = ["--disable-optimizations"]
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "libtool",
    "pkgconf",
]
makedepends = ["libgcrypt-devel"]
pkgdesc = "Research implementation of the AACS specification"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.videolan.org/developers/libaacs.html"
source = f"https://download.videolan.org/pub/videolan/libaacs/{pkgver}/libaacs-{pkgver}.tar.bz2"
sha256 = "a88aa0ebe4c98a77f7aeffd92ab3ef64ac548c6b822e8248a8b926725bea0a39"


@subpackage("libaacs-devel")
def _(self):
    return self.default_devel()


@subpackage("libaacs-progs")
def _(self):
    return self.default_progs()
