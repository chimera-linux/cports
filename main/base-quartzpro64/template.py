pkgname = "base-quartzpro64"
pkgver = "0.1"
pkgrel = 2
archs = ["aarch64"]
depends = [
    "firmware-linux-rockchip",
    "u-boot-menu",
    "u-boot-quartzpro64-rk3588",
]
pkgdesc = "Chimera base package for QuartzPro64"
license = "custom:none"
url = "https://chimera-linux.org"


def install(self):
    # u-boot-menu
    self.install_file(self.files_path / "device", "usr/lib/u-boot")
    self.install_file(self.files_path / "cmdline", "usr/lib/u-boot")
