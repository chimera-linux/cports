pkgname = "obs-pipewire-audio-capture"
pkgver = "1.1.5"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "obs-studio-devel",
    "pipewire-devel",
]
pkgdesc = "OBS plugin for capturing device and application audio using pipewire"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "GPL-2.0-or-later"
url = "https://obsproject.com/forum/resources/pipewire-audio-capture.1458"
source = f"https://github.com/dimtpap/obs-pipewire-audio-capture/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9746c0564cc1e41aa3acf5bc516f4d3646450628c34bfaca49485e45a32cde23"
hardening = ["vis", "!cfi"]
