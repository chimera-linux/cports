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
    "1504c301f6d417f2626085337e5c3bb3dc0282265089396ab36bfe1942feef1c",
]
hardening = ["vis", "cfi"]
# fcgiwrap has no checks
options = ["!check"]


def post_install(self):
    self.install_license(self.sources_path / "COPYING")
