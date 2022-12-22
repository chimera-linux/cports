pkgname = "file"
pkgver = "5.43"
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
sha256 = "8c8015e91ae0e8d0321d94c78239892ef9dbc70c4ade0008c0e95894abfb1991"

if self.profile().cross:
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

    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
