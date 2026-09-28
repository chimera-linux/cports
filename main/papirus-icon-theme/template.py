pkgname = "papirus-icon-theme"
pkgver = "20260801"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Pixel perfect icon theme"
license = "GPL-3.0-or-later"
url = "https://github.com/PapirusDevelopmentTeam/papirus-icon-theme"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "646f622e9e7e9e65eef9d0ab58999d4920ddb33d98e6a75232627cfe3bd508f9"
# makes no sense since it's just icons
options = ["!check"]
