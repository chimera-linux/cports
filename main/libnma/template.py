pkgname = "libnma"
pkgver = "1.10.6"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dgtk_doc=false",
    "-Dlibnma_gtk4=true",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "vala",
    "glib-devel",
    "gettext",
]
makedepends = [
    "networkmanager-devel",
    "gcr-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "mobile-broadband-provider-info",
    "iso-codes",
]
depends = ["networkmanager", "iso-codes"]
pkgdesc = "NetworkManager GNOME applet runtime library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libnma"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c88fd3408c4ff166b06179b5ce5186e08a57b64eb8c9b22e055ca0dbc5e8002b"
options = ["!cross"]


def post_install(self):
    # Conflicts with contrib/network-manager-applet
    # See https://gitlab.gnome.org/GNOME/network-manager-applet/-/commit/574fdd97ae38b89f6d3d1a1c3fbfd63754b25df2
    self.uninstall("usr/share/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml")


@subpackage("libnma-devel")
def _devel(self):
    return self.default_devel()
