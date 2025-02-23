pkgname = "fzy"
pkgver = "1.0"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Simple, fast fuzzy finder for the terminal"
maintainer = "Aaron John <unrealapex@disroot.org>"
license = "MIT"
url = "https://github.com/jhawthorn/fzy"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "80257fd74579e13438b05edf50dcdc8cf0cdb1870b4a2bc5967bd1fdbed1facf"

def post_install(self):
	self.install_license("LICENSE")
	self.install_man("fzy.1")
