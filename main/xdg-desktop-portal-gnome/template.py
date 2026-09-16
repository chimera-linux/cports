pkgname = "xdg-desktop-portal-gnome"
pkgver = "51.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemduserunitdir=/tmp/delete_me",
]
hostmakedepends = ["meson", "pkgconf", "gettext", "glib-devel"]
makedepends = [
    "gnome-desktop-devel",
    "gsettings-desktop-schemas-devel",
    "libadwaita-devel",
    "xdg-desktop-portal-devel",
]
depends = ["xdg-desktop-portal-gtk"]
pkgdesc = "Backend implementation for xdg-desktop-portal for GNOME"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome"
source = f"https://download.gnome.org/sources/xdg-desktop-portal-gnome/{pkgver.split('.')[0]}/xdg-desktop-portal-gnome-{pkgver}.tar.xz"
sha256 = "ec228b305091b649c16c690e102aa1d66fc10e9834888d51e411913c82c1430d"


def post_install(self):
    # systemd service destination dir
    self.uninstall("tmp/delete_me")
