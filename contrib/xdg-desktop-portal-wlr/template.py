pkgname = "xdg-desktop-portal-wlr"
pkgver = "0.7.0"
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
sha256 = "e397a72314165ef736d91655fe95867056efe371935f2d1e4a10d34fa0fffb4f"
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
