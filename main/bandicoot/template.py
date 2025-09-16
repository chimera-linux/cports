pkgname = "bandicoot"
pkgver = "0_git20250216"
pkgrel = 0
_gitrev = "84fccd824c32d4cea26161f10b52bf5ca324d5b1"
build_style = "meson"
configure_args = ["--libexecdir=/usr/lib"]  # XXX libexecdir
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["dinit-chimera", "linux-headers", "zstd-devel"]
pkgdesc = "Crash dump handler"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bandicoot"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "599b6f69c8cbab835b59811298824e26f992d5989e9ea965fc9953b936d286e2"


def post_install(self):
    self.install_service(self.files_path / "bandicootd")
    self.install_license("COPYING.md")
