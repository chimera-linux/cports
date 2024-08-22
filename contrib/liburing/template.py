pkgname = "liburing"
pkgver = "2.7"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later OR MIT"
url = "https://git.kernel.dk/cgit/liburing"
source = f"{url}/snapshot/liburing-{pkgver}.tar.gz"
sha256 = "29c0897868cb612b71728e680fa5fac4c5c9fc51166d8c42a0261f061f4658ae"
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
