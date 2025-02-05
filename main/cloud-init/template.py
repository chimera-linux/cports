pkgname = "cloud-init"
pkgver = "24.2"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-installer",
    "python-jinja2",
    "python-pyyaml",
    "python-requests",
    "python-setuptools",
]
depends = [
    "!chrony-dinit-links",  # cloud-init wants to manage that
    "cloud-utils-growpart",
    "ifupdown-ng",
    "iproute2",
    "python-configobj",
    "python-jsonpatch",
    "python-jsonschema",
    "python-netifaces",
    "python-pyyaml",
    "python-requests",
    "shadow",
    "tzdb",
    "util-linux-mount",
]
checkdepends = [
    "bash",
    "gptfdisk",
    "procps",
    "python-netifaces",
    "python-passlib",
    "python-pyserial",
    "python-pytest",
    "python-pytest-mock",
    "python-responses",
    "python-tox",
    "util-linux-fdisk",
    "util-linux-mount",
]
pkgdesc = "Cloud init scripts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 OR GPL-3.0-only"
url = "https://cloud-init.io"
source = (
    f"https://github.com/canonical/cloud-init/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "b70d49e9e5bd891b0bb021b09b80aed501c81e2bef5f1cba00561adfd8d2e974"
# checkdepends
options = ["!check"]


def post_extract(self):
    for f in [
        "cloudinit/distros/alpine.py",
        "templates/chrony.conf.alpine.tmpl",
        "templates/hosts.alpine.tmpl",
        "tests/unittests/distros/test_alpine.py",
    ]:
        self.cp(f, f.replace("alpine", "chimera"))


# using pep517 does not render templates properly etc.
def build(self):
    self.do("python", "setup.py", "build")


def install(self):
    self.do(
        "python",
        "setup.py",
        "install",
        "--prefix=/usr",
        f"--root={self.chroot_destdir}",
    )


def post_install(self):
    # our services
    self.install_file(
        self.files_path / "cloud-init.wrapper", "usr/libexec", mode=0o755
    )
    self.install_service(self.files_path / "cloud-config")
    self.install_service(self.files_path / "cloud-final")
    self.install_service(self.files_path / "cloud-init-local")
    self.install_service(self.files_path / "cloud-init")

    # delete foreign distro files
    for d in [
        "almalinux",
        "alpine",
        "arch",
        "azurelinux",
        "centos",
        "cloudlinux",
        "cos",
        "debian",
        "fedora",
        "freebsd",
        "gentoo",
        "mariner",
        "openbsd",
        "opensuse*",
        "photon",
        "redhat",
        "rhel",
        "sle*",
        "suse",
        "ubuntu",
    ]:
        self.uninstall(f"etc/cloud/templates/*.{d}.tmpl", glob=True)

    for d in [
        "almalinux",
        "alpine",
        "amazon",
        "arch",
        "azurelinux",
        "bsd",
        "centos",
        "cloudlinux",
        "cos",
        "debian",
        "dragonflybsd",
        "eurolinux",
        "fedora",
        "freebsd",
        "gentoo",
        "mariner",
        "miraclelinux",
        "netbsd",
        "OpenCloudOS",
        "openbsd",
        "openeuler",
        "openmandriva",
        "opensuse*",
        "photon",
        "rhel",
        "rhel_util",
        "rocky",
        "sle*",
        "suse",
        "TencentOS",
        "ubuntu",
        "virtuozzo",
    ]:
        self.uninstall(
            f"usr/lib/python*/site-packages/cloudinit/distros/{d}.py", glob=True
        )
        self.uninstall(
            f"usr/lib/python*/site-packages/cloudinit/distros/__pycache__/{d}.*.pyc",
            glob=True,
        )

    self.uninstall("etc/cloud/templates/sources.list.*.tmpl", glob=True)
    self.uninstall(
        "usr/lib/python*/site-packages/cloudinit/distros/parsers/sys_conf.py",
        glob=True,
    )
    self.uninstall(
        "usr/lib/python*/site-packages/cloudinit/distros/parsers/__pycache__/sys_conf.*.pyc",
        glob=True,
    )

    # systemd-related
    self.uninstall("etc/cloud/templates/timesyncd.conf.tmpl")
    self.uninstall("etc/cloud/templates/systemd.resolved.conf.tmpl")
    self.uninstall("etc/systemd")
    self.uninstall("lib/systemd")

    # move udev rules that get put in wrong place
    self.rename("lib/udev", "usr/lib/udev", relative=False)

    # irrelevant modules
    for mod in [
        "apt_*",
        "byobu",
        "fan",
        "grub_dpkg",
        "landscape",
        "lxd",
        "rh_subscription",
        "snap",
        "spacewalk",
        "ubuntu_autoinstall",
        "ubuntu_drivers",
        "yum_add_repo",
        "zypper_add_repo",
    ]:
        self.uninstall(
            f"usr/lib/python*/site-packages/cloudinit/config/cc_{mod}.py",
            glob=True,
        )
        self.uninstall(
            f"usr/lib/python*/site-packages/cloudinit/config/__pycache__/cc_{mod}.*.pyc",
            glob=True,
        )

    # irrelevant docs
    for d in [
        "add-apt-repos",
        "apt",
        "update-apt",
        "yum-repo",
    ]:
        self.uninstall(
            f"usr/share/doc/cloud-init/examples/cloud-config-{d}.txt"
        )

    # install our own stuff
    self.install_file(self.files_path / "interfaces", "etc/network")
