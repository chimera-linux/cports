pkgname = "xdg-desktop-portal-wlr"
pkgver = "0.7.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "ninja",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "elogind-devel",
    "inih-devel",
    "mesa-devel",
    "pipewire-devel",
    "wayland-devel",
    "wayland-protocols",
    "xdg-desktop-portal-devel",
]
depends = ["xdg-desktop-portal"]
pkgdesc = "XDG-desktop-portal implementation for wlroots"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/emersion/xdg-desktop-portal-wlr"
source = f"https://github.com/emersion/xdg-desktop-portal-wlr/releases/download/v{pkgver}/xdg-desktop-portal-wlr-{pkgver}.tar.gz"
sha256 = "eec6e4be808e1a445e677dba1e20e5acb2f091825f5ff4c6ac49d5843b2185f9"
# FIXME: cfi
hardening = ["vis"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    # (at least an) empty config is a requirement for the portal screen picker apparently
    self.install_file(
        self.files_path / "config", "etc/xdg/xdg-desktop-portal-wlr"
    )
