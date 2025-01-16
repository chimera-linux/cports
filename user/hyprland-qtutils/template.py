pkgname = "hyprland-qtutils"
pkgver = "0.1.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE:STRING=Release"]
hostmakedepends = ["cmake", "pkgconf", "ninja"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qtwayland-devel", "hyprutils-devel"]
depends = ["hyprland-qt-support"]
pkgdesc = "Hyprland QT/qml utility apps"
maintainer = "kkflt <kkflt@cyberdude.com>"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprland-qtutils"
source = f"{url}/archive/v{pkgver}/hyprland-qtutils-v{pkgver}.tar.gz" 
sha256 = "3e57617ebd849ebf074c492bf828efa37a5b47fd6d43b392462874069170c5ed"

def post_install(self):
	self.install_license("LICENSE")
