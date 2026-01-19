pkgname = "maim"
pkgver = "5.8.1"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
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
license = "GPL-3.0-or-later"
url = "https://github.com/naelstrof/maim"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6111555224a277b3698b465c24cef758c2cb7ef101ad22f0308ecd56ccd6c1e7"
# cfi: SIGILL when trying to take a screenshot
hardening = ["vis", "!cfi"]
