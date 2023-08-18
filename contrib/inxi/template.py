pkgname = "inxi"
_pver = "3.3.29-1"
pkgver = f"{_pver.replace('-', '.')}"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://github.com/smxi/inxi"
source = f"https://github.com/smxi/inxi/archive/refs/tags/{_pver}.tar.gz"
sha256 = "5802cc6fe780fb9f24a097c326ffce9b31abe2f5b70957e21c6973e008bbf44b"


def do_install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")
