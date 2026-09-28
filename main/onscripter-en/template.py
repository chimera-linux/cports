pkgname = "onscripter-en"
pkgver = "2025.06.08"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
hostmakedepends = [
    "pkgconf",
]
makedepends = [
    "bzip2-devel",
    "freetype-devel",
    "libjpeg-turbo-devel",
    "libogg-devel",
    "libvorbis-devel",
    "libx11-devel",
    "sdl1.2_image-devel",
    "sdl1.2_mixer-devel",
    "sdl1.2_ttf-devel",
    "sdl12-compat-devel",
    "smpeg0-devel",
]
checkdepends = ["gtest-devel"]
pkgdesc = "Visual novel engine"
license = "GPL-2.0-or-later"
url = "https://galladite.net/~galladite/ons-en"
source = f"https://github.com/Galladite27/ONScripter-EN/archive/refs/tags/{pkgver.replace('.', '-')}.tar.gz"
sha256 = "29d15582fafebbd7c06feb598af74871f1a346397752e970c867360b367d47b8"
# cross: scuffed custom configure script
options = ["!cross"]
