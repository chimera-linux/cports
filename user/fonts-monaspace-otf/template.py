pkgname = "fonts-monaspace-otf"
pkgver = "1.300"
pkgrel = 0
pkgdesc = "GitHub Next Monaspace fonts"
license = "OFL-1.1"
url = "https://github.com/githubnext/monaspace"
source = [
    f"{url}/releases/download/v{pkgver}/monaspace-static-v{pkgver}.zip",
    f"!{url}/blob/v{pkgver}/LICENSE?raw=true",
]
sha256 = [
    "b857609c97dcf8c55e3fc408c6bf3e62b50b53122d6b1cc6813554e39cbebccc",
    "0e84e5f7dd6f05e74a00f2fb828ca43e489d954f5509ff0fa439ea18c0d35fe9",
]


def install(self):
    self.install_file("*/*.otf", "usr/share/fonts/monaspace", glob=True)
    self.install_license(self.sources_path / "LICENSE")
