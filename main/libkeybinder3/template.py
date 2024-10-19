pkgname = "libkeybinder3"
pkgver = "0.3.2"
pkgrel = 2
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = ["gtk+3-devel"]
pkgdesc = "Gtk+3 library for registering global keyboard shortcuts"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "MIT"
url = "https://github.com/engla/keybinder"
source = f"{url}/archive/keybinder-3.0-v{pkgver}.tar.gz"
sha256 = "2eec50be6dfafa672d719e719f639df10403f270b2473e60deb2fb8455d13c51"
# crossbuild fails: does not find gobject-introspection nor gtk-doc
options = ["!cross"]


def post_extract(self):
    self.cp("ChangeLog.pre-git", "ChangeLog")


def post_install(self):
    self.install_license("COPYING")


@subpackage("libkeybinder3-devel")
def _(self):
    return self.default_devel()
