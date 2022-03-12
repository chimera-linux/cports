pkgname = "ckms"
pkgver = "0.0.1_git20220312"
_commit = "e3d4c61094f79de913721b0347527febc2879f51"
pkgrel = 0
depends = ["python"]
triggers = ["/usr/src"]
pkgdesc = "Chimera Kernel Module System"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/ckms"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "ffe0d1430618f8623d778a03224f89c39738e853efb53040e80f03fa2e9b33a0"
# no tests
options = ["!check"]
system_users = ["_ckms"]

def do_install(self):
    self.install_dir("etc/ckms")
    self.install_file("config.ini", "etc/ckms")
    self.install_bin("ckms")
    # kernel hook
    self.install_file(
        self.files_path / "10-ckms.sh", "etc/kernel.d", mode = 0o755
    )
    # initramfs refresh hook
    self.install_file(
        self.files_path / "refresh-initramfs.sh", "etc/ckms", mode = 0o755
    )
