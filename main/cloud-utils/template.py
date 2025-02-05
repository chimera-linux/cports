pkgname = "cloud-utils"
pkgver = "0.33"
pkgrel = 1
build_style = "makefile"
depends = [
    "bash",
    "e2fsprogs",
    "file",
    "qemu-img",
    "ugetopt",
    "util-linux-fdisk",
    "util-linux-mount",
]
pkgdesc = "Utilities to work with cloud images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://launchpad.net/cloud-utils"
source = f"https://github.com/canonical/cloud-utils/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "338770d637788466aacfcbcec17a8d0046f92a13cc3b25fce8fceadb02a7339f"
# not worth it (generally requires root)
options = ["!check"]


def post_extract(self):
    # unneeded
    self.rm("bin/ubuntu-cloudimg-query")
    self.rm("bin/vcs-run")


@subpackage("cloud-utils-ec2metadata")
def _(self):
    self.subdesc = "retrieve metadata on AWS EC2"
    self.depends = ["python-urllib3"]
    self.install_if = [self.parent]

    return ["cmd:ec2metadata"]


@subpackage("cloud-utils-growpart")
def _(self):
    self.subdesc = "grow disk partitions"
    self.depends = ["util-linux-fdisk", "util-linux-mount"]
    self.install_if = [self.parent]

    return ["cmd:growpart"]


@subpackage("cloud-utils-localds")
def _(self):
    self.subdesc = "create cloud-init configuration disk"
    self.depends = [
        "bash",
        "dosfstools",
        "mtools",
        "qemu-img",
        "xorriso",
    ]
    self.install_if = [self.parent]

    return ["cmd:cloud-localds"]


@subpackage("cloud-utils-multipart")
def _(self):
    self.subdesc = "write files to a MIME multipart document"
    self.depends = ["python"]
    self.install_if = [self.parent]

    return ["cmd:write-mime-multipart"]
