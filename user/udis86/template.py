pkgname = "udis86"
pkgver = "1.7.2_git20221013"
_commit = "5336633af70f3917760a6d441ff02d93477b0c86"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "libtool", "python", "automake"]
makedepends = []
pkgdesc = "Disassembler Library for x86 and x86-64"
maintainer = "kkflt <kkflt@cyberdude.com>"
license = "BSD-2-Clause"
url = "https://github.com/canihavesomecoffee/udis86"
source = f"https://github.com/canihavesomecoffee/udis86/archive/{_commit}/udis86-{_commit}.tar.gz"
sha256 = "2f459fafa19535ef1be417bf7614e4f92475e5787d7ba76df20287cc29d1b5a9"

def post_install(self):
	self.install_license("LICENSE")
	
@subpackage("udis86-devel")
def _(self):
	return self.default_devel()
