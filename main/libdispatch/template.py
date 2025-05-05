pkgname = "libdispatch"
pkgver = "6.1"
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
sha256 = "5bba8d7442890f7dbd37a9245340c5bb0c4c924dee6180ba30385b24e3fdf121"
hardening = ["vis", "!cfi"]


@subpackage("libdispatch-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
