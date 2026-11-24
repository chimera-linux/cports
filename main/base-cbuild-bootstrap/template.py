pkgname = "base-cbuild-bootstrap"
pkgver = "0.1"
pkgrel = 5
build_style = "meta"
depends = [
    # stage 0 build systems
    "automake",
    "base-cbuild-host",  # all the host tools for cbuild itself
    "byacc",
    "cmake",
    "flex",
    "gmake",
    "libtool",
    "linux-headers",
    "llvm-clang",
    "meson",
    "ninja",
    "perl",
    # stage 0 tooling
    "pkgconf",
]
pkgdesc = "Everything one needs to build Chimera from source"
license = "custom:meta"
url = "https://chimera-linux.org"
