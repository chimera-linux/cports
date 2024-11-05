pkgname = "terraform"
pkgver = "1.9.8"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags=-X github.com/hashicorp/terraform/version.dev=no"]
hostmakedepends = ["go"]
pkgdesc = "Tool for building, changing and versioning infrastructure"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "BUSL-1.1"
url = "https://github.com/hashicorp/terraform"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "122af732dbe90d856ec9e77302f62df1ea95566e98e9dda3ad6f7d100923417e"
# Terraform tests are not stable
options = ["!check"]
