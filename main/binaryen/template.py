pkgname = "binaryen"
pkgver = "121"
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
    "lit",
    "llvm-tools",
]
pkgdesc = "Optimizer and compiler/toolchain library for WebAssembly"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/WebAssembly/binaryen"
source = [
    f"{url}/archive/refs/tags/version_{pkgver}.tar.gz",
    "https://github.com/WebAssembly/testsuite/archive/e05365077e13a1d86ffe77acfb1a835b7aa78422.tar.gz",
]
source_paths = [".", "test/spec/testsuite"]
sha256 = [
    "93f3b3d62def4aee6d09b11e6de75b955d29bc37878117e4ed30c3057a2ca4b4",
    "0c9961b7b308f87bed2f8187892047fe5575af2298d0bfdca526223219dfc899",
]
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# FIXME: negoverflow wasm::Literal::abs in tests
hardening = ["!int"]
# 'filecheck' is a shitty python port of the llvm FileCheck, just use the original
# only for 'lit' below
exec_wrappers = [("/usr/bin/FileCheck", "filecheck")]


def check(self):
    self.do(
        "python",
        "check.py",
        "--no-torture",
        "--binaryen-bin",
        f"{self.make_dir}/bin",
        "crash",
        "dylink",
        "example",
        "gtest",
        "lld",
        "unit",
        "validator",
        "version",
        "wasm-opt",
        # fail with llvm18 lit lol
        # "lit",
    )


def post_install(self):
    self.uninstall("usr/bin/binaryen-unittests")


@subpackage("binaryen-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
