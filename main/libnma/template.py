pkgname = "libnma"
pkgver = "1.10.6"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dgtk_doc=false",
    "-Dlibnma_gtk4=true",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gcr-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "iso-codes",
    "mobile-broadband-provider-info",
    "networkmanager-devel",
]
depends = ["networkmanager", "iso-codes"]
pkgdesc = "NetworkManager GNOME applet runtime library"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libnma"
source = f"{url}/-/archive/{pkgver}/libnma-{pkgver}.tar.gz"
sha256 = "c88fd3408c4ff166b06179b5ce5186e08a57b64eb8c9b22e055ca0dbc5e8002b"
options = ["!cross"]


def post_install(self):
    # Conflicts with main/network-manager-applet
    # See https://gitlab.gnome.org/GNOME/network-manager-applet/-/commit/574fdd97ae38b89f6d3d1a1c3fbfd63754b25df2
    self.uninstall("usr/share/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml")


@subpackage("libnma-devel")
def _(self):
    return self.default_devel()
