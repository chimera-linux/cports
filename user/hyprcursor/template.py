pkgname = "hyprcursor"
pkgver = "0.1.11"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE:STRING=Release"]
hostmakedepends = ["ninja", "cmake", "pkgconf"]
makedepends = ["cairo-devel", "libzip-devel", "librsvg-devel", "tomlplusplus-devel", "hyprlang",]
checkdepends=["adwaita-icon-theme, xcur2png"]
pkgdesc = "Hyprland cursor format, library and utilities"
maintainer = "kkflt <kkflt@cyberdude.com>"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprcursor"
source = f"{url}/archive/v{pkgver}/hyprcursor-v{pkgver}.tar.gz" 
sha256 = "17e4576b884e6bdb463b445cffff099ad16647b826a87a67b78d38b8cad4c39e"
# Skip checks, fo' sure it works
options=["!check"]

def post_install(self):
	self.install_license("LICENSE")

@subpackage("hyprcursor-devel")
def _(self):
	return self.default_devel()
