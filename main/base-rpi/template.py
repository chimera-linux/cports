pkgname = "base-rpi"
pkgver = "0.1"
pkgrel = 0
archs = ["aarch64"]
depends = ["firmware-rpi"]
pkgdesc = "Chimera base package for Raspberry Pi devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"


def do_install(self):
    self.install_file(
        self.files_path / "71-raspberrypi.rules", "usr/lib/udev/rules.d"
    )
    # kernel hook
    self.install_file(
        self.files_path / "99-rpi-kernel.sh", "etc/kernel.d", mode=0o755
    )
