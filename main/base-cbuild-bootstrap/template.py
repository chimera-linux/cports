pkgname = "base-cbuild-bootstrap"
pkgver = "0.1"
pkgrel = 4
build_style = "meta"
depends = [
    # stage 0 build systems
    "automake",
    "base-cbuild-host",  # all the host tools for cbuild itself
    "byacc",
    # toolchain base
    "clang",
    "cmake",
    "flex",
    "gmake",
    "libtool",
    "linux-headers",
    "lld",
    "meson",
    "ninja",
    "perl",
    # stage 0 tooling
    "pkgconf",
]
pkgdesc = "Everything one needs to build Chimera from source"
license = "custom:meta"
url = "https://chimera-linux.org"
