pkgname = "fonts-maple-mono"
pkgver = "7.9"
pkgrel = 0
pkgdesc = "Monospace font with round corners and ligatures"
license = "OFL-1.1"
url = "https://font.subf.dev"
source = f"https://github.com/subframe7536/maple-font/releases/download/v{pkgver}/MapleMono-OTF.zip"
sha256 = "ecf47b851ae4001b00564399511af8dc9615339d3ae9ded54e8547d6d1ad3da1"


def install(self):
    self.install_file("*.otf", "usr/share/fonts/maple-mono", glob=True)
    self.install_license("LICENSE.txt")
