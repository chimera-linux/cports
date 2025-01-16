pkgname = "hyprgraphics"
pkgver = "0.1.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE:STRING=Release"]
hostmakedepends = ["meson", "cmake", "pkgconf"]
makedepends = [
	"pixman-devel",
	"cairo-devel",
	"hyprutils-devel",
	"file-devel",
	"libjpeg-turbo-devel",
	"libjxl-devel",
	"libwebp-devel",
		
]
pkgdesc = "Hyprland graphics / resource utilities"
maintainer = "kkflt <kkflt@cyberdude.com>"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprgraphics"
source = f"{url}/archive/v{pkgver}/hyprgraphics-v{pkgver}.tar.gz" 
sha256 = "123a29e53a00bfaf37e7971b929433fb716fd497b3555f72c2d0419ae18e65c7"

def post_install(self):
	self.install_license("LICENSE")

@subpackage("hyprgraphics-devel")
def _(self):
	return self.default_devel()
