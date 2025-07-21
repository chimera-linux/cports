pkgname = "xdg-desktop-portal-gnome"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemduserunitdir=/tmp/delete_me"]
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
sha256 = "cd15aca2e1364da308eb3796bb8ae4a577e60ca4fe12006b315232cfd19c8861"


def post_install(self):
    # systemd service destination dir
    self.uninstall("tmp/delete_me")
