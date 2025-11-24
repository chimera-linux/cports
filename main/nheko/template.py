pkgname = "nheko"
pkgver = "0.12.1"
pkgrel = 1
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
    "curl-devel",
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "kdsingleapplication-devel",
    "libevent-devel",
    "lmdb-devel",
    "lmdbxx",
    "mtxclient-devel",
    "nlohmann-json",
    "olm-devel",
    "openssl3-devel",
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
license = "GPL-3.0-or-later"
url = "https://nheko-reborn.github.io"
source = (
    f"https://github.com/Nheko-Reborn/nheko/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "81cc613ee2420b1289c9cc7aeee81cae69a153971fd3112225e48d1c7b224ea5"
# big stack usage
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
