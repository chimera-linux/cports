pkgname = "gnome-online-accounts"
pkgver = "3.50.5"
pkgrel = 0
build_style = "meson"
configure_args = [
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
    "glib-devel",
    "dbus-devel",
    "gcr-devel",
    "gtk4-devel",
    "heimdal-devel",
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
source = f"$(GNOME_SITE)/gnome-online-accounts/{pkgver[:-2]}/gnome-online-accounts-{pkgver}.tar.xz"
sha256 = "2d24942700ebb6d40a4757bb1d202f3c238f80f30df6f32c63f57a9edcb73f1a"
options = ["!cross"]


@subpackage("gnome-online-accounts-devel")
def _(self):
    return self.default_devel()
