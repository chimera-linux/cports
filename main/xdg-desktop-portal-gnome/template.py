pkgname = "xdg-desktop-portal-gnome"
pkgver = "44.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemduserunitdir=/tmp/delete_me"]
hostmakedepends = ["meson", "pkgconf", "gettext-tiny", "glib-devel"]
makedepends = [
    "xdg-desktop-portal-devel", "libadwaita-devel",
    "gsettings-desktop-schemas-devel", "gnome-desktop-devel"
]
depends = ["xdg-desktop-portal-gtk", "dbus"]
pkgdesc = "Backend implementation for xdg-desktop-portal for GNOME"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome"
source = f"https://download.gnome.org/sources/xdg-desktop-portal-gnome/{pkgver.split('.')[0]}/xdg-desktop-portal-gnome-{pkgver}.tar.xz"
sha256 = "3682c546c81922a5ba69d62d86f69c0c26b17c9096823f58149d0b55bbf0eedb"

def post_install(self):
    # systemd service destination dir
    self.rm(self.destdir / "tmp/delete_me", recursive = True)
