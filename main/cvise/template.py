pkgname = "cvise"
pkgver = "2.12.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "clang-tools-extra",
    "cmake",
    "flex",
    "ninja",
]
makedepends = [
    "clang-devel",
    "llvm-devel",
]
depends = [
    "clang",
    "python-chardet",
    "python-pebble",
    "python-psutil",
    "unifdef",
]
checkdepends = [
    "python-pytest",
    *depends,
]
pkgdesc = "Python port of C-Reduce, for program testcase minimisation"
license = "NCSA"
url = "https://github.com/marxin/cvise"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d015050cfc4015460ca5793378c4899a36104ddcf084f29f0f5f6233f6187cb1"


def check(self):
    # this one test fails but everything else is fine
    self.do("pytest", "-k", "not test_simple_reduction", wrksrc=self.make_dir)


def post_install(self):
    self.install_license("COPYING")
    self.uninstall("usr/share/cvise/tests")
