pkgname = "gnome-online-accounts"
pkgver = "3.50.0"
pkgrel = 0
build_style = "meson"
# TODO: figure out if we can make it work with heimdal
configure_args = [
    "-Dintrospection=true",
    "-Dvapi=true",
    "-Dman=true",
    "-Dkerberos=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext-devel",
    "docbook-xsl-nons",
    "glib-devel",
    "xsltproc",
    "gobject-introspection",
    "vala",
]
makedepends = [
    "glib-devel",
    "dbus-devel",
    "gtk4-devel",
    "webkitgtk-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libsecret-devel",
    "libsoup-devel",
    "libxml2-devel",
    "rest-devel",
]
pkgdesc = "GNOME service to access online accounts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-online-accounts"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b0f64f0dcfbb8885a3a759e1c9de7fb204adb3ce6bd32c30bcf52d5533c06d4e"
options = ["!cross"]


@subpackage("gnome-online-accounts-devel")
def _devel(self):
    return self.default_devel()
