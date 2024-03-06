pkgname = "libdispatch"
pkgver = "5.10"
pkgrel = 0
build_style = "cmake"
# these always fail on linux for some reason on musl
make_check_args = ["-E", "dispatch_*"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "linux-headers",
    "musl-bsd-headers",
]
pkgdesc = "Apple's concurrent threading library"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://apple.github.io/swift-corelibs-libdispatch"
source = f"https://github.com/apple/swift-corelibs-libdispatch/archive/refs/tags/swift-{pkgver}-RELEASE.tar.gz"
sha256 = "16e088cf12654d22658879710b9694a6fad1c94d5e5d0c597741b71fbcb3e034"
# FIXME: cfi
hardening = ["vis"]


@subpackage("libdispatch-devel")
def _devel(self):
    # .so libs are unversioned but abi stable
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return ["usr/include"]
