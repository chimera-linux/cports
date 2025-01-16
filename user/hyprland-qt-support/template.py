pkgname = "hyprland-qt-support"
pkgver = "0.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE:STRING=Release", "-DINSTALL_QML_PREFIX=/lib/qt6/qml"]
hostmakedepends = ["cmake", "pkgconf", "ninja"]
makedepends = ["qt6-qtdeclarative-devel", "hyprlang"]
pkgdesc = "Qml style provider for hypr* qt apps"
maintainer = "kkflt <kkflt@cyberdude.com>"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprland-qt-support"
source = f"{url}/archive/v{pkgver}/hyprland-qtutils-v{pkgver}.tar.gz" 
sha256 = "cac1f980bd088b890097f3f999cfdf03e73ee94c53f3c92d0b3bc23baa9e7b2c"

def post_install(self):
	self.install_license("LICENSE")
