pkgname = "bazel"
pkgver = "7.3.0"
pkgrel = 0
hostmakedepends = [
    "bash",
]
makedepends = [
    "java-jdk-openjdk21-default",
    "linux-headers",
    "python",
    "unzip",
    "zip",
]
depends = ["java-jdk-openjdk21-default"]
pkgdesc = "Bazel build system"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "Apache-2.0"
url = "https://bazel.build"
source = f"https://github.com/bazelbuild/bazel/releases/download/{pkgver}/bazel-{pkgver}-dist.zip"
sha256 = "c2bff8a5e8b7357b5a2e521d4b63351091ae0c6b21a31c1f9dacf8c7928fc6e1"
# Enabled via patch file
# hardening = ["vis"]
options = ["!cross"]


def do_build(self):
    self.do(
        "bash",
        "compile.sh",
        env={
            "EXTRA_BAZEL_ARGS": "--tool_java_runtime_version=local_jdk",
        },
    )


def do_install(self):
    self.install_bin("output/bazel")
