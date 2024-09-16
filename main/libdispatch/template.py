pkgname = "libdispatch"
pkgver = "6.0"
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
sha256 = "fa6fe877cf88391d3faba14147ed5531871b424b28e854534f28e83fc77d2081"
hardening = ["vis", "!cfi"]


@subpackage("libdispatch-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
