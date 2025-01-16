pkgname = "hyprwayland-scanner"
pkgver = "0.4.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["ninja", "cmake", "pkgconf"]
makedepends = ["pugixml-devel"]
depends = ["pugixml"]
pkgdesc = "Hyprland implementation of wayland-scanner, in and for C++"
maintainer = "kkflt <kkflt@cyberdude.com>"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprwayland-scanner"
source = f"{url}/archive/v{pkgver}/hyprwayland-scanner-v{pkgver}.tar.gz" 
sha256 = "ac73f626019f8d819ff79a5fca06ce4768ce8a3bded6f48c404445f3afaa25ac"

def post_install(self):
	self.install_license("LICENSE")
