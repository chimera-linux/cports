pkgname = "xdg-desktop-portal-wlr"
pkgver = "0.8.4"
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
sha256 = "41b9683acae9415005d7b62d801e34946cb95da5eaaa83528c7085759a635187"
hardening = ["vis", "!cfi"]
options = ["etcfiles"]


def post_install(self):
    self.install_license("LICENSE")
    # (at least an) empty config is a requirement for the portal screen picker apparently
    self.install_file(
        self.files_path / "config", "etc/xdg/xdg-desktop-portal-wlr"
    )
