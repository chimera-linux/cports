pkgname = "liburing"
pkgver = "2.15"
pkgrel = 0
build_style = "configure"
configure_args = ["--mandir=/usr/share/man", "--use-libc"]
make_check_target = "runtests"
hostmakedepends = [
    "bash",
    "bpftool",
    "pkgconf",
]
makedepends = ["libbpf-devel", "linux-headers", "musl-bsd-headers"]
pkgdesc = "Linux kernel io_uring access library"
license = "LGPL-2.1-or-later OR MIT"
url = "https://github.com/axboe/liburing"
source = f"{url}/archive/refs/tags/liburing-{pkgver}.tar.gz"
sha256 = "8d052f2622dcb3678cbaee5ff582a87572672a6c0a56533cdda5b65cb636120a"
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
