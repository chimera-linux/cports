pkgname = "winetricks"
pkgver = "20250102"
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
sha256 = "24d339806e3309274ee70743d76ff7b965fef5a534c001916d387c924eebe42e"
# check: requires connection
options = ["!check"]
