pkgname = "glib-networking"
pkgver = "2.90.0"
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
    "glib-devel",
    "gnutls-devel",
    "gsettings-desktop-schemas-devel",
    "libproxy-devel",
    "openssl3-devel",
]
depends = ["gsettings-desktop-schemas"]
checkdepends = ["glib"]
pkgdesc = "Network extensions for glib"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/glib-networking"
source = f"$(GNOME_SITE)/glib-networking/{pkgver[:-2]}/glib-networking-{pkgver}.tar.xz"
sha256 = "83a75e3d9c36b66ee86d3281c2fc997816101968a5126ba322b2acb9a74dd8c0"


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("glib-networking-openssl")
def _(self):
    self.subdesc = "OpenSSL backend"
    # autoinstall if openssl is installed
    self.install_if = [self.parent, "openssl3"]

    return ["usr/lib/gio/modules/libgioopenssl.so"]


@subpackage("glib-networking-gnutls")
def _(self):
    self.subdesc = "GnuTLS backend"
    # autoinstall if gnutls is installed
    self.install_if = [self.parent, "gnutls"]

    return ["usr/lib/gio/modules/libgiognutls.so"]
