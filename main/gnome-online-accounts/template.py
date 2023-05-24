pkgname = "gnome-online-accounts"
pkgver = "3.48.0"
pkgrel = 0
build_style = "meson"
# TODO: figure out if we can make it work with heimdal
configure_args = [
    "-Dintrospection=true",
    "-Dvapi=true",
    "-Dmedia_server=true",
    "-Dman=true",
    "-Dkerberos=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext-tiny-devel",
    "docbook-xsl-nons",
    "glib-devel",
    "xsltproc",
    "gobject-introspection",
    "vala",
]
makedepends = [
    "glib-devel",
    "dbus-devel",
    "gtk+3-devel",
    "webkitgtk-devel",
    "json-glib-devel",
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
sha256 = "418bb9fcffdbd72a98205ad365137617fc1e3551a54de74f6a98d45d266175bf"
options = ["!cross"]


@subpackage("gnome-online-accounts-devel")
def _devel(self):
    return self.default_devel()
