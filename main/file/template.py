pkgname = "file"
pkgver = "5.44"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-static",
    "--disable-libseccomp",
    "--disable-bzlib",
    "--disable-xzlib",
]
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "File type identification utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://www.darwinsys.com/file"
source = f"https://astron.com/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "3751c7fba8dbc831cb8d7cc8aff21035459b8ce5155ef8b0880a27d028475f3b"

if self.profile().cross:
    hostmakedepends += ["file"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libmagic")
def _libmagic(self):
    self.pkgdesc = "File type identification library"

    return self.default_libs(
        extra=[
            "usr/share/misc",
            "usr/share/man/man4",
        ]
    )


@subpackage("file-devel")
def _devel(self):
    self.depends += makedepends
    self.pkgdesc = "File type identification library (development files)"

    return self.default_devel()


configure_gen = []
