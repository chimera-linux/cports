pkgname = "cliphist"
pkgver = "0.4.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
depends = ["wl-clipboard", "xdg-utils"]
pkgdesc = "Wayland clipboard manager"
maintainer = "Callum Andrew <contact@candrew.net>"
license = "GPL-3.0-only"
url = "https://github.com/sentriz/cliphist"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e492d6cd4e1bfc77582e32e25a3683687f2ff22e8d390cd06e14d21d7bef32c2"
# objcopy fails on ppc
options = ["!debug"]
