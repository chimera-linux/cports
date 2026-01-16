pkgname = "hiprompt-gtk"
pkgver = "0.9"
pkgrel = 0
build_style = "makefile"
makedepends = [
    "gtk4-devel",
    "gtk4-layer-shell-devel",
    "hare",
    "hare-adwaita",
    "hare-gi",
    "hare-gtk4-layer-shell",
    "himitsu",
    "libadwaita-devel",
    "pkgconf",
]
pkgdesc = "GTK4-based prompter implementation for Himitsu"
license = "GPL-3.0-only"
url = "https://git.sr.ht/~sircmpwn/hiprompt-gtk"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "879bebb24ce66ff92ba28844efcbb39ae8bb514f745e2ea894ef7d8f72d69c15"
tools = {"AS": f"{self.profile().triplet}-as"}
# no tests
options = ["!check"]
