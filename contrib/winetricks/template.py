pkgname = "winetricks"
pkgver = "20240105"
pkgrel = 0
build_style = "makefile"
depends = [
    "virtual:cmd:7z!7zip",
    "virtual:cmd:ar!llvm-binutils",
    "virtual:cmd:cabextract!cabextract",
    "virtual:cmd:curl!curl",
    "virtual:cmd:sha256sum!chimerautils",
    "virtual:cmd:unzip!unzip",
    "virtual:cmd:wine!wine",
    "virtual:cmd:xdg-open!xdg-utils",
    "virtual:cmd:zenity!zenity",
    "virtual:cmd:xz!xz",
]
pkgdesc = "Helper script for Wine"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.1-or-later"
url = "https://github.com/Winetricks/winetricks"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e92929045cf9ffb1e8d16ef8fd971ea1cf63a28a73916b1951e9553c94482f61"
# check: requires connection
options = ["!check"]
