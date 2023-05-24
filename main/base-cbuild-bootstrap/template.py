pkgname = "base-cbuild-bootstrap"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "base-cbuild-host",  # all the host tools for cbuild itself
    # toolchain base
    "clang",
    "lld",
    "elftoolchain",
    "linux-headers",
    # stage 0 tooling
    "pkgconf",
    "byacc",
    "flex",
    "perl",
    # stage 0 build systems
    "cmake",
    "meson",
    "bmake",
    "gmake",
    "ninja",
]
pkgdesc = "Everything one needs to build Chimera from source"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
