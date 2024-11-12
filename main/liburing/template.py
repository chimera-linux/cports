pkgname = "liburing"
pkgver = "2.8"
pkgrel = 1
build_style = "configure"
configure_args = ["--mandir=/usr/share/man", "--use-libc"]
make_check_target = "runtests"
hostmakedepends = [
    "bash",
    "pkgconf",
]
makedepends = ["linux-headers", "musl-bsd-headers"]
pkgdesc = "Linux kernel io_uring access library"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later OR MIT"
url = "https://github.com/axboe/liburing"
source = f"{url}/archive/refs/tags/liburing-{pkgver}.tar.gz"
sha256 = "3ed7891d1b2bbe743ef3fb6d0a4970e630aa02d7c7bd3b0212791fb7be815984"
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
