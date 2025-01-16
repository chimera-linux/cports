pkgname = "hyprutils"
pkgver = "0.3.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE:STRING=Release"]
hostmakedepends = ["ninja", "cmake", "pkgconf"]
makedepends = ["pixman-devel"]
pkgdesc = "Hyprland utilities library used across the ecosystem"
maintainer = "kkflt <kkflt@cyberdude.com>"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprutils"
source = f"{url}/archive/v{pkgver}/hyprutils-v{pkgver}.tar.gz" 
sha256 = "98cbf5750747cb7bda5665c8bcde5c21b5a449b67c508e9a806b46284efbe1d2"

def post_install(self):
	self.install_license("LICENSE")

@subpackage("hyprutils-devel")
def _(self):
	return self.default_devel()
