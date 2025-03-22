pkgname = "xdg-desktop-portal-gtk"
pkgver = "1.15.3"
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
license = "LGPL-2.1-or-later"
url = "https://github.com/flatpak/xdg-desktop-portal-gtk"
source = f"https://github.com/flatpak/xdg-desktop-portal-gtk/releases/download/{pkgver}/xdg-desktop-portal-gtk-{pkgver}.tar.xz"
sha256 = "47a3743d2419a8601e691db37e85bb5fac5ae4b26842177065cd5f22ada23b37"


def post_install(self):
    self.uninstall("usr/lib/systemd")
