pkgname = "xdg-desktop-portal"
pkgver = "1.18.2"
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
sha256 = "dfac239c5476aafd117a9a10131a2f0b142f72106c52fc03859938e00545f440"


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)
    self.install_file(
        self.files_path / "portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("xdg-desktop-portal-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
