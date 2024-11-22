# TODO: split devel, maybe the libs too? (may not be worth it)
pkgname = "erlang"
pkgver = "27.1.2"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
make_install_args = ["install-docs", "DOC_TARGETS=chunks"]
hostmakedepends = ["perl", "pkgconf", "xsltproc"]
makedepends = [
    "glu-devel",
    "linux-headers",
    "ncurses-devel",
    "openssl-devel",
    "unixodbc-devel",
    "wxwidgets-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Erlang OTP"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.erlang.org"
source = f"https://github.com/erlang/otp/archive/OTP-{pkgver}.tar.gz"
sha256 = "365208d47f9590f27c0814ccd7ee7aec0e1b6ba2fe9d875e356edb5d9b054541"
# some staticlibs inside the runtime should be non-lto
options = ["!cross", "!lto"]


def post_build(self):
    self.do("make", f"-j{self.make_jobs}", "DOC_TARGETS=chunks", "docs")


def check(self):
    self.do(
        "make",
        f"-j{self.make_jobs}",
        "release_tests",
        env={"ERL_TOP": self.chroot_cwd},
    )


@subpackage("erlang-wx")
def _(self):
    self.subdesc = "wxWidgets binding"
    self.depends = [self.parent]

    return ["usr/lib/erlang/lib/wx*"]
