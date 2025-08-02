pkgname = "ydotool"
pkgver = "1.0.4"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = ["cmake", "pkgconf", "ninja", "scdoc"]
makedepends = ["linux-headers"]
pkgdesc = "Generic command-line automation tool"
license = "AGPL-3.0-or-later"
url = "https://github.com/ReimuNotMoe/ydotool"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ba075a43aa6ead51940e892ecffa4d0b8b40c241e4e2bc4bd9bd26b61fde23bd"


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
    self.install_license("LICENSE")
