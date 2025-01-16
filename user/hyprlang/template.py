pkgname = "hyprlang"
pkgver = "0.6.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE:STRING=Release"]
hostmakedepends = ["cmake", "pkgconf", "ninja"]
makedepends = ["hyprutils-devel"]
pkgdesc = "Official implementation library for the hypr config language"
maintainer = "kkflt <kkflt@cyberdude.com>"
license = "LGPL-3.0-only"
url = "https://github.com/hyprwm/hyprlang"
source = f"{url}/archive/v{pkgver}/hyprlang-v{pkgver}.tar.gz" 
sha256 = "b1a163606402041d92507936fb6dcbc40dd0035b8e8abbf44b0ab59be627b52c"

def post_install(self):
	self.install_license("LICENSE")
