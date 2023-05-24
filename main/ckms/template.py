pkgname = "ckms"
pkgver = "0.1.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["scdoc"]
depends = ["python"]
triggers = ["/usr/src"]
pkgdesc = "Chimera Kernel Module System"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/ckms"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "29e19116397cf0a50bb49a87b09d816cf8d233aa7016c4884d1ff88bfbc6ab27"
# no tests
options = ["!check"]
system_users = ["_ckms"]


def post_install(self):
    # kernel hook
    self.install_file(
        self.files_path / "10-ckms.sh", "etc/kernel.d", mode=0o755
    )
    # initramfs refresh hook
    self.install_file(
        self.files_path / "refresh-initramfs.sh", "etc/ckms", mode=0o755
    )
    # helpers
    self.install_file(
        self.files_path / "ckms-install-all", "usr/libexec", mode=0o755
    )
