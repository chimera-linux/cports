pkgname = "fvwm3"
pkgver = "1.1.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-mandoc"]
configure_gen = ["./autogen.sh"]
make_dir = "."
hostmakedepends = ["asciidoctor", "automake", "libtool", "pkgconf"]
makedepends = [
    "fribidi-devel",
    "libevent-devel",
    "libpng-devel",
    "librsvg-devel",
    "libxcursor-devel",
    "libxft-devel",
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
sha256 = "fde449c21678e059d16278da3ac69f3786aed96cac90962163e72bf59e840421"
