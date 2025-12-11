pkgname = "dinit-chimera-udev"
pkgver = "0.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "dinit-chimera",
    "libdinitctl-devel",
    "linux-headers",
    "udev-devel",
]
depends = [
    "cmd:udevadm>=256.6-r1!udev",
]
provides = [self.with_pkgver("dinit-chimera-device")]
replaces = [
    "dinit-chimera<=0.99.21-r0",
    "udev<=256.11-r2",
    "udev-dinit<=256.11-r2",
    "udev-dinit-links<=256.11-r2",
]
pkgdesc = "Udev integration for Chimera core services"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-chimera-udev"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "346a4012b9d6364b243d8191123bdbdfae9c445c3e40abd0c225a1009f650eeb"
hardening = ["vis", "cfi"]
options = ["!splitdinit"]


def post_install(self):
    self.install_license("COPYING.md")
    self.install_file(self.files_path / "udevd.wrapper", "usr/lib", mode=0o755)
    self.install_file(self.files_path / "dinit-devd", "usr/lib", mode=0o755)
    self.install_service(self.files_path / "udevd", enable=True)
