pkgname = "dconf"
pkgver = "0.40.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "docbook-xsl-nons",
    "glib-devel",
    "meson",
    "pkgconf",
    "vala",
    "xsltproc",
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/dconf"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "cf7f22a4c9200421d8d3325c5c1b8b93a36843650c9f95d6451e20f0bcb24533"
options = ["linkundefver"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)


@subpackage("dconf-devel")
def _devel(self):
    return self.default_devel()
