pkgname = "xdg-desktop-portal-hyprland"
pkgver = "1.3.9"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
	"cmake",
    "meson",
	"pkgconf",
]
makedepends = [
	"libgbm-devel",
	"hyprland-protocols",
	"hyprlang",
	"hyprutils-devel",
	"hyprwayland-scanner",
	"libdrm",
	"pipewire-devel",
	"sdbus-cpp-devel",
	"qt6-qtbase-devel",
	"wayland-devel",
	"wayland-protocols",
	
]
depends = ["xdg-desktop-portal", "gsettings-desktop-schemas"]
pkgdesc = "Xdg-desktop-portal backend for Hyprland"
maintainer = "kkflt <kkflt@cyberdude.com>"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/xdg-desktop-portal-hyprland"
source = f"{url}/archive/v{pkgver}/xdg-desktop-portal-hyprland-{pkgver}.tar.gz"
sha256 = "3f7d94fd408ed5e3a9b639d3dd8502e2169decc34f285e8552434da5fddf497e"


def post_install(self):
    self.install_license("LICENSE")
    self.uninstall("usr/lib/systemd")
