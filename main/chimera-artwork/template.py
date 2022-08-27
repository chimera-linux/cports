pkgname = "chimera-artwork"
pkgver = "0.99.0"
pkgrel = 0
pkgdesc = "Chimera Linux artwork"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CC-BY-SA-4.0"
url = "https://chimera-linux.org"
source = [
    f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz",
    # temporary, to be replaced with scalables later
    ("https://ftp.octaforge.org/q66/random/wp_light.png", False),
    ("https://ftp.octaforge.org/q66/random/wp_dark.png", False),
]
sha256 = [
    "054efb42c524a7a1249e1133ed57901659dc599a7c09f4a7ee42bb76101a5933",
    "52a8c7cfe2b97f3d26ac6937af7ae266e0e5b1aebe687800f5c56c744c15ebfb",
    "314db662b0f36acc776db3fc284852f6ce19c71f8e70bf22edd41f3d30402845",
]

def do_install(self):
    from cbuild.core import paths

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
    sp = paths.sources() / f"{pkgname}-{pkgver}"
    dp = "usr/share/backgrounds/chimera"
    self.install_file(sp / "wp_light.png", dp, name = "bg-l.png")
    self.install_file(sp / "wp_dark.png", dp, name = "bg-d.png")
    self.install_file(
        self.files_path / "chimera.xml",
        "usr/share/gnome-background-properties"
    )
