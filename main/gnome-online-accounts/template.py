pkgname = "gnome-online-accounts"
pkgver = "3.54.1"
pkgrel = 1
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
    "libxslt-progs",
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
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-online-accounts"
source = f"$(GNOME_SITE)/gnome-online-accounts/{pkgver[:-2]}/gnome-online-accounts-{pkgver}.tar.xz"
sha256 = "9d058b3aac8b2d8b6b2ae7cb57c8a8abe539e73c88220c315b5b99f87ce6efd8"
options = ["!cross"]


@subpackage("gnome-online-accounts-devel")
def _(self):
    return self.default_devel()
