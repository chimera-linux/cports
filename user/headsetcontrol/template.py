pkgname = "headsetcontrol"
pkgver = "3.1.0_git20260114"
pkgrel = 0
build_style = "cmake"
configure_args = [f"-DGIT_VERSION={pkgver}"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["hidapi-devel"]
pkgdesc = "Tool to control gaming headsets"
license = "GPL-3.0-or-later"
url = "https://github.com/Sapd/HeadsetControl"
# source = f"{url}/archive/refs/tags/3.1.0.tar.gz"
source = f"{url}/archive/6fe0cec4f8baeae5e6441489df02c395e39c6ae2.tar.gz"
sha256 = "9ee16cd2b54bd6630fd3cb34f5b25bd1004205babc9a2dfea7bb839980952183"


def post_install(self):
    # library not yet necessary
    self.uninstall("usr/include")
    self.uninstall("usr/lib/*.a", glob=True)
