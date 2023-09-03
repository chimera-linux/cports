pkgname = "netavark"
pkgver = "1.7.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo",
    "go-md2man",
    "protobuf",
]
makedepends = [
    "linux-headers",
    "rust",
]
pkgdesc = "Container network stack"
maintainer = "roastveg <louis@hamptonsoftworks.com>"
license = "Apache-2.0"
url = "https://github.com/containers/netavark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b0ed7d80fd96ef2af88e7a001d91024919125e5842d9772de94648044630e116"
