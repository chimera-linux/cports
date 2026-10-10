pkgname = "bandicoot"
pkgver = "0_git20261010"
pkgrel = 0
_gitrev = "8770fae3016a325f38f9d3092b5847346537d6eb"
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["dinit-chimera", "linux-headers", "zstd-devel"]
pkgdesc = "Crash dump handler"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bandicoot"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "6cdd6c1ab307350d407ed505479247c6e6701720ddbbfdccce8af478aa26dbb0"


def post_install(self):
    self.install_service(self.files_path / "bandicootd")
    self.install_license("COPYING.md")
