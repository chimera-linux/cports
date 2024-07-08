pkgname = "binaryen"
pkgver = "117"
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
    "python-filecheck",
]
pkgdesc = "Optimizer and compiler/toolchain library for WebAssembly"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/WebAssembly/binaryen"
source = f"{url}/archive/refs/tags/version_{pkgver}.tar.gz"
sha256 = "9acf7cc5be94bcd16bebfb93a1f5ac6be10e0995a33e1981dd7c404dafe83387"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# take forever
options = ["!check"]


def do_check(self):
    self.do(
        "python",
        "check.py",
        "--no-torture",
        "--binaryen-bin",
        f"{self.chroot_cwd}/{self.make_dir}/bin",
    )


def post_install(self):
    self.uninstall("usr/bin/binaryen-unittests")


@subpackage("binaryen-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
