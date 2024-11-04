pkgname = "base-vpsfree"
pkgver = "0.2"
pkgrel = 3
archs = ["x86_64"]
depends = [
    "!base-full-firmware",  # we're not loading a kernel, so...
    "!base-full-kernel",  # we don't care about kernel at all
    "!base-full-session",  # we don't care about elogind here by default
    "!base-full-sound",  # no sound on a vps
    "!chrony-dinit-links",  # we don't want ntp to come up
    "!elogind-dinit-links",  # not necessary by default (and may not work)
    "!nyagetty-dinit-links",  # don't want default ttys
    "!pipewire-dinit-links",  # no sound on a vps
    "!udev-dinit-links",  # don't want udev to run
    "!wireplumber-dinit-links",  # no sound on a vps
    "resolvconf-none",  # resolv.conf is managed externally
]
replaces = ["dinit-chimera"]
pkgdesc = "Chimera base package for vpsfree.cz VPSes"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"
broken_symlinks = ["usr/lib/dinit.d/boot.d/*"]
options = ["!autosplit"]


def install(self):
    self.install_dir("usr/lib/dinit.d/boot.d")
    # replace dinit-chimera cgroups init
    self.install_file(
        self.files_path / "cgroups.sh",
        "usr/lib/dinit.d/early/scripts",
        mode=0o755,
    )
    self.install_link(
        "usr/lib/dinit.d/boot.d/agetty-service@console",
        "../agetty-service@console",
    )
    self.install_link("usr/lib/dinit.d/boot.d/ifupdown-ng", "../ifupdown-ng")
    self.install_link("usr/lib/dinit.d/boot.d/sshd", "../sshd")


@subpackage("base-vpsfree-meta")
def _(self):
    self.subdesc = "optional dependencies"
    self.depends = [
        "ifupdown-ng",  # needed for default networking
        "openssh",  # needed for remote access
    ]
    self.install_if = [self.parent]
    self.broken_symlinks = ["usr/lib/dinit.d/boot.d/*"]
    self.options = ["!autosplit"]
    return [
        "usr/lib/dinit.d/boot.d/ifupdown-ng",
        "usr/lib/dinit.d/boot.d/sshd",
    ]
