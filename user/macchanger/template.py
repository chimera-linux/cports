pkgname = "macchanger"
pkgver = "1.7.0"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["autoconf", "automake"]
makedepends = ["dinit-chimera", "linux-headers"]
pkgdesc = "GNU MAC Changer"
license = "GPL-3.0-only"
url = "http://www.gnu.org/software/macchanger"
source = f"https://github.com/alobbs/macchanger/releases/download/{pkgver}/macchanger-{pkgver}.tar.gz"
sha256 = "dae2717c270fd5f62d790dbf80c19793c651b1b26b62c101b82d5fdf25a845bf"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_service(self.files_path / "macchanger")
