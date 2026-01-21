pkgname = "cockatrice"
pkgver = "2.10.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
makedepends = [
    "protobuf-devel",
    "qt6-qtbase-devel",
    "qt6-qtimageformats-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwebsockets-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Virtual tabletop for multiplayer card games"
license = "GPL-2.0-only"
url = "https://cockatrice.github.io"
source = "https://github.com/Cockatrice/Cockatrice/archive/refs/tags/2025-04-03-Release-2.10.2.tar.gz"
sha256 = "73cabec34604261b3ec2beb66b6a11faff0b0d1ca50f25cc58a45325a39225d4"
