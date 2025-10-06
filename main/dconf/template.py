pkgname = "dconf"
pkgver = "0.49.0"
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
sha256 = "16a47e49a58156dbb96578e1708325299e4c19eea9be128d5bd12fd0963d6c36"
options = ["linkundefver"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("dconf-devel")
def _(self):
    return self.default_devel()
