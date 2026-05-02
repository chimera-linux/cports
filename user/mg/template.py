pkgname = "mg"
pkgver = "3.7"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
make_build_args = ["V=1"]
makedepends = ["ncurses-devel"]
pkgdesc = "Micro (GNU) Emacs-like text editor"
maintainer = "Christiano Haesbaert <haesbaert@haesbaert.org>"
license = "custom:none"
url = "https://github.com/troglobit/mg"
source = f"{url}/releases/download/v{pkgver}/mg-{pkgver}.tar.gz"
sha256 = "05101360d2194392da0950e8b6f18d067d8af0fd2f572461ba4d4e7b4ccbb4c1"
hardening = ["vis", "cfi", "!int"]
