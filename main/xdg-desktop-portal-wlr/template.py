pkgname = "xdg-desktop-portal-wlr"
pkgver = "0.9.0"
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
license = "MIT"
url = "https://github.com/emersion/xdg-desktop-portal-wlr"
source = f"https://github.com/emersion/xdg-desktop-portal-wlr/releases/download/v{pkgver}/xdg-desktop-portal-wlr-{pkgver}.tar.gz"
sha256 = "45e5c2d1a80f622892a00c980aca4bc50b6966137886892529f935caf0724172"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
