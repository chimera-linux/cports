pkgname = "kcov"
pkgver = "43"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = ["curl-devel", "elfutils-devel", "openssl3-devel"]
pkgdesc = "Code coverage tool"
license = "GPL-2.0-only"
url = "https://simonkagstrom.github.io/kcov"
source = (
    f"https://github.com/SimonKagstrom/kcov/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "4cbba86af11f72de0c7514e09d59c7927ed25df7cebdad087f6d3623213b95bf"
hardening = ["vis", "cfi"]
