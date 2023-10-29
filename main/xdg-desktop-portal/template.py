pkgname = "xdg-desktop-portal"
pkgver = "1.18.1"
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
sha256 = "4560478e78b1e246c53e4b0540e63748187143942d6f202a4dcd4864318bfd10"


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)
    self.install_file(
        self.files_path / "portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("xdg-desktop-portal-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
