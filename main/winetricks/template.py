pkgname = "winetricks"
pkgver = "20260125"
pkgrel = 0
build_style = "makefile"
depends = [
    "cmd:7z!7zip",
    "cmd:ar!llvm-binutils",
    "cmd:cabextract!cabextract",
    "cmd:curl!curl",
    "cmd:sha256sum!chimerautils",
    "cmd:unzip!unzip",
    "cmd:wine!wine",
    "cmd:xdg-open!xdg-utils",
    "cmd:xz!xz",
    "cmd:zenity!zenity",
]
pkgdesc = "Helper script for Wine"
license = "LGPL-2.1-or-later"
url = "https://github.com/Winetricks/winetricks"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2890bd9fbbade4638e58b4999a237273192df03b58516ae7b8771e09c22d2f56"
# check: requires connection
options = ["!check"]
