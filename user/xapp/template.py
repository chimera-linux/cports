pkgname = "xapp"
pkgver = "3.2.3"
pkgrel = 0
build_style = "meson"
configure_args = [
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
license = "GPL-3.0-or-later AND LGPL-3.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/xapp/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e1df3c3e803bf59d133e53a718013b0a4213057beab3ee1eeeb3bfd3b48a946e"
# No tests
options = ["etcfiles", "!check", "!cross"]


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
