pkgname = "xdg-desktop-portal-gtk"
pkgver = "1.15.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    # pulls gnome-desktop
    "-Dwallpaper=disabled",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "fontconfig-devel",
    "gsettings-desktop-schemas-devel",
    "gtk+3-devel",
    "xdg-desktop-portal-devel",
]
depends = ["xdg-desktop-portal", "gsettings-desktop-schemas"]
pkgdesc = "Gtk implementation of xdg-desktop-portal"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/flatpak/xdg-desktop-portal-gtk"
source = f"https://github.com/flatpak/xdg-desktop-portal-gtk/releases/download/{pkgver}/xdg-desktop-portal-gtk-{pkgver}.tar.xz"
sha256 = "0295af247fc0d8c94e722731c29a2db7a045d38b132325b22e508709a235300b"


def post_install(self):
    self.uninstall("usr/lib/systemd")
