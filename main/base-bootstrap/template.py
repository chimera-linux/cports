pkgname = "base-bootstrap"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = ["base-files", "musl", "bsdutils", "bsdgrep", "bsdsed", "dash", "awk"]
pkgdesc = "Scriptless base metapackage for bootstrapping systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

options = ["bootstrap"]
