pkgname = "libdispatch"
pkgver = "5.9.2"
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
sha256 = "b1f3e46ed248df6a3456d20bc23b2d8a12b740a40185d81b668b1d31735cadf2"
# FIXME: cfi
hardening = ["vis"]


@subpackage("libdispatch-devel")
def _devel(self):
    # .so libs are unversioned but abi stable
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return ["usr/include"]
