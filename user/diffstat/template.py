pkgname = "diffstat"
pkgver = "1.67"
pkgrel = 1
build_style = "configure"
configure_args = ["--prefix=/usr"]
pkgdesc = "Display a histogram of diff changes"
license = "MIT OR Apache-2.0"
url = "https://invisible-island.net/diffstat"
source = [
    f"https://invisible-mirror.net/archives/diffstat/diffstat-{pkgver}.tgz",
]
sha256 = [
        "760ed0c99c6d643238d41b80e60278cf1683ffb94a283954ac7ef168c852766a",
        ]

def post_install(self):
    self.install_license("COPYING")
