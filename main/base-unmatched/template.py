pkgname = "base-unmatched"
pkgver = "0.1"
pkgrel = 2
archs = ["riscv64"]
depends = ["u-boot-sifive_unmatched", "u-boot-menu"]
pkgdesc = "Chimera base package for HiFive Unmatched"
license = "custom:none"
url = "https://chimera-linux.org"


def install(self):
    # u-boot-menu
    self.install_file(self.files_path / "device", "usr/lib/u-boot")
    self.install_file(self.files_path / "cmdline", "usr/lib/u-boot")
