pkgname = "gnome-online-accounts"
pkgver = "3.52.3.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocumentation=false",
    "-Dintrospection=true",
    "-Dvapi=true",
    "-Dman=true",
    "-Dkerberos=true",
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
    "dbus-devel",
    "gcr-devel",
    "glib-devel",
    "gtk4-devel",
    "heimdal-devel",
    "json-glib-devel",
    "keyutils-devel",
    "libadwaita-devel",
    "libsecret-devel",
    "libsoup-devel",
    "libxml2-devel",
    "rest-devel",
    "webkitgtk-devel",
]
pkgdesc = "GNOME service to access online accounts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-online-accounts"
source = f"$(GNOME_SITE)/gnome-online-accounts/{pkgver[:-4]}/gnome-online-accounts-{pkgver}.tar.xz"
sha256 = "49ed727d6fc49474996fa7edf0919b21e4fc856ea37e6e30f17b50b103af9701"
options = ["!cross"]


@subpackage("gnome-online-accounts-devel")
def _(self):
    return self.default_devel()
