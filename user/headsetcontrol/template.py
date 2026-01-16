pkgname = "headsetcontrol"
pkgver = "3.1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["hidapi-devel"]
pkgdesc = "Tool to control gaming headsets"
license = "GPL-3.0-or-later"
url = "https://github.com/Sapd/HeadsetControl"
source = f"{url}/archive/refs/tags/3.1.0.tar.gz"
sha256 = "caba01afa69477f0a4fce1f8608a0c5e85e7032c350c1239bb4e1ecdfb171359"
