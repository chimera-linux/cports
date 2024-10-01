pkgname = "maim"
pkgver = "5.8.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "glew-devel",
    "glm",
    "icu-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libwebp-devel",
    "libxcomposite-devel",
    "libxrandr-devel",
    "libxrender-devel",
    "slop-devel",
]
pkgdesc = "X11 screenshot utility"
maintainer = "peri <peri@periwinkle.sh>"
license = "GPL-3.0-or-later"
url = "https://github.com/naelstrof/maim"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ecafe01dcbe4246071c58ff36acdcd93d290ed501f67933334b646436650450e"
hardening = ["vis", "cfi"]
