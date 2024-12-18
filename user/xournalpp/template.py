pkgname = "xournalpp"
pkgver = "1.2.5"
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
maintainer = "daringcuteseal <daringcuteseal@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/xournalpp/xournalpp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9a67fb0073bc5dd97b32d5c740ce583d90bc530532e4c6d74d187c840792fe3e"
# known overflow in tablet handling thread
tool_flags = {
    "CXXFLAGS": ["-DNDEBUG"],
    "LDFLAGS": ["-Wl,-z,stack-size=0x200000"],
}
