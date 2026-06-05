pkgname = "xdelta"
pkgver = "3.1.0"
pkgrel = 0
build_wrksrc = "xdelta3"
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
]
pkgdesc = "Delta compression using VCDIFF/RFC 3284 streams"
license = "GPL-2.0-only"
url = "https://github.com/jmacd/xdelta"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7515cf5378fca287a57f4e2fee1094aabc79569cfe60d91e06021a8fd7bae29d"
