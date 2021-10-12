pkgname = "file"
pkgver = "5.40"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-static", "--disable-libseccomp",
    "--disable-bzlib", "--disable-xzlib"
]
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "File type identification utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://www.darwinsys.com/file"
source = f"https://astron.com/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "167321f43c148a553f68a0ea7f579821ef3b11c27b8cbe158e4df897e4a5dd57"
options = ["bootstrap"]

if current.cross_build:
    hostmakedepends += ["file"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libmagic")
def _libmagic(self):
    self.pkgdesc = "File type identification library"

    return self.default_libs(extra = [
        "usr/share/misc",
        "usr/share/man/man4",
    ])

@subpackage("file-devel")
def _devel(self):
    self.depends += makedepends
    self.pkgdesc = "File type identification library (development files)"

    return self.default_devel(man = True)
