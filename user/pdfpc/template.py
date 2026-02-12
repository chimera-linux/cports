pkgname = "pdfpc"
pkgver = "4.7.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "libgee-devel",
    "ninja",
    "pkgconf",
    "vala",
]
makedepends = [
    "discount-devel",
    "gst-plugins-base-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libgee-devel",
    "poppler-devel",
    "qrencode-devel",
    "vala-devel",
    "webkitgtk-devel",
    "zstd-devel",
]
pkgdesc = "Presenter console with multi-monitor support for PDF files"
license = "GPL-3.0-or-later"
url = "https://pdfpc.github.io"
source = f"https://github.com/pdfpc/pdfpc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0083a958a2e9288a15c31aabb76b3eadf104672b4e815017f31ffa0d87db02ec"
