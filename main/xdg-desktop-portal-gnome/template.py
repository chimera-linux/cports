pkgname = "xdg-desktop-portal-gnome"
pkgver = "50.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/libexec",  # TODO switch libexec
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
sha256 = "ceeef2fb68b34b3f66a3def0a332a22a70af272641fb6c50065b7a2fde3d5759"


def post_install(self):
    # systemd service destination dir
    self.uninstall("tmp/delete_me")
