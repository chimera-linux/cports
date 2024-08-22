pkgname = "onscripter-en"
pkgver = "2024.07.21"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
hostmakedepends = [
    "gsed",
    "pkgconf",
]
makedepends = [
    "bzip2-devel",
    "freetype-devel",
    "libogg-devel",
    "libvorbis-devel",
    "libx11-devel",
    "sdl1.2_image-devel",
    "sdl1.2_mixer-devel",
    "sdl1.2_ttf-devel",
    "sdl12-compat-devel",
    "smpeg0-devel",
]
pkgdesc = "Visual novel engine"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://galladite.net/~galladite/ons-en"
source = f"https://github.com/Galladite27/ONScripter-EN/archive/refs/tags/{pkgver.replace('.', '-')}.tar.gz"
sha256 = "af61fac4833b717b4175b6a66969cf8ef4fc97f89b6255b0dcecac2bc9daec28"
# cross: scuffed custom configure script
# check: no tests
options = ["!cross", "!check"]
exec_wrappers = [("/usr/bin/gsed", "sed")]
