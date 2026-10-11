pkgname = "katifetch"
pkgver = "13.1"
pkgrel = 0
build_style = "meta"
depends = ["bash"]
pkgdesc = "Customizable system information tool written in Bash"
license = "MIT"
url = "https://github.com/ximimoments/katifetch"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "57018797a61ab6befb80a0b76cdf7ca457421ef8cfc030fe41d77a78b017fd30"

def install(self):
    self.install_bin("katifetch")
