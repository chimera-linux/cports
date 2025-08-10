pkgname = "thinkfan"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["yaml-cpp-devel", "lm-sensors-devel"]
pkgdesc = "Simple fan control program"
license = "GPL-3.0-or-later"
url = "https://github.com/vmatare/thinkfan"
source = f"https://github.com/vmatare/thinkfan/archive/{pkgver}.tar.gz"
sha256 = "0fc94eb378dcba8c889e91f41dab3a8d6eebc7324a59a0704cc39aa66551987e"
hardening = ["vis"]


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "thinkfan")
