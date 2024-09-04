pkgname = "xdg-desktop-portal-gnome"
pkgver = "47_rc"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemduserunitdir=/tmp/delete_me"]
hostmakedepends = ["meson", "pkgconf", "gettext", "glib-devel"]
makedepends = [
    "xdg-desktop-portal-devel",
    "libadwaita-devel",
    "gsettings-desktop-schemas-devel",
    "gnome-desktop-devel",
]
depends = ["xdg-desktop-portal-gtk"]
pkgdesc = "Backend implementation for xdg-desktop-portal for GNOME"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome"
source = f"https://download.gnome.org/sources/xdg-desktop-portal-gnome/{pkgver[:2]}/xdg-desktop-portal-gnome-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "3f28f1dd76b6520b5c52f0a61066c80255b4d59483a480dd98b72b2d001fd866"


def post_install(self):
    # systemd service destination dir
    self.uninstall("tmp/delete_me")
