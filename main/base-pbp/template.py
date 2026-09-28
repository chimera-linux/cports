pkgname = "base-pbp"
pkgver = "0.1"
pkgrel = 2
archs = ["aarch64"]
depends = [
    "firmware-ap6256",
    "firmware-linux-rockchip",
    "u-boot-menu",
    "u-boot-pinebook-pro-rk3399",
]
pkgdesc = "Chimera base package for Pinebook Pro"
license = "custom:none"
url = "https://chimera-linux.org"


def install(self):
    self.install_file(
        self.files_path / "60-pinebookpro.rules", "usr/lib/udev/rules.d"
    )
    self.install_file(
        self.files_path / "10-pinebookpro.hwdb", "usr/lib/udev/hwdb.d"
    )
    # u-boot-menu
    self.install_file(self.files_path / "device", "usr/lib/u-boot")
    self.install_file(self.files_path / "cmdline", "usr/lib/u-boot")
