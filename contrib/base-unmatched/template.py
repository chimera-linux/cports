pkgname = "base-unmatched"
pkgver = "0.1"
pkgrel = 1
archs = ["riscv64"]
depends = ["u-boot-sifive_unmatched", "u-boot-menu"]
pkgdesc = "Chimera base package for HiFive Unmatched"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"


def do_install(self):
    self.install_file(self.files_path / "agetty", "etc/default")
    # u-boot-menu
    self.install_file(self.files_path / "u-boot-device", "etc/default")
    self.install_file(self.files_path / "u-boot-cmdline", "etc/default")
