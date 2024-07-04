pkgname = "glib-networking"
pkgver = "2.80.0"
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
sha256 = "d8f4f1aab213179ae3351617b59dab5de6bcc9e785021eee178998ebd4bb3acf"


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("glib-networking-openssl")
def _openssl(self):
    self.pkgdesc = f"{pkgdesc} (OpenSSL backend)"
    # autoinstall if openssl is installed
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "openssl"]

    return ["usr/lib/gio/modules/libgioopenssl.so"]


@subpackage("glib-networking-gnutls")
def _gnutls(self):
    self.pkgdesc = f"{pkgdesc} (GnuTLS backend)"
    # autoinstall if gnutls is installed
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "gnutls"]

    return ["usr/lib/gio/modules/libgiognutls.so"]
