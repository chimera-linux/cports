pkgname = "podman-tui"
pkgver = "1.2.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
makedepends = [
    "libbtrfs-devel",
    "linux-headers",
]
checkdepends = [
    "gpgme-devel",
    "pkgconf",
]
go_build_tags = [
    "exclude_graphdriver_devicemapper",
    "exclude_graphdriver_btrfs",
    "btrfs_noversion",
    "containers_image_openpgp",
    "remote",
]
pkgdesc = "Podman terminal UI"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/containers/podman-tui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "feb8249ea05d7f53e2bc8036cff439d04a09b9628f70355e280cfc5d7e8919f9"
