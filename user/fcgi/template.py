pkgname = "fcgi"
pkgver = "2.4.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "slibtool", "pkgconf"]
pkgdesc = "Language independent, high performance extension to CGI"
maintainer = "mia <mia@mia.jetzt>"
license = "custom:fcgi"
url = "https://github.com/FastCGI-Archives/fcgi2"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "c0e0d9cc7d1e456d7278c974e2826f593ef5ca555783eba81e7e9c1a07ae0ecc"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("fcgi-devel")
def _(self):
    return self.default_devel()
