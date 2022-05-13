pkgname = "chimera-artwork"
pkgver = "0.99.0"
pkgrel = 0
pkgdesc = "Chimera Linux artwork"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CC-BY-SA-4.0"
url = "https://chimera-linux.org"
source = f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "054efb42c524a7a1249e1133ed57901659dc599a7c09f4a7ee42bb76101a5933"

def do_install(self):
    for f in ["png", "svg"]:
        self.install_file(f"chimera-logo.{f}", "usr/share/chimera-artwork")
    for s in [16, 22, 32, 48, 64, 128, 256, 512, 1024]:
        self.install_file(
            f"icons/chimera-logo-{s}.png",
            f"usr/share/icons/hicolor/{s}x{s}/apps",
            name = "chimera-logo.png"
        )
    self.install_file(
        "icons/chimera-logo.svg", "usr/share/icons/hicolor/scalable/apps"
    )
