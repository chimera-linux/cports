pkgname = "base-quartzpro64"
pkgver = "0.1"
pkgrel = 1
archs = ["aarch64"]
depends = [
    "firmware-linux-rockchip",
    "u-boot-quartzpro64-rk3588",
    "u-boot-menu",
]
pkgdesc = "Chimera base package for QuartzPro64"
license = "custom:none"
url = "https://chimera-linux.org"


def install(self):
    # u-boot-menu
    self.install_file(self.files_path / "u-boot-device", "etc/default")
    self.install_file(self.files_path / "u-boot-cmdline", "etc/default")
    # agetty service customization
    self.install_file(self.files_path / "agetty", "etc/default")
    self.install_file(self.files_path / "agetty-ttyS2", "etc/default")
