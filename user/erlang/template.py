# TODO: split devel, maybe the libs too? (may not be worth it)
pkgname = "erlang"
pkgver = "28.1.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
make_install_args = ["install-docs", "DOC_TARGETS=chunks"]
hostmakedepends = ["perl", "pkgconf", "libxslt-progs"]
makedepends = [
    "glu-devel",
    "linux-headers",
    "ncurses-devel",
    "openssl3-devel",
    "unixodbc-devel",
    "wxwidgets-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Erlang OTP"
license = "Apache-2.0"
url = "https://www.erlang.org"
source = f"https://github.com/erlang/otp/archive/OTP-{pkgver}.tar.gz"
sha256 = "69630ce5adcb3fc3ede136717c56f1dabff04d370451a27993f91a8f098fb339"
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
