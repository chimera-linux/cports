pkgname = "nc"
pkgver = "3.8.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DLIBRESSL_SKIP_INSTALL=true"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["openssl-devel", "libretls-devel"]
pkgdesc = "TCP/IP swiss army knife - OpenBSD variant"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "BSD-3-Clause"
url = "https://man.openbsd.org/nc.1"
source = (
    f"https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-{pkgver}.tar.gz"
)
sha256 = "6d4b8d5bbb25a1f8336639e56ec5088052d43a95256697a85c4ce91323c25954"
hardening = ["vis", "cfi"]
# no testsuite
options = ["!check"]


def post_extract(self):
    for f in (
        "strtonum.c",
        "arc4random.c",
        "arc4random_uniform.c",
        "chacha_private.h",
    ):
        self.cp(f"crypto/compat/{f}", "apps/nc/compat")
    self.cp("crypto/compat/arc4random_linux.h", "apps/nc/compat/arc4random.h")
    with self.pushd("apps/nc"):
        self.cp("netcat.c", "LICENSE")
        self.do("sed", "-n", "-i.bak", r"1,2d;\-^ \*/-q;s/^ \* //p", "LICENSE")


def post_install(self):
    self.install_license("apps/nc/LICENSE")
