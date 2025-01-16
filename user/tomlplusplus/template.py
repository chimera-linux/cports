pkgname = "tomlplusplus"
pkgver = "3.4.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "cmake", "pkgconf"]
makedepends = []
pkgdesc = "Header-only TOML config file parser and serializer for C++17"
maintainer = "kkflt <kkflt@cyberdude.com>"
license = "MIT"
url = "https://github.com/marzer/tomlplusplus"
source = f"{url}/archive/v{pkgver}/tomlplusplus-v{pkgver}.tar.gz" 
sha256 = "8517f65938a4faae9ccf8ebb36631a38c1cadfb5efa85d9a72e15b9e97d25155"

def post_install(self):
	self.install_license("LICENSE")

@subpackage("tomlplusplus-devel")
def _(self):
	return self.default_devel()
