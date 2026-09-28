pkgname = "xournalpp"
pkgver = "1.3.4"
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
sha256 = "acc261afba7b61a5556a10e03f77a141c9a4872a2529d1ed39a0f14dbc0d87db"
# known overflow in tablet handling thread
tool_flags = {
    "CXXFLAGS": ["-DNDEBUG"],
    "LDFLAGS": ["-Wl,-z,stack-size=0x200000"],
}
