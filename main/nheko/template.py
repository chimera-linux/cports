pkgname = "nheko"
pkgver = "0.12.0"
pkgrel = 4
build_style = "cmake"
hostmakedepends = [
    "asciidoctor",
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qttools-devel",
]
makedepends = [
    "cmark-devel",
    "coeurl-devel",
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "kdsingleapplication-devel",
    "curl-devel",
    "libevent-devel",
    "lmdb-devel",
    "lmdbxx",
    "mtxclient-devel",
    "nlohmann-json",
    "olm-devel",
    "openssl-devel",
    "qt6-qtbase-private-devel",  # qqmlincubator_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "qtkeychain-devel",
    "re2-devel",
    "spdlog-devel",
]
depends = [
    "gst-plugins-bad",
    "gst-plugins-base",
    "gst-plugins-good",
    "gst-plugins-good-qt6",
]
checkdepends = [*depends]
pkgdesc = "Qt-based matrix client"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://nheko-reborn.github.io"
source = (
    f"https://github.com/Nheko-Reborn/nheko/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "a3a7578bd9386a0b9a4188fa1296fdddb7df0f846c39728b80a998f9d06f36d1"
# big stack usage
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
