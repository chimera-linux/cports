pkgname = "papirus-icon-theme"
pkgver = "20250501"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Pixel perfect icon theme"
license = "GPL-3.0-or-later"
url = "https://github.com/PapirusDevelopmentTeam/papirus-icon-theme"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3831a487f813479ad3224fdbfb0c7023f23056899bc78c93737f341aa655558e"
# makes no sense since it's just icons
options = ["!check"]
