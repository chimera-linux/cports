pkgname = "papirus-icon-theme"
pkgver = "20250201"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Pixel perfect icon theme"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "GPL-3.0-or-later"
url = "https://github.com/PapirusDevelopmentTeam/papirus-icon-theme"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "01a7a07293db9e22437b96fae9d7fd8dad74c33c5460af8c86227973cb3a9846"
# makes no sense since it's just icons
options = ["!check"]
