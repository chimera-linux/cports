pkgname = "liburing"
pkgver = "2.12"
pkgrel = 0
build_style = "configure"
configure_args = ["--mandir=/usr/share/man", "--use-libc"]
make_check_target = "runtests"
hostmakedepends = [
    "bash",
    "pkgconf",
]
makedepends = ["linux-headers", "musl-bsd-headers"]
pkgdesc = "Linux kernel io_uring access library"
license = "LGPL-2.1-or-later OR MIT"
url = "https://github.com/axboe/liburing"
source = f"{url}/archive/refs/tags/liburing-{pkgver}.tar.gz"
sha256 = "f1d10cb058c97c953b4c0c446b11e9177e8c8b32a5a88b309f23fdd389e26370"
# vis breaks symbols
hardening = ["!vis", "!cfi"]
# FIXME: run into timeout
options = ["!check", "linkundefver"]


def init_configure(self):
    majver, minver = pkgver.split(".")
    self.env["VERSION_MAJOR"] = majver
    self.env["VERSION_MINOR"] = minver


def post_install(self):
    self.install_license("LICENSE")


@subpackage("liburing-devel")
def _(self):
    return self.default_devel()
