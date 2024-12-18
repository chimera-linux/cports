pkgname = "ckms"
pkgver = "0.1.1"
pkgrel = 2
build_style = "makefile"
hostmakedepends = ["scdoc"]
depends = ["python"]
pkgdesc = "Chimera Kernel Module System"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/ckms"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d15e252fc5a9fa6d9a9187979512849b1634a52c4b98d44839a3f42464964021"
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
    # depmod hook
    self.install_file(self.files_path / "depmod.sh", "etc/ckms", mode=0o755)
