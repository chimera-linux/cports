pkgname = "xournalpp"
pkgver = "1.2.8"
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
sha256 = "f42d81e9509d4bd2d4c2cb2c54049c8518381aa9500c0671febd6c518010e0a7"
# known overflow in tablet handling thread
tool_flags = {
    "CXXFLAGS": ["-DNDEBUG"],
    "LDFLAGS": ["-Wl,-z,stack-size=0x200000"],
}
