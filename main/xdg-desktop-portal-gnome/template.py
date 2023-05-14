pkgname = "xdg-desktop-portal-gnome"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemduserunitdir=/tmp/delete_me"]
hostmakedepends = ["meson", "pkgconf", "gettext-tiny", "glib-devel"]
makedepends = ["xdg-desktop-portal-devel", "libadwaita-devel", "gsettings-desktop-schemas-devel", "gnome-desktop-devel"]
depends = ["xdg-desktop-portal"]
pkgdesc = "Backend implementation for xdg-desktop-portal for GNOME"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1"
url = "https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome"
source = f"https://download.gnome.org/sources/xdg-desktop-portal-gnome/{pkgver.split('.')[0]}/xdg-desktop-portal-gnome-{pkgver}.tar.xz"
sha256 = "55011e57f64b7caf0837405efa034a336b9e73deb9f84e5c14cc9f7a8e0e7b34"


def post_install(self):
    # systemd service destination dir
    self.rm(self.destdir / "tmp/delete_me", recursive=True)
