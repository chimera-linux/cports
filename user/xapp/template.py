pkgname = "xapp"
pkgver = "2.8.5"
pkgrel = 0
build_style = "meson"
# XXX: drop libexec
configure_args = ["--libexecdir=/usr/lib", "-Ddocs=true"]
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
sha256 = "c1fd855bdf90b1ce53a417da06186df72ab6d59f07d75620272a9c54facd07f3"
# No tests
options = ["!check", "!cross"]


@subpackage("xapp-devel")
def _(self):
    return self.default_devel()
