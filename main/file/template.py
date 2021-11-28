pkgname = "file"
pkgver = "5.41"
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
sha256 = "13e532c7b364f7d57e23dfeea3147103150cb90593a57af86c10e4f6e411603f"
options = ["lto"]

if self.cross_build:
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

@subpackage("file-static")
def _static(self):
    self.pkgdesc = "File type identification library (static library)"

    return self.default_static()

@subpackage("file-devel")
def _devel(self):
    self.depends += makedepends
    self.pkgdesc = "File type identification library (development files)"

    return self.default_devel(man = True)
