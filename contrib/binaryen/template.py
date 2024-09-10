pkgname = "binaryen"
pkgver = "119"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "python",
]
makedepends = ["gtest-devel"]
checkdepends = [
    "nodejs",
    "filecheck",
]
pkgdesc = "Optimizer and compiler/toolchain library for WebAssembly"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/WebAssembly/binaryen"
source = f"{url}/archive/refs/tags/version_{pkgver}.tar.gz"
sha256 = "9c2614212f628fad451b847ffa0ce2fc59339453f4ea1bacf4417590caa5fc71"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# FIXME: negoverflow wasm::Literal::abs in tests
hardening = ["!int"]
# take forever
options = ["!check"]


def check(self):
    self.do(
        "python",
        "check.py",
        "--no-torture",
        "--binaryen-bin",
        f"{self.make_dir}/bin",
    )


def post_install(self):
    self.uninstall("usr/bin/binaryen-unittests")


@subpackage("binaryen-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
