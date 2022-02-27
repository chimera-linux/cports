pkgname = "ckms"
pkgver = "0.0.1_git2022027"
_commit = "fc0ea30b3e7fa1c5001e2bf8f12e637150b59256"
pkgrel = 0
depends = ["python"]
triggers = ["/usr/src"]
pkgdesc = "Chimera Kernel Module System"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/ckms"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "3063dfac7f2ee02d86e9ac3d19cfeed32d882de2be16c633f94881b5c90753ea"
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
