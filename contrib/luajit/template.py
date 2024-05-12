pkgname = "luajit"
pkgver = "2.1_p20231117"
pkgrel = 1
archs = ["aarch64", "ppc64le", "ppc64", "x86_64"]
_tests_rev = "9ad3724b1a02855a3cad638bba2e564f825954ce"
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "amalg"
make_build_args = ["PREFIX=/usr", "Q=", "E=@:"]
make_use_env = True
hostmakedepends = ["gmake", "pkgconf"]
checkdepends = [
    "perl",
    "sqlite-devel",
    "zlib-devel",
]
pkgdesc = "OpenResty's LuaJIT fork"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/openresty/luajit2"
source = [
    f"{url}/archive/refs/tags/v{pkgver.replace('_p', '-')}.tar.gz",
    f"{url}-test-suite/archive/{_tests_rev}.tar.gz",
]
source_paths = [
    ".",
    "test-suite",
]
sha256 = [
    "cc92968c57c00303eb9eaebf65cc8b29a0f851670f16bb514896ab5057ae381f",
    "f87648d5392b0fa7a82107b84478d1011d12f82920b2757ca0029c9330c2fb3e",
]
hardening = []
# cba
options = ["!cross"]


if self.profile().arch == "aarch64":
    # fails buildvm
    hardening += ["!int"]


def init_build(self):
    cc = self.get_tool("CC")
    cfl = self.get_cflags(shell=True)
    ldfl = self.get_ldflags(shell=True)
    hcc = self.get_tool("CC", target="host")
    hcfl = self.get_cflags(shell=True, target="host")
    hldfl = self.get_ldflags(shell=True, target="host")
    # build system is dumb and does not pass link args properly
    self.make_build_args += [
        f"CC={cc}",
        f"TARGET_CFLAGS={cfl}",
        f"TARGET_LDFLAGS={cfl} {ldfl}",
        f"TARGET_SHLDFLAGS={cfl} {ldfl}",
        f"HOST_CC={hcc}",
        f"HOST_CFLAGS={hcfl}",
        f"HOST_LDFLAGS={hcfl} {hldfl}",
    ]


def do_check(self):
    pfx = str(self.chroot_cwd / "test-suite/target")
    self.do("gmake", "install", "PREFIX=" + pfx)
    self.do(
        "./run-tests",
        pfx,
        f"{pfx}/bin/luajit",
        "clang",
        "clang++",
        wrksrc="test-suite",
    )


def post_install(self):
    self.install_license("COPYRIGHT")


@subpackage("luajit-devel")
def _devel(self):
    return self.default_devel()
