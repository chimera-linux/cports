pkgname = "xdg-desktop-portal"
pkgver = "1.18.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "bubblewrap", "glib-devel"]
makedepends = [
    "flatpak-devel",
    "json-glib-devel",
    "fuse-devel",
    "gdk-pixbuf-devel",
    "pipewire-devel",
    "libportal-devel",
    "geoclue-devel",
]
checkdepends = ["bash", "dbus"]
pkgdesc = "Desktop integration portal"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/flatpak/xdg-desktop-portal"
source = f"https://github.com/flatpak/xdg-desktop-portal/releases/download/{pkgver}/xdg-desktop-portal-{pkgver}.tar.xz"
sha256 = "5ea35a6420a98b598c83355fc19feaea8ba999149641bf84079b0c572b00f5bd"


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)


@subpackage("xdg-desktop-portal-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
