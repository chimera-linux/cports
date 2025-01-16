pkgname = "hyprland-protocols"
pkgver = "0.5.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "ninja", "pkgconf"]
makedepends = []
pkgdesc = "Wayland protocol extensions for Hyprland"
maintainer = "kkflt <kkflt@cyberdude.com>"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprland-protocols"
source = f"{url}/archive/v{pkgver}/hyprland-protocols-v{pkgver}.tar.gz" 
sha256 = "5bbce79ad924310ebc3df30c5f409791b9c05764dc5268d2e37cbc001e3f9c6b"

def post_install(self):
	self.install_license("LICENSE")
