pkgname = "mg"
pkgver = "20260227"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["ncurses-devel", "libbsd-devel"]
pkgdesc = "Micro GNU Emacs"
license = "custom:none"
url = "https://github.com/hboetes/mg"
source = f"https://github.com/hboetes/mg/archive/{pkgver}.tar.gz"
sha256 = "21877e912a63c69253538dc8ba6ae3beb1c89f35222e8381d14320f6537cec89"
# This package does not have a check instruction
options = ["!check"]
