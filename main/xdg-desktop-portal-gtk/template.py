pkgname = "xdg-desktop-portal-gtk"
pkgver = "1.15.1"
pkgrel = 1
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
sha256 = "425551ca5f36451d386d53599d95a3a05b94020f1a4927c5111a2c3ba3a0fe4c"


def post_install(self):
    self.uninstall("usr/lib/systemd")
