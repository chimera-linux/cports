pkgname = "file"
pkgver = "5.46"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-static",
    "--disable-libseccomp",
    "--disable-bzlib",
    "--disable-xzlib",
]
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "File type identification utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://www.darwinsys.com/file"
source = f"https://astron.com/pub/file/file-{pkgver}.tar.gz"
sha256 = "c9cc77c7c560c543135edc555af609d5619dbef011997e988ce40a3d75d86088"

if self.profile().cross:
    hostmakedepends += ["file"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("file-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libmagic")]

    return self.default_libs(
        extra=[
            "usr/share/misc",
            "usr/share/man/man4",
        ]
    )


@subpackage("file-devel")
def _(self):
    self.depends += makedepends

    return self.default_devel()
