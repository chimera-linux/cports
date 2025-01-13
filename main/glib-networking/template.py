pkgname = "glib-networking"
pkgver = "2.80.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgnutls=enabled",
    "-Dopenssl=enabled",
    "-Dlibproxy=enabled",
    "-Dgnome_proxy=enabled",
    "-Ddefault_library=shared",
]
hostmakedepends = ["meson", "pkgconf", "glib-devel", "gettext"]
makedepends = [
    "openssl-devel",
    "gnutls-devel",
    "gsettings-desktop-schemas-devel",
    "glib-devel",
    "libproxy-devel",
]
depends = ["gsettings-desktop-schemas"]
checkdepends = ["glib"]
pkgdesc = "Network extensions for glib"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/glib-networking"
source = f"$(GNOME_SITE)/glib-networking/{pkgver[:-2]}/glib-networking-{pkgver}.tar.xz"
sha256 = "b80e2874157cd55071f1b6710fa0b911d5ac5de106a9ee2a4c9c7bee61782f8e"


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("glib-networking-openssl")
def _(self):
    self.subdesc = "OpenSSL backend"
    # autoinstall if openssl is installed
    self.install_if = [self.parent, "openssl"]

    return ["usr/lib/gio/modules/libgioopenssl.so"]


@subpackage("glib-networking-gnutls")
def _(self):
    self.subdesc = "GnuTLS backend"
    # autoinstall if gnutls is installed
    self.install_if = [self.parent, "gnutls"]

    return ["usr/lib/gio/modules/libgiognutls.so"]
