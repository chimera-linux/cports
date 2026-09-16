pkgname = "dconf"
pkgver = "51.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "docbook-xsl-nons",
    "glib-devel",
    "libxslt-progs",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "bash-completion",
    "dbus-devel",
    "glib-devel",
    "gtk+3-devel",
    "libxml2-devel",
    "vala-devel",
]
checkdepends = ["dbus"]
pkgdesc = "Low-level configuration system for GNOME"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/dconf"
source = f"$(GNOME_SITE)/dconf/{pkgver[:-2]}/dconf-{pkgver}.tar.xz"
sha256 = "e65c1b7867f836faad9f9ee04acf5c5a6cae2bbc784833fe093207e0cb590248"
options = ["linkundefver"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("dconf-devel")
def _(self):
    return self.default_devel()
