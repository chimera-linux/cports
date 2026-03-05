pkgname = "elixir"
pkgver = "1.19.5"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["erlang"]
depends = ["erlang"]
pkgdesc = "Functional, concurrent, general-purpose programming language"
license = "Apache-2.0"
url = "https://github.com/elixir-lang/elixir"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "10750b8bd74b10ac1e25afab6df03e3d86999890fa359b5f02aa81de18a78e36"
# check doesn't work
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
