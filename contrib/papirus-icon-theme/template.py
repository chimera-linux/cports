pkgname = "papirus-icon-theme"
pkgver = "20240201"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake"]
pkgdesc = "Pixel perfect icon theme"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "GPL-3.0-or-later"
url = "https://github.com/PapirusDevelopmentTeam/papirus-icon-theme"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8ff3caded7862e5e6f531dbae54b213ff1cd3666d26f23357c6183173856f380"
# makes no sense since it's just icons
options = ["!check"]
