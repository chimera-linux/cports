pkgname = "winetricks"
pkgver = "20240105"
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
    "cmd:zenity!zenity",
    "cmd:xz!xz",
]
pkgdesc = "Helper script for Wine"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.1-or-later"
url = "https://github.com/Winetricks/winetricks"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e92929045cf9ffb1e8d16ef8fd971ea1cf63a28a73916b1951e9553c94482f61"
# check: requires connection
options = ["!check"]
