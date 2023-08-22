pkgname = "xdg-desktop-portal-gtk"
pkgver = "1.14.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "glib-devel", "gmake", "gettext"]
makedepends = [
    "gtk+3-devel",
    "xdg-desktop-portal-devel",
    "fontconfig-devel",
    "gsettings-desktop-schemas-devel",
]
depends = ["xdg-desktop-portal"]
pkgdesc = "Gtk implementation of xdg-desktop-portal"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/flatpak/xdg-desktop-portal-gtk"
source = f"https://github.com/flatpak/xdg-desktop-portal-gtk/releases/download/{pkgver}/xdg-desktop-portal-gtk-{pkgver}.tar.xz"
sha256 = "3ee2a992187eabb237a76170a7dead2a3bcea2edbf59344647cc0d1c640a5700"


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)


configure_gen = []
