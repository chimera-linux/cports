pkgname = "libdispatch"
pkgver = "6.0.2"
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
sha256 = "3df429b22d9294c0ca5291c86e83a35f6326600a1c271933107bba199b919008"
hardening = ["vis", "!cfi"]


@subpackage("libdispatch-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
