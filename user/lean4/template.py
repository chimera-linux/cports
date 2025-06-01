pkgname = "lean4"
pkgver = "4.21.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    # requires llvm 15
    "-DLLVM=OFF",
    # lol
    "-DUSE_MIMALLOC=NO",
    # add it to depends instead of installing a copy
    "-DINSTALL_CADICAL=NO",
]
# ninja: error: build.ninja:478: bad $-escape (literal $ must be written as $$)
make_cmd = "make"
make_check_target = "test"
hostmakedepends = [
    "bash",
    "cadical",
    "cmake",
    "pkgconf",
    "python",
]
makedepends = [
    "gmp-devel",
    "libuv-devel",
]
checkdepends = ["perl"]
# bash and make are executed from the leanmake script
# git is executed by lake
depends = [
    "cmd:bash!bash",
    "cmd:cadical!cadical",
    "cmd:git!git",
    "cmd:make!gmake",
    "gmp-devel",
    "libuv-devel",
    self.with_pkgver("lean4-devel-static"),
]
pkgdesc = "Proof assistant and functional programming language"
license = "Apache-2.0"
url = "https://lean-lang.org"
source = (
    f"https://github.com/leanprover/lean4/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "fb4a1b696fad43336267e9b2f70f3cfb97e4c7f9985af0eee655732312ed7d48"
# int: -fwrapv
hardening = ["!int"]


def init_configure(self):
    # make lean itself use our flags
    self.configure_args += [
        "-DLEAN_EXTRA_CXX_FLAGS=" + self.get_cxxflags(shell=True),
        "-DLEANC_EXTRA_CC_FLAGS=" + self.get_cflags(shell=True),
        "-DLEAN_EXTRA_LINKER_FLAGS=" + self.get_ldflags(shell=True),
    ]


def init_check(self):
    self.make_check_args += [f"ARGS=-j{self.make_jobs}"]


@subpackage("lean4-devel")
def _(self):
    return self.default_devel()


@subpackage("lean4-devel-static")
def _(self):
    return ["usr/lib/lean/*.a"]
