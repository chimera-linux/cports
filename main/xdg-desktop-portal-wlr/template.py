pkgname = "xdg-desktop-portal-wlr"
pkgver = "0.8.0"
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
sha256 = "89a29d7d8f964023c03a20bdee8f263eb50419425bbdeeb822b69e5e9626ffc1"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
    # (at least an) empty config is a requirement for the portal screen picker apparently
    self.install_file(
        self.files_path / "config", "etc/xdg/xdg-desktop-portal-wlr"
    )
