pkgname = "xournalpp"
pkgver = "1.3.8"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # cpptrace is fetched directly during build; we don't want that.
    "-DENABLE_CPPTRACE=OFF",
]
hostmakedepends = [
    "cmake",
    "gettext",
    "help2man",
    "ninja",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "gtksourceview4-devel",
    "librsvg-devel",
    "libsndfile-devel",
    "libxml2-devel",
    "libzip-devel",
    "lua5.4-devel",
    "poppler-devel",
    "portaudio-devel",
    "qpdf-devel",
    "qpdf-devel-static",  # cmake lol
]
pkgdesc = "Handwriting notetaking software with PDF annotation support"
license = "GPL-2.0-or-later"
url = "https://github.com/xournalpp/xournalpp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e6f64f1aa3cd58a5221200af3b907f96471fb04144fa29084febea6b44e52bc0"
# known overflow in tablet handling thread
tool_flags = {
    "CXXFLAGS": ["-DNDEBUG"],
    "LDFLAGS": ["-Wl,-z,stack-size=0x200000"],
}
