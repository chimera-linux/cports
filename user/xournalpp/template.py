pkgname = "xournalpp"
pkgver = "1.2.7"
pkgrel = 0
build_style = "cmake"
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
]
pkgdesc = "Handwriting notetaking software with PDF annotation support"
license = "GPL-2.0-or-later"
url = "https://github.com/xournalpp/xournalpp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cd20608417fef374e5360ec96c9f56c61236d45e0d35d33b48346ed39eaf025d"
# known overflow in tablet handling thread
tool_flags = {
    "CXXFLAGS": ["-DNDEBUG"],
    "LDFLAGS": ["-Wl,-z,stack-size=0x200000"],
}
