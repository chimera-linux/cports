pkgname = "fvwm3"
pkgver = "1.1.5"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dmandoc=true",
]
# avoid clash with script called 'build'
make_dir = "compile"
hostmakedepends = ["asciidoctor", "meson", "perl", "pkgconf"]
makedepends = [
    "fribidi-devel",
    "libevent-devel",
    "libpng-devel",
    "librsvg-devel",
    "libxcursor-devel",
    "libxft-devel",
    "libxkbcommon-devel",
    "libxpm-devel",
    "libxrandr-devel",
    "libxt-devel",
    "musl-bsd-headers",
    "xtrans",
]
pkgdesc = "X11 window manager"
license = "GPL-2.0-or-later"
url = "https://github.com/fvwmorg/fvwm3"
source = f"{url}/releases/download/{pkgver}/fvwm3-{pkgver}.tar.gz"
sha256 = "6b827885e226261eda97fec57ec03feb5e82e102f3081a3dc941020403a9c196"
