pkgname = "networkmanager-openconnect"
pkgver = "1.2.10"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-gtk4=yes", "--disable-static"]
make_dir = "."
hostmakedepends = [
    "automake",
    "file",
    "gcr-progs",
    "gettext-devel",
    "glib-devel",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gcr3-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "libnma-devel",
    "libsecret-devel",
    "libxml2-devel",
    "networkmanager-devel",
    "openconnect-devel",
    "webkitgtk-devel",
]
pkgdesc = "OpenConnect support for NetworkManager"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/NetworkManager-openconnect"
source = f"{url}/-/archive/{pkgver}/NetworkManager-openconnect-{pkgver}.tar.bz2"
sha256 = "df21a8730438b1614de390ecf1f73d379536d388a8e464c9a802dab14dd23c8f"


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
