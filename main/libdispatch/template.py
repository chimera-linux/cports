pkgname = "libdispatch"
pkgver = "6.0.3"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://apple.github.io/swift-corelibs-libdispatch"
source = f"https://github.com/apple/swift-corelibs-libdispatch/archive/refs/tags/swift-{pkgver}-RELEASE.tar.gz"
sha256 = "444c0de5fe18e148548a3f3b60b3bac3d4d586285c21064346c7ca17ed1d4fac"
hardening = ["vis", "!cfi"]


@subpackage("libdispatch-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
