pkgname = "gnome-online-accounts"
pkgver = "3.50.1"
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
sha256 = "42ee43fd1e2942b9ff6106252ccdc834602815508bf7a3a52c0bdfffa56eaf40"
options = ["!cross"]


@subpackage("gnome-online-accounts-devel")
def _devel(self):
    return self.default_devel()
