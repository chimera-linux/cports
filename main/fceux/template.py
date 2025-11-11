pkgname = "fceux"
pkgver = "2.6.6"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DQT6=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "ffmpeg-devel",
    "libarchive-devel",
    "lua5.1-devel",
    "minizip-devel",
    "qt6-qtdeclarative-devel",
    "sdl2-compat-devel",
]
pkgdesc = "NES/Famicom emulator"
license = "GPL-2.0-or-later"
url = "https://fceux.com"
source = (
    f"https://github.com/TASEmulators/fceux/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "0320241d45c6d609f7aeb6f85fdd9019552047206b0864a7f9fddff15b004daa"
hardening = ["!int"]
options = ["!cross"]


def post_install(self):
    # ???
    self.uninstall("usr/share/fceux/*.chm", glob=True)
    self.uninstall("usr/share/fceux/*.dll", glob=True)
