pkgname = "scrot"
pkgver = "1.11.1"
pkgrel = 0
build_style = "configure"
pkgdesc = "Screenshot utility for X11"
maintainer = "theuae <theuae@nanachi.network>"
license = "MIT-feh"
url = "https://github.com/resurrecting-open-source-projects/scrot"

configure_args = [ "--prefix=/usr" ]

hostmakedepends = [
    "imlib2",
    "imlib2-devel",
    "autoconf",
    "autoconf-archive",
    "pkgconf",
    "libx11",
    "libx11-devel",
    "libxcomposite",
    "libxcomposite-devel",
    "libxfixes",
    "libxfixes-devel",
    "libxinerama",
    "libxinerama-devel"
]
depends = [
    "imlib2",
    "libx11",
    "libxcomposite",
    "libxfixes",
    "libxinerama",
]

source = f"https://github.com/resurrecting-open-source-projects/scrot/releases/download/{pkgver}/scrot-{pkgver}.tar.gz"
sha256 = "c8ceda53b4ff76df4b9e51e9397acb4bcf12a51418895bf80c41f2a890e44738"

def post_install(self):
    self.install_license("COPYING")
