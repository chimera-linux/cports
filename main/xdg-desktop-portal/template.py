pkgname = "xdg-desktop-portal"
pkgver = "1.18.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "bubblewrap", "glib-devel"]
makedepends = [
    "flatpak-devel",
    "fuse-devel",
    "gdk-pixbuf-devel",
    "geoclue-devel",
    "json-glib-devel",
    "libportal-devel",
    "pipewire-devel",
]
checkdepends = ["bash", "dbus"]
pkgdesc = "Desktop integration portal"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/flatpak/xdg-desktop-portal"
source = f"https://github.com/flatpak/xdg-desktop-portal/releases/download/{pkgver}/xdg-desktop-portal-{pkgver}.tar.xz"
sha256 = "b858aa1e74e80c862790dbb912906e6eab8b1e4db9339cd759473af62b461e65"


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_file(
        self.files_path / "portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("xdg-desktop-portal-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
