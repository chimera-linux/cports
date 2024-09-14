pkgname = "thinkfan"
pkgver = "1.3.1"
pkgrel = 1
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["yaml-cpp-devel"]
pkgdesc = "Simple fan control program"
maintainer = "Val Packett <val@packett.cool>"
license = "GPL-3.0-or-later"
url = "https://github.com/vmatare/thinkfan"
source = f"https://github.com/vmatare/thinkfan/archive/{pkgver}.tar.gz"
sha256 = "9466c8c82b7c4333b280fa66445ab26185ffbb4aada6bcb4a164eed742f8d78c"
hardening = ["vis"]


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "thinkfan")
