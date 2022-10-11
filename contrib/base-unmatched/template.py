pkgname = "base-unmatched"
pkgver = "0.1"
pkgrel = 0
archs = ["riscv64"]
depends = ["linux", "u-boot-sifive_unmatched"]
pkgdesc = "Chimera base package for HiFive Unmatched"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"

def do_install(self):
    # kernel hook
    self.install_file(
        self.files_path / "99-unmatched-kernel.sh", "etc/kernel.d", mode = 0o755
    )
    # cmdline
    self.install_file(self.files_path / "unmatched-cmdline", "etc/default")
    # agetty service
    self.install_service(self.files_path / "agetty-ttySIF0")
