pkgname = "ckms"
pkgver = "0.1.0"
pkgrel = 4
build_style = "makefile"
hostmakedepends = ["scdoc"]
depends = ["python"]
pkgdesc = "Chimera Kernel Module System"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/ckms"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "29e19116397cf0a50bb49a87b09d816cf8d233aa7016c4884d1ff88bfbc6ab27"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING.md")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    # kernel hook
    self.install_file(
        self.files_path / "10-ckms.sh", "usr/lib/kernel.d", mode=0o755
    )
    # initramfs refresh hook
    self.install_file(
        self.files_path / "refresh-initramfs.sh", "etc/ckms", mode=0o755
    )
