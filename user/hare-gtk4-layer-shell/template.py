pkgname = "hare-gtk4-layer-shell"
pkgver = "0.1.0"
pkgrel = 0
build_style = "makefile"
makedepends = [
    "at-spi2-core-devel",
    "gtk4-layer-shell-devel",
    "hare-gi",
]
pkgdesc = "Hare bindings to gtk4-layer-shell"
license = "MPL-2.0"
url = "https://git.sr.ht/~sircmpwn/hare-gtk4-layer-shell"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "0264500c71b716483bb9dd8c26f979bdabec01d46d988b329eaeb1f93c4a9d41"
# no tests
options = ["!check"]
