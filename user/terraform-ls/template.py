pkgname = "terraform-ls"
pkgver = "0.35.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terraform language server"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "MPL-2.0"
url = "https://github.com/hashicorp/terraform-ls"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dcbae6aab18141ea7b2e69526cf248caa49613db234c86f275e049c0b9948ebd"
# Tests requires network connection
options = ["!check"]
