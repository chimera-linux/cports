pkgname = "lxqt-openssh-askpass"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja", "perl"]
makedepends = [
    "kwindowsystem-devel",
    "liblxqt-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "GUI to query passwords on behalf of SSH agents"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/lxqt-openssh-askpass"
source = (
    f"{url}/releases/download/{pkgver}/lxqt-openssh-askpass-{pkgver}.tar.xz"
)
sha256 = "294a20ea148b4c4c6aff9b6cd7b563d7d2ec0d2fa6c2bc18129b4793f86c8c0f"
