# TODO: split devel, maybe the libs too? (may not be worth it)
pkgname = "erlang"
pkgver = "28.3.1"
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
sha256 = "0174210eef9db97d41fc277ee272d707f6ee4e07850225e6973216215946aad9"
# .beam/erl_process.c:9750:13: runtime error: signed integer overflow
hardening = ["!int"]
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
