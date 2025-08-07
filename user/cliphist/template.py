pkgname = "cliphist"
pkgver = "0.6.1"
pkgrel = 9
build_style = "go"
hostmakedepends = ["go"]
depends = ["wl-clipboard", "xdg-utils"]
pkgdesc = "Wayland clipboard manager"
license = "GPL-3.0-only"
url = "https://github.com/sentriz/cliphist"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "db0f25ba3e9173dcb257d66cb1293e277a8bdfed11cc8d6b38b7473b0947781d"
# cannot use nopTestdeps{} blabla ...
options = ["!check"]
