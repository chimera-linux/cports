pkgname = "sakura"
pkgver = "3.8.7"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "perl", "pkgconf", "gettext"]
makedepends = ["vte-gtk3-devel"]
depends = ["desktop-file-utils"]
pkgdesc = "Libvte based terminal emulator"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "GPL-2.0-only"
url = "https://launchpad.net/sakura"
source = f"{url}/trunk/{pkgver}/+download/sakura-{pkgver}.tar.gz"
sha256 = "c0feba49d88a039ce56563f43ee59a96fbf9805c02e69775a8fdc45763b8545a"
hardening = ["cfi", "vis"]
