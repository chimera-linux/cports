pkgname = "xdg-desktop-portal-gnome"
pkgver = "46.2"
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
source = f"https://download.gnome.org/sources/xdg-desktop-portal-gnome/{pkgver.split('.')[0]}/xdg-desktop-portal-gnome-{pkgver}.tar.xz"
sha256 = "b5c65ea25e8483502d033a613be6dc6b71883ac07f1a3e474ad18049c47d16d6"


def post_install(self):
    # systemd service destination dir
    self.uninstall("tmp/delete_me")
