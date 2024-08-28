# TODO: split devel, maybe the libs too? (may not be worth it)
pkgname = "erlang"
pkgver = "27.0.1"
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
sha256 = "47d96bb7044cf44bca886213fa828ef82457a911b7622c453d9b3c615b6f68ab"
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
