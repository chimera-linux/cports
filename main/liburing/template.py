pkgname = "liburing"
pkgver = "2.8"
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
sha256 = "e289852ddf6dd1428afd509eac5a4549e050398fcde7a467fa57f53efa3df64c"
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
