pkgname = "cliphist"
pkgver = "0.5.0"
pkgrel = 9
build_style = "go"
hostmakedepends = ["go"]
depends = ["wl-clipboard", "xdg-utils"]
pkgdesc = "Wayland clipboard manager"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://github.com/sentriz/cliphist"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "02285cf3358a1851e34f95c0c369b27284d8d0996759d759fa2bbcb5b30fb13d"
# cannot use nopTestdeps{} blabla ...
options = ["!check"]
