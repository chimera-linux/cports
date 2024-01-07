pkgname = "base-rpi"
pkgver = "0.3"
pkgrel = 0
archs = ["aarch64"]
depends = ["rpi-boot", "firmware-linux-brcm-rpi"]
replaces = ["firmware-rpi<=20220905-r0"]
pkgdesc = "Chimera base package for Raspberry Pi devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"


def do_install(self):
    # config
    self.install_file(self.files_path / "rpi-cmdline.txt", "etc/default")
    self.install_file(self.files_path / "rpi-config.txt", "etc/default")

    self.install_file(
        self.files_path / "71-raspberrypi.rules", "usr/lib/udev/rules.d"
    )
    # kernel hook
    self.install_file(
        self.files_path / "99-rpi-kernel.sh", "etc/kernel.d", mode=0o755
    )
