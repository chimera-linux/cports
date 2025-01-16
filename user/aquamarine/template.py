pkgname = "aquamarine" 
pkgver = "0.7.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["pkgconf", "ninja"]
makedepends = [
 	"cmake",
 	"udev-devel",
 	"hwdata-devel",
 	"hyprutils-devel",
 	"hyprwayland-scanner",
 	"libdisplay-info-devel",
 	"libinput-devel",
 	"libseat-devel",
 	"mesa-devel",
 	"pixman-devel",
 	"wayland-devel",
 	"wayland-protocols",
]
pkgdesc = "Aquamarine is a very light linux rendering backend library"
maintainer = "kkflt <kkftl@cyberdude.com>"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/aquamarine"
source = f"{url}/archive/v{pkgver}/aquamarine-v{pkgver}.tar.gz"
sha256 = "e61453345e1df9c37cedd10d4c48df0b2d3a53d8e535fc71c3dd06f88f1d31f3"
# tests are broken
options= ["!check"]

def post_install(self):
	self.install_license("LICENSE")

@subpackage("aquamarine-devel")
def _(self):
	return self.default_devel()
