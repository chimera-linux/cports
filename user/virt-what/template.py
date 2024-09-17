pkgname = "virt-what"
pkgver = "1.27"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "Script for getting host virtual-machine context"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-2.0-only"
url = "https://people.redhat.com/~rjones/virt-what"
source = f"{url}/files/virt-what-{pkgver}.tar.gz"
sha256 = "d4d9bd9d4ae59095597443fac663495315c7eb4330b872aa5f062df38ac69bf1"
# check: tests depend on kvm kernel module (and other modules)
options = ["!check"]
