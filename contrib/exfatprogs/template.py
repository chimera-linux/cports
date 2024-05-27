pkgname = "exfatprogs"
pkgver = "1.2.3"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
]
makedepends = ["linux-headers"]
pkgdesc = "ExFAT filesystem utilities"
maintainer = "Val Packett <val@packett.cool>"
license = "GPL-2.0-only"
url = "https://github.com/exfatprogs/exfatprogs"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a8ecebeb31cc23652d82af0853214ce85dba6021a9e8affb5aa38f47ae0f7975"
