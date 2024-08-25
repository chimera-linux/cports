pkgname = "podman-tui"
pkgver = "1.2.1"
pkgrel = 0
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
sha256 = "e97fb24ded58d5dccb71fd21221cc2cae25853797ca44e1710baeaf3d5d77b6f"
