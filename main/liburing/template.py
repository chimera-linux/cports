pkgname = "liburing"
pkgver = "2.9"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later OR MIT"
url = "https://github.com/axboe/liburing"
source = f"{url}/archive/refs/tags/liburing-{pkgver}.tar.gz"
sha256 = "897b1153b55543e8b92a5a3eb9b906537a5fedcf8afaf241f8b8787940c79f8d"
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
