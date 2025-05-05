pkgname = "libuv"
pkgver = "1.51.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Multi-platform support library with focus on asynchronous I/O"
license = "MIT"
url = "https://libuv.org"
source = f"https://dist.libuv.org/dist/v{pkgver}/libuv-v{pkgver}-dist.tar.gz"
sha256 = "2ceca1a7577633cf92794db5bf5512370f6cd45a5746d6e14f8c20aeab0a547b"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuv-devel")
def _(self):
    return self.default_devel()
