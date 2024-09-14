pkgname = "papirus-icon-theme"
pkgver = "20240501"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Pixel perfect icon theme"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "GPL-3.0-or-later"
url = "https://github.com/PapirusDevelopmentTeam/papirus-icon-theme"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c12a64963639afffc5c5425c4d8fd09e9d5510bbc4c408a1fec9a1d617c5089b"
# makes no sense since it's just icons
options = ["!check"]
