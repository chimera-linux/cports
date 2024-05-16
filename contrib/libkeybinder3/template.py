pkgname = "libkeybinder3"
pkgver = "0.3.2"
pkgrel = 1
build_style = "gnu_configure"
configure_env = {"NOCONFIGURE": "1"}
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = [
    "gettext",
    "gmake",
    "gnome-common",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = ["gtk+3-devel"]
pkgdesc = "Library for registering global keyboard shortcuts (GTK+3)"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "MIT"
url = "https://github.com/engla/keybinder"
source = f"{url}/archive/keybinder-3.0-v{pkgver}.tar.gz"
sha256 = "2eec50be6dfafa672d719e719f639df10403f270b2473e60deb2fb8455d13c51"
# crossbuild fails: does not find gobject-introspection nor gtk-doc
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libkeybinder3-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/girepository-1.0",
        ]
    )
