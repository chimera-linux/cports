pkgname = "luajit"
pkgver = "2.1_p20241113"
pkgrel = 0
archs = ["aarch64", "ppc64le", "ppc64", "x86_64"]
_tests_rev = "a3a5deb5d97d57fb4da567017a621ae73ee7305e"
build_style = "makefile"
make_build_target = "amalg"
make_build_args = ["PREFIX=/usr", "Q=", "E=@:"]
make_use_env = True
hostmakedepends = ["pkgconf"]
checkdepends = [
    "perl",
    "sqlite-devel",
    "zlib-ng-compat-devel",
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
    "3b269f3a55c420e5a286bbd6b8ef8a5425dbcb4194fa2beb9e22eea277cd6638",
    "b9862f002768dac55c8ab3d1ea21f3aa06d4075f6d022bb2eff76e82df264ffc",
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


def check(self):
    pfx = str(self.chroot_cwd / "test-suite/target")
    self.do("make", "install", "PREFIX=" + pfx)
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
def _(self):
    return self.default_devel()
