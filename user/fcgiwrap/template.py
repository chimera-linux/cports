pkgname = "fcgiwrap"
pkgver = "1.1.0"
pkgrel = 0
build_style = "gnu_configure"
# without an empty prefix, everything gets installed to /usr/usr/
configure_args = ["--prefix="]
make_dir = "."
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["fcgi-devel"]
pkgdesc = "Simple server for running CGI applications over FastCGI"
maintainer = "mia <mia@mia.jetzt>"
license = "MIT"
url = "https://github.com/gnosek/fcgiwrap"
source = [
    f"{url}/archive/{pkgver}.tar.gz",
    # final tag doesn't include license
    "!https://raw.githubusercontent.com/gnosek/fcgiwrap/b6696a1495dc818d0b22d9c2e9be7c618e25b3af/COPYING",
]
sha256 = [
    "4c7de0db2634c38297d5fcef61ab4a3e21856dd7247d49c33d9b19542bd1c61f",
    "cb1b716d0c1a361e05a6bc126eea53c0e06f6161affa66a01b6f4d779d5b58b7",
]
hardening = ["vis", "cfi"]
# fcgiwrap has no checks
options = ["!check"]


def post_install(self):
    self.install_license(self.sources_path / "COPYING")
