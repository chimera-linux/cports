pkgname = "libdispatch"
pkgver = "6.1.2"
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
license = "Apache-2.0"
url = "https://apple.github.io/swift-corelibs-libdispatch"
source = f"https://github.com/apple/swift-corelibs-libdispatch/archive/refs/tags/swift-{pkgver}-RELEASE.tar.gz"
sha256 = "26e8f6d661415502c10f909835961cac4edf56a0ab9512a9988489fe98601385"
hardening = ["vis", "!cfi"]


@subpackage("libdispatch-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
