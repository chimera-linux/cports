pkgname = "file"
pkgver = "5.47"
pkgrel = 0
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
license = "BSD-2-Clause"
url = "http://www.darwinsys.com/file"
source = f"https://astron.com/pub/file/file-{pkgver}.tar.gz"
sha256 = "45672fec165cb4cc1358a2d76b5d57d22876dcb97ab169427ac385cbe1d5597a"

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
