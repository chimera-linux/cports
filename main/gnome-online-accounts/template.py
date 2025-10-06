pkgname = "gnome-online-accounts"
pkgver = "3.56.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Ddocumentation=false",
    "-Dintrospection=true",
    "-Dvapi=true",
    "-Dman=true",
    "-Dkerberos=true",
]
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "libxslt-progs",
    "meson",
    "pkgconf",
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
    "librest-devel",
    "libsecret-devel",
    "libsoup-devel",
    "libxml2-devel",
    "webkitgtk-devel",
]
pkgdesc = "GNOME service to access online accounts"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-online-accounts"
source = f"$(GNOME_SITE)/gnome-online-accounts/{pkgver[:-2]}/gnome-online-accounts-{pkgver}.tar.xz"
sha256 = "31d6a017d171b27ff936478fdb0792a200c8142eafc18b255073ce9dfb417572"
options = ["!cross"]


@subpackage("gnome-online-accounts-devel")
def _(self):
    return self.default_devel()
