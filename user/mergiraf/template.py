pkgname = "mergiraf"
pkgver = "0.18.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
checkdepends = ["git", "jj"]
pkgdesc = "Syntax-aware git merge driver"
license = "GPL-3.0-only"
url = "https://mergiraf.org"
source = f"https://codeberg.org/mergiraf/mergiraf/archive/v{pkgver}.tar.gz"
sha256 = "28b5187a1cd201c96aee6732dda9084406ad3001ed93fcff4e9fc3b740dbe471"
# checks may be disabled
options = []

if self.profile().arch in ["loongarch64"]:
    # checkdepends can't be installed
    options += ["!check"]
