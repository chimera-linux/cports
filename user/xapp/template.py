pkgname = "xapp"
pkgver = "2.8.6"
pkgrel = 0
build_style = "meson"
# XXX: drop libexec
configure_args = [
    "--libexecdir=/usr/lib",
    "-Ddocs=true",
    "-Ddebian_derivative=true",
]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "gtk-doc-tools",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "dbus-devel",
    "glib-devel",
    "gtk+3-devel",
    "libdbusmenu-devel",
    "libgnomekbd-devel",
    "libxkbfile-devel",
    "python-gobject-devel",
]
depends = ["gtk+3", "python-gobject", "python-setproctitle"]
pkgdesc = "Cross-desktop libraries and common resources"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/xapp/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7cb987399789502bc4094add704c22873c610323426379e61cf18fd5921e9be5"
# No tests
options = ["!check", "!cross"]


def post_install(self):
    # worthless
    self.uninstall("usr/bin/xapp-gpu-offload")


@subpackage("xapp-devel")
def _(self):
    return self.default_devel()


@subpackage("xapp-progs")
def _(self):
    self.depends += [self.parent, "python"]
    return self.default_progs()
